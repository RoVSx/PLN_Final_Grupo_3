from __future__ import annotations

import json
import math
import re
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


TOKEN_PATTERN = re.compile(r"[a-z0-9]+", re.IGNORECASE)
LABEL_KEYWORDS = {
    "limpieza_publica": {"basura", "residuos", "desmonte", "escombros", "barrido", "contenedores", "camion", "olores"},
    "alumbrado": {"luminaria", "poste", "farola", "lampara", "iluminacion", "oscura", "alumbrado"},
    "transito": {"semaforo", "congestion", "vehicular", "ciclovia", "senalizacion", "estacionan", "trafico", "rompemuelles"},
    "areas_verdes": {"poda", "arboles", "grass", "jardines", "plantas", "palmera", "riego", "arbustos"},
    "ruido": {"musica", "ruido", "bulla", "parlantes", "bocinas", "vibraciones", "madrugada"},
    "seguridad": {"robos", "patrullaje", "serenazgo", "sospechosas", "pelea", "inseguridad", "vigilancia", "amenaza"},
    "otros": {"horario", "requisitos", "tramite", "arbitrios", "documento", "orientacion", "consulta", "licencia"},
}


def normalize_text(text: str) -> str:
    normalized = unicodedata.normalize("NFD", text.lower())
    normalized = "".join(char for char in normalized if unicodedata.category(char) != "Mn")
    return normalized


def tokenize(text: str) -> list[str]:
    text = normalize_text(text)
    unigrams = TOKEN_PATTERN.findall(text)
    bigrams = [f"{unigrams[idx]}_{unigrams[idx + 1]}" for idx in range(len(unigrams) - 1)]
    return unigrams + bigrams


@dataclass
class Prediction:
    label: str
    confidence: float
    scores: dict[str, float]


class TextComplaintClassifier:
    def __init__(self) -> None:
        self.labels: list[str] = []
        self.vocabulary: set[str] = set()
        self.label_doc_counts: Counter[str] = Counter()
        self.label_token_counts: dict[str, Counter[str]] = defaultdict(Counter)
        self.total_tokens_by_label: Counter[str] = Counter()
        self.total_docs = 0

    def fit(self, texts: list[str], labels: list[str]) -> None:
        if len(texts) != len(labels):
            raise ValueError("texts y labels deben tener la misma longitud")
        if not texts:
            raise ValueError("Se requiere al menos un ejemplo para entrenar")

        for text, label in zip(texts, labels):
            tokens = tokenize(text)
            self.labels.append(label) if label not in self.labels else None
            self.label_doc_counts[label] += 1
            self.total_docs += 1
            for token in tokens:
                self.vocabulary.add(token)
                self.label_token_counts[label][token] += 1
                self.total_tokens_by_label[label] += 1

        self.labels = sorted(set(self.labels))

    def predict(self, text: str) -> Prediction:
        if not self.labels:
            raise ValueError("El modelo no ha sido entrenado")

        tokens = tokenize(text)
        if not tokens:
            fallback_scores = {label: 1 / len(self.labels) for label in self.labels}
            return Prediction(label=self.labels[0], confidence=fallback_scores[self.labels[0]], scores=fallback_scores)

        log_scores: dict[str, float] = {}
        vocab_size = max(len(self.vocabulary), 1)

        for label in self.labels:
            prior = math.log(self.label_doc_counts[label] / self.total_docs)
            log_score = prior
            total_tokens = self.total_tokens_by_label[label]

            for token in tokens:
                token_count = self.label_token_counts[label][token]
                likelihood = (token_count + 1) / (total_tokens + vocab_size)
                log_score += math.log(likelihood)

            keyword_matches = sum(1 for token in tokens if token in LABEL_KEYWORDS.get(label, set()))
            log_score += keyword_matches * 1.25

            log_scores[label] = log_score

        probabilities = self._softmax(log_scores)
        best_label = max(probabilities, key=probabilities.get)
        return Prediction(label=best_label, confidence=probabilities[best_label], scores=probabilities)

    def evaluate(self, texts: list[str], labels: list[str]) -> dict[str, float]:
        correct = 0
        for text, expected in zip(texts, labels):
            predicted = self.predict(text).label
            if predicted == expected:
                correct += 1
        accuracy = correct / len(labels) if labels else 0.0
        return {"accuracy": accuracy}

    def save(self, output_path: str | Path) -> None:
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "labels": self.labels,
            "vocabulary": sorted(self.vocabulary),
            "label_doc_counts": dict(self.label_doc_counts),
            "label_token_counts": {label: dict(counter) for label, counter in self.label_token_counts.items()},
            "total_tokens_by_label": dict(self.total_tokens_by_label),
            "total_docs": self.total_docs,
        }
        path.write_text(json.dumps(payload, ensure_ascii=True, indent=2), encoding="utf-8")

    @classmethod
    def load(cls, input_path: str | Path) -> "TextComplaintClassifier":
        payload = json.loads(Path(input_path).read_text(encoding="utf-8"))
        model = cls()
        model.labels = payload["labels"]
        model.vocabulary = set(payload["vocabulary"])
        model.label_doc_counts = Counter(payload["label_doc_counts"])
        model.label_token_counts = defaultdict(Counter, {label: Counter(tokens) for label, tokens in payload["label_token_counts"].items()})
        model.total_tokens_by_label = Counter(payload["total_tokens_by_label"])
        model.total_docs = payload["total_docs"]
        return model

    @staticmethod
    def _softmax(log_scores: dict[str, float]) -> dict[str, float]:
        max_log = max(log_scores.values())
        exp_scores = {label: math.exp(score - max_log) for label, score in log_scores.items()}
        total = sum(exp_scores.values())
        return {label: score / total for label, score in exp_scores.items()}
