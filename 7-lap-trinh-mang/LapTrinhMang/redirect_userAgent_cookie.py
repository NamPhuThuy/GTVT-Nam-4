
from urllib.request import Request, urlopen, build_opener, HTTPCookieProcessor
from http.cookiejar import CookieJar
import datetime

# # gửi yêu cầu redirect

# r = Request("https://gmail.com")
# r1 = urlopen(r)
# #print(r.url)
# print(r.redirect_dict)

####################################################################################################

# # gửi yêu cầu với User-Agent

# r = Request("https://www.python.org")
# r1 = urlopen(r)
# print(r.get_header('User-Agent'))

####################################################################################################

# # gửi yêu cầu với cookie

cj = CookieJar()
opener = build_opener(HTTPCookieProcessor(cj))

r = opener.open("https://www.github.com")
print(r)
print(len(cj))

cookies = list(cj)
for cookie in cookies:
    # đánh dấu số thứ tự của cookie
    print(f"Cookie {cookies.index(cookie) + 1}")
    print(cookie.name)
    print(cookie.value)
    print(cookie.domain)
    print(cookie.path)
    print(cookie.expires)
    print(cookie.secure)
    if cookie.expires is not None:
        print(datetime.datetime.fromtimestamp(cookie.expires))
    else:
        print("No expiration date")

####################################################################################################
