import requests
# from bs4 import BeautifulSoup
import re

url = "https://utc.edu.vn/#footer"


def find_email(url):
    response = requests.get(url)
    response.raise_for_status()

    try:
        # Lấy thông tin email có trên web
        data = response.text
        emails = re.findall(
            r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", data)

    # lọc email trùng
        emails = list(set(emails))
        return emails

    except requests.RequestException as e:
        print(e)
        return set()


if __name__ == "__main__":
    emails = find_email(url)
    print(emails)
    with open("output.txt", "w") as file:
        for i in emails:
            file.write(f"{i}\n")
