import pytest
from src.utils.parse_data import parse_dates

@pytest.mark.parametrize(
    "start_date, end_date, expected_date",
    [
        ("2020-10-10", "2020-10-12", ["2020-10-10", "2020-10-11", "2020-10-12"]),
        ("2020-10-21", "2020-10-23", ["2020-10-21", "2020-10-22", "2020-10-23"]),
        ("2020-10-24", "2020-10-24", ["2020-10-24"]),
        ("2020-10-30", "2020-11-01", ["2020-10-30", "2020-10-31", "2020-11-01"]),
    ]
)
def test_parse_dates(start_date, end_date, expected_date):
    assert expected_date == parse_dates(start_date, end_date)