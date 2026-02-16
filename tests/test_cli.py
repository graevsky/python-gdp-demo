from pathlib import Path

import pytest

from econ_report.cli import main


def test_cli_prints_table_for_average_gdp(tmp_path: Path, capsys: pytest.CaptureFixture[str]):
    p = tmp_path / "economic.csv"
    p.write_text(
        "country,year,gdp,gdp_growth,inflation,unemployment,population,continent\n"
        "X,2021,10,0,0,0,0,NA\n"
        "X,2022,30,0,0,0,0,NA\n"
        "Y,2022,100,0,0,0,0,NA\n",
        encoding="utf-8",
    )

    code = main(["--files", str(p), "--report", "average-gdp"])
    assert code == 0

    out = capsys.readouterr().out
    assert "country" in out
    assert "avg_gdp" in out
    assert "| Y" in out
    assert "| X" in out


def test_cli_errors_on_unknown_report(capsys: pytest.CaptureFixture[str]):
    with pytest.raises(SystemExit) as e:
        main(["--files", "whatever.csv", "--report", "unknown"])
    assert e.value.code == 2


def test_cli_errors_on_missing_file(tmp_path: Path):
    missing = tmp_path / "nope.csv"
    with pytest.raises(SystemExit) as e:
        main(["--files", str(missing), "--report", "average-gdp"])
    assert e.value.code == 2
