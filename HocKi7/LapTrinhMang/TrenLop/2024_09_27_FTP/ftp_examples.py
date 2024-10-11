import  ftplib

def download_file(ftp_server, username, password, remote_file, local_file):
    """Downloads a file from an FTP server.
  
    Args:
      ftp_server: The FTP server address.
      username: The username for the FTP server.
      password: The password for the FTP server.
      remote_file: The name of the remote file to download.
      local_file: The name of the local file to save the downloaded content.
    """

    try:
        with ftplib.FTP(ftp_server) as ftp:
            ftp.login(username, password)
            with open(local_file, 'wb') as f:
                ftp.retrbinary('RETR ' + remote_file, f.write)
            print(f"Downloaded {remote_file} to {local_file}")
    except Exception as e:
        print(f"Error downloading file: {e}")

def upload_file(ftp_server, username, password, local_file, remote_file):
    """Uploads a file to an FTP server.
  
    Args:
      ftp_server: The FTP server address.
      username: The username for the FTP server.
      password: The password for the FTP server.
      local_file: The name of the local file to upload.
      remote_file: The name of the remote file to create.
    """

    try:
        with ftplib.FTP(ftp_server) as ftp:
            ftp.login(username, password)
            with open(local_file, 'rb') as f:
                ftp.storbinary('STOR ' + remote_file, f)
            print(f"Uploaded {local_file} to {remote_file}")
    except Exception as e:
        print(f"Error uploading file: {e}")

def list_files(ftp_server, username, password):
    """Lists files on an FTP server.
  
    Args:
      ftp_server: The FTP server address.
      username: The username for the FTP server.
      password: The password for the FTP server.
    """

    try:
        with ftplib.FTP(ftp_server) as ftp:
            ftp.login(username, password)
            ftp.dir()
    except Exception as e:
        print(f"Error listing files: {e}")

if __name__ == "__main__":
    ftp_server = "test.rebex.net"
    username = "demo"
    password = "password"
    remote_file = "remote_file.txt"
    local_file = "downloaded_file.txt"
    
    download_file(ftp_server, username, password, remote_file, local_file)