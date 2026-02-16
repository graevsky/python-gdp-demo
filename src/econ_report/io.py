from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True, slots=True)
class DataRow:
    country: str
    year: int
    gdp: float


def read_data_rows(files: Iterable[str]) -> list[DataRow]:
    rows: list[DataRow] = []

    for fp in files:
        path = Path(fp)
        if not path.exists() or not path.is_file():
            raise FileNotFoundError(f"File not found: {fp}")

        with path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for r in reader:
                rows.append(
                    DataRow(
                        country=r["country"].strip(),
                        year=int(r["year"]),
                        gdp=float(r["gdp"]),
                    )
                )

    return rows
