import requests

# URL đăng nhập và URL khảo sát
login_url = "https://sis.utc.edu.vn"
home_url = "https://sis.utc.edu.vn/index.php"  # URL trang chủ
survey_url = "https://sis.utc.edu.vn/survey/overview.php"

# Dữ liệu đăng nhập
username = ""
password = ""

print("Enter username (email in sis.utc): ")
username = input()

data = {"username": username, "password": password}

# Tạo session
session = requests.Session()

# Đăng nhập vào trang web
response = session.post(login_url, data=data)

if response.status_code == 200:
    print("Login successful")

    # Kiểm tra cookies
    cookies = session.cookies.get_dict()
    print("Cookies after login:", cookies)

    # Truy cập trang chủ để duy trì phiên làm việc
    response = session.get(home_url)
    print("Access home page status code:", response.status_code)

    if response.status_code == 200:
        # Thực hiện yêu cầu GET từ trang khảo sát với cookies
        response = session.get(survey_url)
        print("Access survey page status code:", response.status_code)

        if response.status_code == 200:
            # Xuất nội dung thành file HTML với mã hóa UTF-8
            with open("survey_overview.html", "w", encoding="utf-8") as file:
                file.write(response.text)
            print("Survey data saved to survey_overview.html")
        else:
            print("Failed to retrieve survey data")
    else:
        print("Failed to access home page")
else:
    print("Login failed")
