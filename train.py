from __future__ import annotations

from pathlib import Path

from src.classifier import TextComplaintClassifier
from src.data_utils import load_jsonl, train_test_split


DATA_PATH = Path("data/train_data.jsonl")
MODEL_PATH = Path("artifacts/model.json")


def main() -> None:
    rows = load_jsonl(DATA_PATH)
    train_rows, test_rows = train_test_split(rows, test_ratio=0.25, seed=42)

    classifier = TextComplaintClassifier()
    classifier.fit(
        texts=[row["text"] for row in train_rows],
        labels=[row["label"] for row in train_rows],
    )

    metrics = classifier.evaluate(
        texts=[row["text"] for row in test_rows],
        labels=[row["label"] for row in test_rows],
    )
    classifier.save(MODEL_PATH)

    print("Entrenamiento completado")
    print(f"Ejemplos train: {len(train_rows)}")
    print(f"Ejemplos test: {len(test_rows)}")
    print(f"Accuracy: {metrics['accuracy']:.2%}")
    print(f"Modelo guardado en: {MODEL_PATH}")


if __name__ == "__main__":
    main()
