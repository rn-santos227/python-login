import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config.config import smtp_server, smtp_port, email_user, email_password

def send_email(receiver_email, subject, message):
  email_message = MIMEMultipart()
  email_message["From"] = email_user
  email_message["To"] = receiver_email
  email_message["Subject"] = subject

  email_message.attach(MIMEText(message, "plain"))

  try:
    server = smtplib.SMTP(smtp_server, smtp_port)

  except Exception as e:
    print(f"Failed to send email: {e}")