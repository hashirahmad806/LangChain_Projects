from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()
# 1. Server and account configuration
smtp_server = "smtp.gmail.com"  # Replace with your SMTP server
port = 587  # 587 for STARTTLS, 465 for SSL


sender_email = os.getenv("SMTP_SENDER_EMAIL")
# print(sender_email)
password = os.getenv("SMTP_PASSWORD")
# print(password)


# Creating Function


def send_email_by_gmail(to: str, subject: str, body_text: str):
    if not sender_email or not password:
        raise ValueError(
            "Set SMTP_SENDER_EMAIL and SMTP_PASSWORD before sending email.")

    # 2. Create the MIMEMultipart message container
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to
    message["Subject"] = subject
    # 3. Attach the plain-text body (explicitly avoiding HTML)
    # body = "Hello,\n\nThis is a plain-text email sent using Python's smtplib and MIMEMultipart."
    message.attach(MIMEText(body_text, "plain", "utf-8"))

    # 4. Connect to the server and send the email
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # Upgrade connection to secure TLS
            server.login(sender_email, password)
            server.sendmail(sender_email, to, message.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


@tool
def send_email(to: str, subject: str, body: str):
    """
    Send email to any email  address  by providing  the correct email address  , subject and body
    Args :
        to - email address
        subject - email subject
        body - email body in the plain text
    """
    send_email_by_gmail(to, subject, body_text=body)
    return "Email Send Successfully"


ALL_TOOLS = [send_email]
# when  send email called it will cal the send by email tool
