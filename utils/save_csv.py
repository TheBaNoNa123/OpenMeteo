from pathlib import Path
import csv

def append_csv(path):
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Latitude", "Longitude", "Start_Date", "End_Date",
                                         "Time_Zone", "Date", "Time", "Temperature"])
        writer.writeheader()
        writer.writerows([{"Latitude": 1, "Longitude": 2, "Start_Date": 3, "End_Date": 4, "Time": 5, "Temperature": 6}])

append_csv("groot/bob.csv")
