from urllib.request import Request
from urllib.request import urlopen
import gzip

req = Request("https://www.utc.edu.vn")

#req.add_header("Accept-Language", "en")
req.add_header("Accept-Encoding", "gzip")

response = urlopen(req)
#response = response.read()

data = gzip.decompress(response.read())

res = data

f = open("output.txt", "w")
f.write(str(res))