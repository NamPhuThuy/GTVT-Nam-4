import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass

SMTP_Server = "smtp.gmail.com"  # aspmx.l.google.com
SMTP_Port = 587


def send_email(sender, receiver):
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = receiver

    subject = input("Enter the subject: ")
    msg["Subject"] = subject

    message = input("Enter the message: ")
    part = MIMEText(message, "plain")
    part.set_payload(message)
    msg.attach(part)

    # tạo smtp session
    session = smtplib.SMTP(SMTP_Server, SMTP_Port)

    session.set_debuglevel(1)

    session.ehlo()
    session.starttls()
    session.ehlo()

    password = input("Enter your password: ")
    session.login(sender, password)

    # gửi thư
    session.sendmail(sender, receiver, msg.as_string())
    print("Send email to {0} successfully".format(receiver))
    session.quit()


if __name__ == "__main__":
    sender = input("Enter your email: ")
    receiver = input("Enter receiver's email: ")
    send_email(sender, receiver)
