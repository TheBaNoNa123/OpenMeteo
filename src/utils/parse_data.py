import time
from datetime import datetime, date, timedelta

def parse_dates(start_date, end_date):
    start = date.fromisoformat(start_date)
    end = date.fromisoformat(end_date)
    dates = []

    for i in range((end - start).days + 1):
        dates.append((start + timedelta(days=i)).isoformat())
    return dates


parse_dates("2026-10-20", "2026-10-25")
