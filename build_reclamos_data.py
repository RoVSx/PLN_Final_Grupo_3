from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

INPUT_CSV = Path("artifacts/clasificado_output.csv")
OUTPUT_JS = Path("src/mockData.js")

VERBO_POR = {"Reclamo", "Denuncia"}


def construir_texto(row: pd.Series) -> str:
    tipo = row["tipo"]
    verbo = "por" if tipo in VERBO_POR else "de"
    partes = [f'{tipo} {verbo} "{row["prestacion"]}", {row["distrito"]}']

    if pd.notna(row["urbanizacion"]):
        partes[0] += f', urb. {row["urbanizacion"]}'

    ubicacion = []
    if pd.notna(row["via"]):
        via = str(row["via"])
        if pd.notna(row["numero"]):
            via += f' {row["numero"]}'
        ubicacion.append(via)
    if pd.notna(row["referencia"]):
        ubicacion.append(str(row["referencia"]))

    texto = partes[0]
    if ubicacion:
        texto += " — " + ", ".join(ubicacion)
    texto += "."
    return texto


CRITICAL_COLUMNS = [
    "nro_solicitud",
    "categoria_sugerida",
    "tipo",
    "distrito",
    "fecha_ingreso",
    "prestacion",
]


def main() -> None:
    df = pd.read_csv(INPUT_CSV)

    before = len(df)
    df = df.dropna(subset=CRITICAL_COLUMNS)
    dropped = before - len(df)
    if dropped:
        print(f"Descartados {dropped} registros con campos nulos en {CRITICAL_COLUMNS}")

    records = []
    for _, row in df.iterrows():
        records.append(
            {
                "id": row["nro_solicitud"],
                "categoria": row["categoria_sugerida"],
                "tipo": row["tipo"],
                "distrito": row["distrito"],
                "fecha": row["fecha_ingreso"],
                "texto": construir_texto(row),
            }
        )

    js_array = json.dumps(records, ensure_ascii=False, indent=2)
    content = f"const RECLAMOS_DATA = {js_array};\n"
    OUTPUT_JS.write_text(content, encoding="utf-8")
    print(f"Escritos {len(records)} registros en {OUTPUT_JS}")


if __name__ == "__main__":
    main()
