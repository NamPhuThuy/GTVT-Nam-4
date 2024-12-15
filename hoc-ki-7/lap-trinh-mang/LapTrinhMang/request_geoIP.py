import requests


def get_geoIP(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        print("IP: ", data.get("ip"))
        print("Country: ", data.get("country"))
        print("City: ", data.get("city"))
        print("Region: ", data.get("region"))
        print("Zip code: ", data.get("postal"))
        print("Location: ", data.get("loc"))
    except requests.RequestException as e:
        print(e)


if __name__ == "__main__":
    url = "https://ipinfo.io/1.55.183.28/json"
    get_geoIP(url)
