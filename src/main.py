from weather_forecast import fetch_data
def main():
    print("Enter latitude: ")
    latitude = float(input())

    print("Enter longitude: ")
    longitude = float(input())

    print("Enter start date (YYYY-MM-DD): ")
    start_date = input()

    print("Enter end date (YYYY-MM-DD): ")
    end_date = input()

    print("Enter path: ")
    path = input()

    fetch_data(latitude, longitude, start_date, end_date, path)

if __name__ == "__main__":
    main()