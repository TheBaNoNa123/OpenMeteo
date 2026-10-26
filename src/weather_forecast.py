import requests



url  = "https://api.open-meteo.com/v1/forecast"

print("Enter latitude: ")
latitude = float(input())

print("Enter longitude: ")
longitude = float(input())

print("Enter start date (YYYY-MM-DD): ")
start_date = input()

print("Enter end date (YYYY-MM-DD): ")
end_date = input()
def fetch_data(lat, long, start, end):
    try:
        data = requests.get(url, params={"latitude": lat, "longitude": long,
                                        "hourly": "temperature_2m", "start_date": start,
                                        "end_date": end, "timezone": "Asia/Tokyo" })
        data.raise_for_status()
        response = data.json()
        temperature = response["hourly"]["temperature_2m"]
        for i in temperature:
            print(i)
    except requests.exceptions.RequestException as e:
            print(e)

fetch_data(latitude, longitude, start_date, end_date)
