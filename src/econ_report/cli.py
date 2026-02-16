from __future__ import annotations

import argparse
from typing import Sequence

from tabulate import tabulate

from .io import read_data_rows
from .reports import REPORTS


def arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="economic-report",
        description="Build GDP report from CSV data",
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Paths to CSV files (multiple files allowed).",
    )
    parser.add_argument(
        "--report",
        required=True,
        help="Report name. Supported: " + ", ".join(sorted(REPORTS.keys())),
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = arg_parser()
    args = parser.parse_args(argv)

    report_name: str = args.report
  
    if report_name not in REPORTS:
        parser.error(
            f"Unsupported report: {report_name}. "
            f"Supported: {', '.join(sorted(REPORTS.keys()))}"
        )

    try:
        rows = read_data_rows(args.files)
    except FileNotFoundError as e:
        parser.error(str(e))

    report_fun = REPORTS[report_name]
    report_rows = report_fun(rows)

    table = [[r.country, round(r.avg_gdp, 2)] for r in report_rows]
    print(tabulate(table, headers=["country", "avg_gdp"], tablefmt="github"))

    return 0
