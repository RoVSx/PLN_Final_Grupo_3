from __future__ import annotations

import json
import random
from collections import defaultdict
from pathlib import Path


def load_jsonl(path: str | Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    with Path(path).open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def train_test_split(rows: list[dict[str, str]], test_ratio: float = 0.25, seed: int = 42) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    if not 0 < test_ratio < 1:
        raise ValueError("test_ratio debe estar entre 0 y 1")

    grouped_rows: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped_rows[row["label"]].append(row)

    train_rows: list[dict[str, str]] = []
    test_rows: list[dict[str, str]] = []
    rng = random.Random(seed)

    for label_rows in grouped_rows.values():
        shuffled = label_rows[:]
        rng.shuffle(shuffled)
        split_idx = max(1, int(len(shuffled) * (1 - test_ratio)))
        if split_idx == len(shuffled):
            split_idx = len(shuffled) - 1

        train_rows.extend(shuffled[:split_idx])
        test_rows.extend(shuffled[split_idx:])

    rng.shuffle(train_rows)
    rng.shuffle(test_rows)
    return train_rows, test_rows
