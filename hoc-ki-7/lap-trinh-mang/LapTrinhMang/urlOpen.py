from urllib.request import urlopen

r = urlopen("https://www.utc.edu.vn")
print(r.url)
print(r.status)
c = r.read()
print(c)

# ghi chuỗi c vào file output.txt
f = open("output.txt", "w")

f.write(str(c))
