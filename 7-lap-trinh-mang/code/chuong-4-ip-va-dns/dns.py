import socket

def get_host_name_ip():
    try:
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        print("Hostname:", host_name)
        print("IP Address:", ip_address)
    except:
        print("Unable to get Hostname and IP")

# Gọi hàm để thực thi
get_host_name_ip()