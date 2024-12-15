import ftplib

def share_directory_ftp(hostname, port, username, password, directory, permissions):
    print("---------- Function share_directory_ftp ----------")
    try:
        # Kết nối tới server FTP
        ftp = ftplib.FTP()
        ftp.connect(hostname, port)
        ftp.login(username, password)
        
        # Thử lệnh SITE CHMOD
        response = ftp.sendcmd(f'SITE CHMOD {permissions} {directory}')
        print(f"Shared directory: {directory} with permissions: {permissions}")
        print(f"Server response: {response}")
        
        # Đóng kết nối FTP
        ftp.quit()
    except ftplib.all_errors as e:
        print(f"Error sharing directory via FTP: {e}")

# Ví dụ sử dụng
hostname = "127.0.0.1"
port = 21  # Sử dụng cổng 21 cho FTP
username = "User01"
password = "123"
directory = "/test01"
permissions = "755"

share_directory_ftp(hostname, port, username, password, directory, permissions)