import imaplib
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import getpass
import quopri
import base64

# Cấu hình thông tin email
imap_server = "imap.gmail.com"
imap_port = 993  # Cổng IMAP cho SSL
imap_user = "namwizard22@gmail.com"

# Mật khẩu ứng dụng email
# cách bật: https://support.google.com/accounts/answer/185833?hl=vi
imap_password = ""


def decode_content(content, encoding):
    if encoding == "quoted-printable":
        return quopri.decodestring(content).decode("utf-8", errors="ignore")
    elif encoding == "base64":
        return base64.b64decode(content).decode("utf-8", errors="ignore")
    else:
        return content.decode("utf-8", errors="ignore")


def get_email_content(msg):
    # Nếu là multipart
    if msg.is_multipart():
        # Lặp qua từng phần tử trong msg
        for part in msg.get_payload():
            # Đệ quy để lấy nội dung
            return get_email_content(part)
    else:
        # Lấy nội dung và giải mã nếu cần
        content_type = msg.get_content_type()
        content = msg.get_payload(decode=True)
        encoding = msg.get("Content-Transfer-Encoding", "").lower()
        if content_type == "text/plain" or content_type == "text/html":
            return decode_content(content, encoding)
        else:
            return content


def get_email_info(msg):
    # Lấy thông tin người gửi và người nhận
    from_addr = parseaddr(msg.get("From"))[1]
    to_addr = parseaddr(msg.get("To"))[1]

    # Lấy tiêu đề email
    subject = decode_header(msg.get("Subject"))[0][0]
    if isinstance(subject, bytes):
        subject = subject.decode()

    # Lấy nội dung email
    content = get_email_content(msg)

    return from_addr, to_addr, subject, content


def check_email(imap_user, imap_password):
    # Kết nối đến máy chủ IMAP
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(imap_user, imap_password)

    # Chọn thư mục inbox
    mail.select("inbox")

    # Tìm kiếm email
    result, data = mail.search(None, "ALL")

    # Lấy email mới nhất
    latest_email_id = data[0].split()[-1]

    # Lấy email theo số thứ tự
    result, data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = data[0][1]

    # Giải mã email
    msg = email.message_from_bytes(raw_email)

    # Lấy thông tin email
    from_addr, to_addr, subject, content = get_email_info(msg)

    # Hiển thị thông tin email
    print(f"From: {from_addr}")
    print(f"To: {to_addr}")
    print(f"Subject: {subject}")
    print(f"Content: {content}")
    print("--------------------------------------------------")

    # Đóng kết nối
    mail.close()
    mail.logout()


if __name__ == "__main__":
    check_email(imap_user, imap_password)
