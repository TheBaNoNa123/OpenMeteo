import csv
from src.utils.save_csv import append_csv

def test_append_csv_writes_header_and_row(tmp_path):

    path = tmp_path / "example.csv"
    append_csv(path, 36, 138, "2026-10-29", 14.3,
               "12:00", "Asia/Tokyo")
    with open(path, newline="") as file:
        rows = list(csv.DictReader(file))

        assert(len(rows) == 1)
        assert rows[0] == {
            "Latitude": "36",
            "Longitude": "138",
            "Time_Zone": "Asia/Tokyo",
            "Date": "2026-10-29",
            "Temperature": "14.3",
            "Time": "12:00"
        }



def test_append_csv_does_not_duplicate_header(tmp_path):
    path = tmp_path / "example.csv"
    append_csv(path, 36, 138, "2026-10-29", 14.3,
               "12:00", "Asia/Tokyo")
    append_csv(path, 36, 138, "2026-10-29", 14.3,
               "12:00", "Asia/Tokyo")

    with open(path, newline="") as file:
        rows = list(csv.DictReader(file))

        assert len(rows) == 2



