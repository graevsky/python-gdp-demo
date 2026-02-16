from __future__ import annotations

from dataclasses import dataclass
from statistics import mean
from typing import Iterable

from .io import DataRow


@dataclass(frozen=True, slots=True)
class ReportRow:
    country: str
    avg_gdp: float


def average_gdp(rows: Iterable[DataRow]) -> list[ReportRow]:
    acc: dict[str, list[float]] = {}

    for row in rows:
        acc.setdefault(row.country, []).append(row.gdp)

    report = [ReportRow(country=c, avg_gdp=mean(gdps)) for c, gdps in acc.items()]
    report.sort(key=lambda x: x.avg_gdp, reverse=True)
    return report


REPORTS = {
    "average-gdp": average_gdp,
}
