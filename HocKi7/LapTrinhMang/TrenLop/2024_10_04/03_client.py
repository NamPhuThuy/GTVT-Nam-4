import socket

if __name__ == '__main__':
    
    #Thiết lập TCP socket cho kết nối IPv4
    s= socket.socket( socket.AF_INET ,socket.SOCK_STREAM ,0)
    
    #Kết nối với máy local qua port 9050
    s.connect(('127.0.0.1',9050))
    
    while True:
        #Nhận tới 4096 bytes dữ liệu từ server và lưu trong biến 'data
        data = s.recv(4096)

        print("receive from server: {}", format(data.decode('utf-8')))
        
        

        if(data.decode('utf-8')== 'bye'):
            break

        data= input("input text: ")
        s.send(data.encode('utf-8'))

    s.close()