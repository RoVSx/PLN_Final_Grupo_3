from __future__ import annotations

import argparse
import sys

from src.supervised_classifier import (
    DEFAULT_ARTIFACT_PATH,
    MODEL_NAME,
    cargar_dataset,
    cargar_modelo_embeddings,
    entrenar_desde_dataframe,
    guardar_modelo,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Entrena un clasificador supervisado de reclamos municipales usando embeddings."
    )
    parser.add_argument(
        "dataset_csv",
        nargs="?",
        default="atencion_ciudadana_lima_2023.csv",
        help="Ruta del CSV historico con columnas prestacion y categoria.",
    )
    parser.add_argument(
        "--output-model",
        default=str(DEFAULT_ARTIFACT_PATH),
        help=f"Ruta donde se guardara el modelo entrenado. Default: {DEFAULT_ARTIFACT_PATH}",
    )
    parser.add_argument(
        "--test-size",
        type=float,
        default=0.2,
        help="Proporcion de datos reservada para evaluacion. Default: 0.2",
    )
    parser.add_argument(
        "--model-name",
        default=MODEL_NAME,
        help=f"Modelo de embeddings a utilizar. Default: {MODEL_NAME}",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if not 0.0 < args.test_size < 1.0:
        print("El parametro --test-size debe estar en el rango (0, 1).", file=sys.stderr)
        return 1

    try:
        df = cargar_dataset(args.dataset_csv)
        embedding_model = cargar_modelo_embeddings(args.model_name)
        classifier, metrics = entrenar_desde_dataframe(
            df=df,
            embedding_model=embedding_model,
            test_size=args.test_size,
            random_state=42,
        )
        guardar_modelo(
            classifier=classifier,
            output_path=args.output_model,
            embedding_model_name=args.model_name,
        )
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print("Entrenamiento supervisado completado")
    print(f"Dataset total: {len(df)}")
    print(f"Train: {metrics['train_size']}")
    print(f"Test: {metrics['test_size']}")
    print(f"Accuracy: {metrics['accuracy']:.4f}")
    print("Reporte por clase:")
    print(metrics["report"])
    print(f"Modelo guardado en: {args.output_model}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
