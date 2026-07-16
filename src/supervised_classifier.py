from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

try:
    from sentence_transformers import SentenceTransformer
except ImportError as exc:  # pragma: no cover - handled at runtime
    SentenceTransformer = None  # type: ignore[assignment]
    SENTENCE_TRANSFORMERS_IMPORT_ERROR = exc
else:
    SENTENCE_TRANSFORMERS_IMPORT_ERROR = None


MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
TEXT_COLUMN = "prestacion"
LABEL_COLUMN = "categoria"
DEFAULT_ARTIFACT_PATH = Path("artifacts/supervised_model.joblib")


@dataclass(frozen=True)
class TrainingArtifacts:
    embedding_model_name: str
    label_column: str
    text_column: str
    classes: list[str]


def normalizar_texto(texto: Any) -> str:
    """Aplica la misma normalizacion minima usada en inferencia."""
    if texto is None or pd.isna(texto):
        return ""
    return " ".join(str(texto).split()).strip()


def cargar_dataset(csv_path: str | Path) -> pd.DataFrame:
    """Carga el dataset historico y valida columnas clave."""
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"No se encontro el archivo: {csv_path}") from exc
    except pd.errors.EmptyDataError as exc:
        raise ValueError(f"El archivo CSV esta vacio: {csv_path}") from exc
    except Exception as exc:
        raise RuntimeError(f"Error al leer el CSV '{csv_path}': {exc}") from exc

    if "\ufeffnro_solicitud" in df.columns:
        df = df.rename(columns={"\ufeffnro_solicitud": "nro_solicitud"})

    missing = [column for column in (TEXT_COLUMN, LABEL_COLUMN) if column not in df.columns]
    if missing:
        raise ValueError(f"Faltan columnas obligatorias en el dataset: {missing}")

    output_df = df.copy()
    output_df[TEXT_COLUMN] = output_df[TEXT_COLUMN].apply(normalizar_texto)
    output_df[LABEL_COLUMN] = output_df[LABEL_COLUMN].apply(normalizar_texto)
    output_df = output_df[(output_df[TEXT_COLUMN] != "") & (output_df[LABEL_COLUMN] != "")]

    if output_df.empty:
        raise ValueError("No quedaron filas validas luego de limpiar textos y etiquetas vacias.")

    return output_df


def cargar_modelo_embeddings(model_name: str = MODEL_NAME) -> SentenceTransformer:
    """Carga el modelo de sentence-transformers para generar embeddings."""
    if SentenceTransformer is None:
        raise RuntimeError(
            "No se pudo importar sentence-transformers. "
            "Instala las dependencias de requirements.txt."
        ) from SENTENCE_TRANSFORMERS_IMPORT_ERROR

    try:
        return SentenceTransformer(model_name)
    except Exception as exc:  # pragma: no cover - depends on local environment
        raise RuntimeError(f"No se pudo cargar el modelo '{model_name}': {exc}") from exc


def generar_embeddings(
    texts: list[str],
    embedding_model: SentenceTransformer,
    batch_size: int = 64,
) -> Any:
    """Convierte textos en embeddings normalizados."""
    try:
        return embedding_model.encode(
            texts,
            batch_size=batch_size,
            convert_to_numpy=True,
            normalize_embeddings=True,
            show_progress_bar=False,
        )
    except Exception as exc:
        raise RuntimeError(f"No se pudieron generar embeddings: {exc}") from exc


def entrenar_clasificador(
    X_train: Any,
    y_train: list[str],
    random_state: int = 42,
) -> LogisticRegression:
    """Entrena un clasificador supervisado sobre embeddings."""
    model = LogisticRegression(
        max_iter=1000,
        class_weight="balanced",
        random_state=random_state,
    )
    model.fit(X_train, y_train)
    return model


def evaluar_modelo(
    classifier: LogisticRegression,
    X_test: Any,
    y_test: list[str],
) -> dict[str, Any]:
    """Calcula accuracy y reporte por clase."""
    predictions = classifier.predict(X_test)
    return {
        "accuracy": float(accuracy_score(y_test, predictions)),
        "report": classification_report(y_test, predictions, zero_division=0),
    }


def guardar_modelo(
    classifier: LogisticRegression,
    output_path: str | Path,
    embedding_model_name: str,
    text_column: str = TEXT_COLUMN,
    label_column: str = LABEL_COLUMN,
) -> None:
    """Serializa el clasificador entrenado y sus metadatos."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    payload = {
        "classifier": classifier,
        "artifacts": TrainingArtifacts(
            embedding_model_name=embedding_model_name,
            label_column=label_column,
            text_column=text_column,
            classes=sorted(classifier.classes_.tolist()),
        ),
    }
    joblib.dump(payload, output_path)


def cargar_modelo_supervisado(model_path: str | Path) -> dict[str, Any]:
    """Carga el clasificador serializado."""
    try:
        payload = joblib.load(model_path)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"No se encontro el modelo entrenado: {model_path}") from exc
    except Exception as exc:
        raise RuntimeError(f"No se pudo cargar el modelo entrenado '{model_path}': {exc}") from exc

    if "classifier" not in payload or "artifacts" not in payload:
        raise ValueError("El archivo de modelo no tiene la estructura esperada.")

    return payload


def entrenar_desde_dataframe(
    df: pd.DataFrame,
    embedding_model: SentenceTransformer,
    test_size: float = 0.2,
    random_state: int = 42,
) -> tuple[LogisticRegression, dict[str, Any]]:
    """Separa train/test, genera embeddings, entrena y evalua."""
    X_train_texts, X_test_texts, y_train, y_test = train_test_split(
        df[TEXT_COLUMN].tolist(),
        df[LABEL_COLUMN].tolist(),
        test_size=test_size,
        random_state=random_state,
        stratify=df[LABEL_COLUMN].tolist(),
    )

    X_train = generar_embeddings(X_train_texts, embedding_model)
    X_test = generar_embeddings(X_test_texts, embedding_model)
    classifier = entrenar_clasificador(X_train, y_train, random_state=random_state)
    metrics = evaluar_modelo(classifier, X_test, y_test)
    metrics["train_size"] = len(X_train_texts)
    metrics["test_size"] = len(X_test_texts)
    return classifier, metrics


def clasificar_dataframe_supervisado(
    df: pd.DataFrame,
    embedding_model: SentenceTransformer,
    classifier: LogisticRegression,
    text_column: str = TEXT_COLUMN,
) -> pd.DataFrame:
    """Clasifica nuevos reclamos con el modelo supervisado."""
    if text_column not in df.columns:
        raise ValueError(f"Falta la columna obligatoria '{text_column}' en el DataFrame.")

    output_df = df.copy()
    normalized_texts = output_df[text_column].apply(normalizar_texto)
    valid_mask = normalized_texts != ""
    output_df["categoria_sugerida"] = "Otros / Revision manual"
    output_df["confianza_modelo"] = 0.0
    output_df["requiere_revision"] = True

    if valid_mask.any():
        valid_texts = normalized_texts[valid_mask].tolist()
        embeddings = generar_embeddings(valid_texts, embedding_model)
        probabilities = classifier.predict_proba(embeddings)
        predictions = classifier.classes_[probabilities.argmax(axis=1)]
        scores = probabilities.max(axis=1)

        output_df.loc[valid_mask, "categoria_sugerida"] = predictions
        output_df.loc[valid_mask, "confianza_modelo"] = scores
        output_df.loc[valid_mask, "requiere_revision"] = False

    return output_df
