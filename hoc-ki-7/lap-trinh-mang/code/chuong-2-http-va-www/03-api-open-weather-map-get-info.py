import requests


def get_weather_info(city_name, api_key, units="metric"):
    # URL của API với các tham số
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units={units}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        for d in data:
            print(d, data[d])
        print("-----------------")

        # Lấy thông tin thời tiết cần thiết
        main = data["main"]

        # for m in main:
        #     print(m, main[m])
        # print('-----------------')

        weather = data["weather"]
        for w in weather:
            print(w)  # In ra toàn bộ từ điển thời tiết
            for key, value in w.items():
                print(f"{key}: {value}")
        print("-----------------")

        location = data["coord"]

        # Hiển thị thông tin thời tiết
        # print(f"City: {city_name}")
        # print(f"Coordinates: {location['lat']}, {location['lon']}")
        # print(f"Temperature: {main['temp']}°C")  # alt + 0176: ký tự °
        # print(f"Weather: {weather['description']}")
    else:
        print(
            f"Failed to get weather data for {city_name}. Error code: {response.status_code}"
        )


if __name__ == "__main__":
    api_key = "c244f22c4cd4ee98867fe4830bca0176"
    city_name = "Hanoi"
    # city_name = input("Enter city name: ")
    get_weather_info(city_name, api_key)
