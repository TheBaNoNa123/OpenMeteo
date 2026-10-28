from pathlib import Path
import csv
import os

def append_csv(path, lat, long, dates, temperature, time, time_zone):
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Latitude", "Longitude",
                                                  "Time_Zone", "Date", "Time", "Temperature"])
        if os.path.getsize(file_path) == 0:
            writer.writeheader()
        writer.writerows([{"Latitude": lat, "Longitude": long, "Time_Zone": time_zone, "Date" : dates, "Time": time, "Temperature": temperature}])

