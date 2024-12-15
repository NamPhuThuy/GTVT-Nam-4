import ftplib
import os

# Hàm liệt kê thư mục
def list_directory(ftp):
    print("---------- Function list_directory ----------")
    try:
        files = []
        ftp.dir(files.append)
        return files
    except ftplib.all_errors as e:
        print(f"Error listing directory: {e}")
        return []


# Hàm thay đổi thư mục
def change_directory(ftp, directory):
    print("---------- Function change_directory ----------")
    try:
        ftp.cwd(directory)
        print(f"Changed to directory: {directory}")
    except ftplib.all_errors as e:
        print(f"Error changing directory: {e}")


# Hàm tạo thư mục
def create_directory(ftp, directory):
    print("---------- Function create_directory ----------")
    try:
        ftp.mkd(directory)
        print(f"Created directory: {directory}")
    except ftplib.all_errors as e:
        print(f"Error creating directory: {e}")


# Hàm xóa tệp
def delete_file(ftp, filename):
    print("---------- Function delete_file ----------")
    try:
        ftp.delete(filename)
        print(f"Deleted file: {filename}")
    except ftplib.all_errors as e:
        print(f"Error deleting file: {e}")


# Hàm xóa thư mục
def delete_directory(ftp, directory):
    print("---------- Function delete_directory ----------")
    try:
        ftp.rmd(directory)
        print(f"Deleted directory: {directory}")
    except ftplib.all_errors as e:
        print(f"Error deleting directory: {e}")


# Hàm đổi tên tệp hoặc thư mục
def rename_file_or_directory(ftp, from_name, to_name):
    print("---------- Function rename_file_or_directory ----------")
    try:
        ftp.rename(from_name, to_name)
        print(f"Renamed {from_name} to {to_name}")
    except ftplib.all_errors as e:
        print(f"Error renaming {from_name} to {to_name}: {e}")


# Hàm lấy kích thước tệp
def get_file_size(ftp, filename):
    print("---------- Function get_file_size ----------")
    try:
        size = ftp.size(filename)
        print(f"Size of {filename}: {size} bytes")
        return size
    except ftplib.all_errors as e:
        print(f"Error getting file size: {e}")
        return None


# Hàm tải tệp xuống
def download_file(ftp, file_orig, file_copy):
    print("---------- Function download_file ----------")
    try:
        with open(file_copy, "wb") as fp:
            ftp.retrbinary("RETR " + file_orig, fp.write)
        print(f"Download of {file_orig} to {file_copy} completed successfully.")
    except ftplib.all_errors as e:
        print(f"FTP error: {e}")
        if os.path.isfile(file_copy):
            os.remove(file_copy)


# Hàm tải tệp lên
def upload_file(ftp, filename):
    print("---------- Function upload_file ----------")
    try:
        with open(filename, "rb") as fp:
            res = ftp.storbinary("STOR " + filename, fp)
            print(f"Server response: {res}")
            if not res.startswith("226"):
                print("Upload failed")
            else:
                print(f"Upload of {filename} completed successfully.")
    except ftplib.all_errors as e:
        print(f"FTP error: {e}")


# Hàm gửi lệnh tùy chỉnh
def send_command(ftp, command):
    print("---------- Function send_command ----------")
    try:
        response = ftp.sendcmd(command)
        return response
    except ftplib.all_errors as e:
        print(f"Error sending command: {e}")
        return None


# Hàm in menu
def print_menu():
    print("\nMenu:")
    print("1. List directory")
    print("2. Change directory")
    print("3. Create directory")
    print("4. Delete file")
    print("5. Delete directory")
    print("6. Rename file or directory")
    print("7. Get file size")
    print("8. Download file")
    print("9. Upload file")
    print("10. Send custom command")
    print("11. Exit")


# Chương trình chính
if __name__ == "__main__":
    with ftplib.FTP("34.124.137.135") as ftp:
        try:
            ftp.login("test", "LapTrinhMang@2024")
            ftp.set_pasv(True)

            print(ftp.getwelcome())

            while True:
                print_menu()
                choice = input("Enter your choice: ")

                # Xử lý lựa chọn của người dùng
                if choice == "1":
                    entries = list_directory(ftp)
                    print(len(entries), "entries:")
                    for entry in entries:
                        print(entry)
                elif choice == "2":
                    directory = input("Enter directory to change to: ")
                    change_directory(ftp, directory)
                elif choice == "3":
                    directory = input("Enter directory name to create: ")
                    create_directory(ftp, directory)
                elif choice == "4":
                    filename = input("Enter filename to delete: ")
                    delete_file(ftp, filename)
                elif choice == "5":
                    directory = input("Enter directory name to delete: ")
                    delete_directory(ftp, directory)
                elif choice == "6":
                    from_name = input("Enter current name: ")
                    to_name = input("Enter new name: ")
                    rename_file_or_directory(ftp, from_name, to_name)
                elif choice == "7":
                    filename = input("Enter filename to get size: ")
                    get_file_size(ftp, filename)
                elif choice == "8":
                    file_orig = input("Enter remote filename to download: ")
                    file_copy = input("Enter local path and filename to save as: ")
                    download_file(ftp, file_orig, file_copy)
                elif choice == "9":
                    filename = input("Enter local filename to upload: ")
                    upload_file(ftp, filename)
                elif choice == "10":
                    command = input("Enter custom FTP command: ")
                    response = send_command(ftp, command)
                    if response:
                        print(response)
                elif choice == "11":
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Please try again.")

        except ftplib.all_errors as e:
            print(f"FTP error: {e}")
