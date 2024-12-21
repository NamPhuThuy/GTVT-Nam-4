import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Cấu hình thông tin email

smtp_server = "smtp.gmail.com"
smtp_port = 587  # Cổng SMTP cho TLS
smtp_user = "namwizard22@gmail.com"

# Mật khẩu ứng dụng email
# cách bật: https://support.google.com/accounts/answer/185833?hl=vi
smtp_password = ""  # Mật khẩu ứng dụng email

# Tạo đối tượng MIMEMultipart
msg = MIMEMultipart()
msg["From"] = smtp_user
msg["To"] = "dungle@imail.edu.vn"
msg["Subject"] = "Test Email"

# Thêm nội dung email
body = "test 123"
msg.attach(MIMEText(body, "plain"))

# Kết nối đến máy chủ SMTP và gửi email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)
    text = msg.as_string()
    server.sendmail(smtp_user, "dungle@imail.edu.vn", text)
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
finally:
    server.quit()
