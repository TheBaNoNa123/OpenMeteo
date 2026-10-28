from datetime import datetime, timedelta
import requests
import logging
from utils.parse_data import parse_dates
from utils.save_csv import append_csv

logging.basicConfig(
    filename="../logs/weather_forecast.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program started")

url = "https://api.open-meteo.com/v1/forecast"

def fetch_data(lat, long, start, end, path):
    try:
        data = requests.get(url, params={"latitude": lat, "longitude": long,
                                        "hourly": "temperature_2m", "start_date": start,
                                        "end_date": end, "timezone": "auto" })
        data.raise_for_status()
        response = data.json()
        temperature = response["hourly"]["temperature_2m"]
        dates = parse_dates(start, end)

        count = 0
        date = 0
        base_time = datetime.strptime("00:00", "%H:%M")

        while count <= 24:
            if date > len(dates) - 1:
                break
            for i in temperature:
                current_time = base_time.strftime("%H:%M")
                append_csv(path, lat, long, dates[date], i, current_time, response["timezone"])
                base_time += timedelta(hours=1)
                count += 1

                if count == 24:
                    count = 0
                    date += 1
                    base_time -= timedelta(hours=24)

    except requests.exceptions.HTTPError as e:
        logging.error(e)
    except requests.exceptions.RequestException as e:
        logging.error(e)


logging.info("Program finished\n")

