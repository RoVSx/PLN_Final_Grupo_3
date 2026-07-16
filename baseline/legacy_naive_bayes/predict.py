from __future__ import annotations

import argparse

from baseline.legacy_naive_bayes.classifier import TextComplaintClassifier


def main() -> None:
    parser = argparse.ArgumentParser(description="Clasifica reclamos municipales a partir de texto libre")
    parser.add_argument("text", help="Texto del reclamo ciudadano")
    parser.add_argument("--model", default="artifacts/model.json", help="Ruta del modelo entrenado")
    args = parser.parse_args()

    classifier = TextComplaintClassifier.load(args.model)
    prediction = classifier.predict(args.text)

    print(f"Categoria: {prediction.label}")
    print(f"Confianza: {prediction.confidence:.2%}")
    print("Scores:")
    for label, score in sorted(prediction.scores.items(), key=lambda item: item[1], reverse=True):
        print(f"  - {label}: {score:.2%}")


if __name__ == "__main__":
    main()
