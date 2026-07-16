from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

from src.supervised_classifier import (
    DEFAULT_ARTIFACT_PATH,
    cargar_modelo_embeddings,
    cargar_modelo_supervisado,
    clasificar_dataframe_supervisado,
)


def cargar_csv(input_path: str | Path) -> pd.DataFrame:
    try:
        df = pd.read_csv(input_path)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"No se encontro el archivo de entrada: {input_path}") from exc
    except pd.errors.EmptyDataError as exc:
        raise ValueError(f"El archivo CSV esta vacio: {input_path}") from exc
    except Exception as exc:
        raise RuntimeError(f"Error al leer el CSV '{input_path}': {exc}") from exc

    if "\ufeffnro_solicitud" in df.columns:
        df = df.rename(columns={"\ufeffnro_solicitud": "nro_solicitud"})

    return df


def guardar_csv(df: pd.DataFrame, output_path: str | Path) -> None:
    output_path = Path(output_path)
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path, index=False, encoding="utf-8")
    except Exception as exc:
        raise RuntimeError(f"Error al escribir el CSV '{output_path}': {exc}") from exc


def imprimir_resumen(df: pd.DataFrame) -> None:
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
        description="Clasifica reclamos con un modelo supervisado entrenado sobre embeddings."
    )
    parser.add_argument("entrada_csv", help="Ruta del archivo CSV de entrada.")
    parser.add_argument("salida_csv", help="Ruta del archivo CSV de salida.")
    parser.add_argument(
        "--model-path",
        default=str(DEFAULT_ARTIFACT_PATH),
        help=f"Ruta del modelo entrenado. Default: {DEFAULT_ARTIFACT_PATH}",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        payload = cargar_modelo_supervisado(args.model_path)
        artifacts = payload["artifacts"]
        classifier = payload["classifier"]
        df = cargar_csv(args.entrada_csv)
        embedding_model = cargar_modelo_embeddings(artifacts.embedding_model_name)
        result_df = clasificar_dataframe_supervisado(
            df=df,
            embedding_model=embedding_model,
            classifier=classifier,
            text_column=artifacts.text_column,
        )
        guardar_csv(result_df, args.salida_csv)
        imprimir_resumen(result_df)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
