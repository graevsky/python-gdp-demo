from econ_report.io import DataRow
from econ_report.reports import average_gdp


def test_average_dgp():
    rows = [
        DataRow(country="A", year=2025, gdp=10.0),
        DataRow(country="A", year=2026, gdp=20.0),
        DataRow(country="B", year=2025, gdp=200.0),
        DataRow(country="B", year=2026, gdp=0.0),
        DataRow(country="C", year=2025, gdp=300.0),
        DataRow(country="C", year=2026, gdp=660.0),
        DataRow(country="D", year=2025, gdp=400.0),
        DataRow(country="D", year=2026, gdp=400.0),
        DataRow(country="E", year=2000, gdp=10.0),
    ]

    report = average_gdp(rows)

    assert len(report) == 5

    assert report[0].country == "C"
    assert report[0].avg_gdp == 480.0

    assert report[1].country == "D"
    assert report[1].avg_gdp == 400.0

    assert report[2].country == "B"
    assert report[2].avg_gdp == 100.0

    assert report[3].country == "A"
    assert report[3].avg_gdp == 15.0

    assert report[4].country == "E"
    assert report[4].avg_gdp == 10.0
