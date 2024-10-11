import socket

if __name__ == '__main__':
    #Tạo UPD socket cho kết nối IPv4
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    #Liên kết socket với địa chỉ IP của máy cục bộ ('127.0.0.1') và port 9050
    s.bind(('127.0.0.1', 9050))
    
    '''
    Cho phép nhận tới 1024 bytes dữ liệu từ client
    - data: chứa dữ liệu nhận được
    - addr: chứa địa chỉ của máy client
    '''
    data, addr = s.recvfrom(1024)
    
    
    print('client gui {}', format(data))
    
    #Dữ liệu gửi tới client
    data = 'Hello client'
    
    #Thực hiện gửi tới client
    s.sendto(data.encode('utf-8'), addr)
    s.close()