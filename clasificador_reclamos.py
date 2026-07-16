from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd

try:
    from sentence_transformers import SentenceTransformer
except ImportError as exc:  # pragma: no cover - handled at runtime
    SentenceTransformer = None  # type: ignore[assignment]
    SENTENCE_TRANSFORMERS_IMPORT_ERROR = exc
else:
    SENTENCE_TRANSFORMERS_IMPORT_ERROR = None


MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
DEFAULT_THRESHOLD = 0.45
TEXT_COLUMN = "prestacion"
REVIEW_LABEL = "Otros / Revision manual"
EXPECTED_COLUMNS = [
    "nro_solicitud",
    "periodo",
    "categoria",
    "prestacion",
    "tipo",
    "fecha_ingreso",
    "hora_ingreso",
    "distrito",
    "urbanizacion",
    "via",
    "numero",
    "referencia",
    "canal",
    "latitud",
    "longitud",
    "genero",
    "estado",
]


@dataclass(frozen=True)
class ClassificationResult:
    categoria_sugerida: str
    similitud_maxima: float
    requiere_revision: bool


def cargar_modelo(model_name: str = MODEL_NAME) -> SentenceTransformer:
    """Carga el modelo de embeddings multilingue."""
    if SentenceTransformer is None:
        raise RuntimeError(
            "No se pudo importar sentence-transformers. "
            "Instala las dependencias de requirements.txt."
        ) from SENTENCE_TRANSFORMERS_IMPORT_ERROR

    try:
        return SentenceTransformer(model_name)
    except Exception as exc:  # pragma: no cover - depends on local environment
        raise RuntimeError(f"No se pudo cargar el modelo '{model_name}': {exc}") from exc


def crear_descripciones_categorias() -> dict[str, str]:
    """Define descripciones semanticas amplias para cada categoria municipal."""
    return {
        "Limpieza publica": (
            "Reclamos sobre basura acumulada, residuos solidos, desmonte, escombros, "
            "contenedores llenos, falta de barrido, recojo de basura, desperdicios en calles, "
            "malos olores por suciedad, limpieza de mercados, veredas, avenidas, parques y espacios publicos."
        ),
        "Alumbrado publico": (
            "Reportes de luminarias apagadas, postes de luz averiados, faroles danados, "
            "falta de iluminacion en calles, parques y avenidas, lamparas que parpadean, "
            "sectores oscuros, reparacion de alumbrado publico y mantenimiento de infraestructura electrica urbana."
        ),
        "Transito": (
            "Incidencias relacionadas con semaforos averiados, congestion vehicular, desorden del trafico, "
            "senalizacion vial deficiente, estacionamiento indebido, rompemuelles, ciclovias obstruidas, "
            "cruces peatonales peligrosos, fiscalizacion del transporte y seguridad vial."
        ),
        "Areas verdes": (
            "Solicitudes sobre poda de arboles, mantenimiento de jardines, grass seco, riego de areas verdes, "
            "ramas caidas, arbustos crecidos, palmeras en riesgo, parques descuidados, retiro de vegetacion "
            "y conservacion de espacios publicos con plantas y arbolado urbano."
        ),
        "Ruido": (
            "Quejas por musica excesivamente alta, bulla vecinal, parlantes, fiestas, bares ruidosos, "
            "bocinas, maquinaria, construccion con ruido, vibraciones, ruidos molestos en horarios nocturnos "
            "o de madrugada y perturbacion del descanso."
        ),
        "Seguridad": (
            "Reclamos sobre robos, asaltos, inseguridad ciudadana, falta de serenazgo, patrullaje insuficiente, "
            "personas sospechosas, peleas en via publica, amenazas, vandalismo, consumo de alcohol en la calle, "
            "necesidad de vigilancia, camaras y proteccion en parques, colegios y zonas comerciales."
        ),
        "Otros": (
            "Consultas generales o reclamos que no encajan claramente en servicios municipales especificos; "
            "tramites, orientacion, informacion administrativa, documentos, licencias, horarios de atencion "
            "u otros pedidos ambiguos, incompletos o sin suficiente contexto."
        ),
    }


def generar_embeddings_categorias(
    model: SentenceTransformer,
    category_descriptions: dict[str, str],
) -> dict[str, Any]:
    """Genera embeddings una sola vez para las descripciones de categorias."""
    labels = list(category_descriptions.keys())
    descriptions = [category_descriptions[label] for label in labels]

    try:
        embeddings = model.encode(descriptions, convert_to_numpy=True, normalize_embeddings=True)
    except Exception as exc:
        raise RuntimeError(f"No se pudieron generar embeddings de categorias: {exc}") from exc

    return {"labels": labels, "embeddings": embeddings}


def normalizar_texto(texto: Any) -> str:
    """Aplica normalizacion minima: conversion a texto y espacios repetidos."""
    if texto is None or pd.isna(texto):
        return ""
    normalized = " ".join(str(texto).split())
    return normalized.strip()


def clasificar_texto(
    text: Any,
    model: SentenceTransformer,
    category_embeddings: dict[str, Any],
    threshold: float = DEFAULT_THRESHOLD,
) -> ClassificationResult:
    """Clasifica un reclamo individual segun la mayor similitud coseno."""
    normalized_text = normalizar_texto(text)
    if not normalized_text:
        return ClassificationResult(
            categoria_sugerida=REVIEW_LABEL,
            similitud_maxima=0.0,
            requiere_revision=True,
        )

    try:
        text_embedding = model.encode([normalized_text], convert_to_numpy=True, normalize_embeddings=True)[0]
    except Exception as exc:
        raise RuntimeError(f"No se pudo generar el embedding del reclamo: {exc}") from exc

    category_matrix = category_embeddings["embeddings"]
    labels = category_embeddings["labels"]
    similarities = category_matrix @ text_embedding

    best_index = int(similarities.argmax())
    best_similarity = float(similarities[best_index])
    best_label = str(labels[best_index])
    requires_review = best_similarity < threshold

    return ClassificationResult(
        categoria_sugerida=REVIEW_LABEL if requires_review else best_label,
        similitud_maxima=best_similarity,
        requiere_revision=requires_review,
    )


def clasificar_dataframe(
    df: pd.DataFrame,
    model: SentenceTransformer,
    threshold: float = DEFAULT_THRESHOLD,
) -> pd.DataFrame:
    """Clasifica todos los reclamos del DataFrame conservando columnas originales."""
    if TEXT_COLUMN not in df.columns:
        raise ValueError(f"Falta la columna obligatoria '{TEXT_COLUMN}' en el DataFrame.")

    category_descriptions = crear_descripciones_categorias()
    category_embeddings = generar_embeddings_categorias(model, category_descriptions)

    results = [
        clasificar_texto(
            text=value,
            model=model,
            category_embeddings=category_embeddings,
            threshold=threshold,
        )
        for value in df[TEXT_COLUMN]
    ]

    output_df = df.copy()
    output_df["categoria_sugerida"] = [result.categoria_sugerida for result in results]
    output_df["similitud_maxima"] = [result.similitud_maxima for result in results]
    output_df["requiere_revision"] = [result.requiere_revision for result in results]
    return output_df


def cargar_csv(input_path: str | Path) -> pd.DataFrame:
    """Carga el CSV de entrada y valida la presencia de la columna de texto."""
    try:
        df = pd.read_csv(input_path)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"No se encontro el archivo de entrada: {input_path}") from exc
    except pd.errors.EmptyDataError as exc:
        raise ValueError(f"El archivo CSV esta vacio: {input_path}") from exc
    except Exception as exc:
        raise RuntimeError(f"Error al leer el CSV '{input_path}': {exc}") from exc

    if TEXT_COLUMN not in df.columns:
        raise ValueError(
            f"El CSV debe incluir la columna '{TEXT_COLUMN}'. "
            f"Columnas encontradas: {list(df.columns)}"
        )

    missing_columns = [column for column in EXPECTED_COLUMNS if column not in df.columns]
    if missing_columns:
        print(
            "Advertencia: faltan columnas esperadas en el CSV: "
            f"{', '.join(missing_columns)}",
            file=sys.stderr,
        )

    return df


def guardar_csv(df: pd.DataFrame, output_path: str | Path) -> None:
    """Guarda el DataFrame clasificado en un nuevo archivo CSV."""
    output_path = Path(output_path)
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path, index=False, encoding="utf-8")
    except Exception as exc:
        raise RuntimeError(f"Error al escribir el CSV '{output_path}': {exc}") from exc


def imprimir_resumen(df: pd.DataFrame) -> None:
    """Muestra estadisticas finales del proceso."""
    total = len(df)
    counts = df["categoria_sugerida"].value_counts(dropna=False)
    manual_review = int(df["requiere_revision"].sum())

    print(f"Total de reclamos procesados: {total}")
    print("Cantidad por categoria sugerida:")
    for category, count in counts.items():
        print(f"  - {category}: {count}")
    print(f"Cantidad enviada a revision manual: {manual_review}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Clasifica reclamos municipales usando embeddings y similitud coseno."
    )
    parser.add_argument("entrada_csv", help="Ruta del archivo CSV de entrada.")
    parser.add_argument("salida_csv", help="Ruta del archivo CSV de salida.")
    parser.add_argument(
        "--threshold",
        type=float,
        default=DEFAULT_THRESHOLD,
        help=f"Umbral minimo de similitud para aceptar una categoria. Default: {DEFAULT_THRESHOLD}",
    )
    parser.add_argument(
        "--model-name",
        default=MODEL_NAME,
        help=f"Modelo de sentence-transformers a utilizar. Default: {MODEL_NAME}",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.threshold < -1.0 or args.threshold > 1.0:
        print("El threshold debe estar en el rango [-1.0, 1.0].", file=sys.stderr)
        return 1

    try:
        df = cargar_csv(args.entrada_csv)
        model = cargar_modelo(args.model_name)
        result_df = clasificar_dataframe(df, model=model, threshold=args.threshold)
        guardar_csv(result_df, args.salida_csv)
        imprimir_resumen(result_df)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
