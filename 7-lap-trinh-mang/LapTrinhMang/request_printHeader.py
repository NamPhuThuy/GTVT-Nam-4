import requests
import json


def get_geoIP(url):
    try:
        response = requests.get(url)
        print("Status code: ", response.status_code)
        print("Header: ", response.headers)

        if response.status_code == 200:
            data = response.json()

            for d in data:
                print(d, ":", data[d])

            print("Header respone: ")
            for header, value in response.headers.items():
                print(header, "-->", value)

            print("Header request: ")
            for header, value in response.request.headers.items():
                print(header, "-->", value)
            print("Server:" + response.headers["Server"])
        else:
            print("Error: ", response.status_code)

    except requests.RequestException as e:
        print(e)


if __name__ == "__main__":
    url = "http://httpbin.org/get"
    get_geoIP(url)
