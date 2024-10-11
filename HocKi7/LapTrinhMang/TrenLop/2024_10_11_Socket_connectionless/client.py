import socket

if __name__ == '__main__':

    #Tạo UPD socket cho kết nối IPv4
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    data = 'hello server'
    s.sendto(data.encode('utf-8'),('127.0.0.1',9050))
    
    #Nhận dữ liệu lên tới 1024 bytes từ server
    data = s.recvfrom(1024)
    print("server gui {}", format(data))
    s.close()