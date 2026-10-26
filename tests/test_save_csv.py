import pytest
import csv
from utils.save_csv import append_csv


def test_append_csv(tmp_path):
    path = tmp_path / "example.csv"
    append_csv(path)



