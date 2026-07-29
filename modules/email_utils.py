import smtplib
import random
from email.mime.text import MIMEText

EMAIL = "bhaktidixit21@gmail.com"
APP_PASSWORD = "cychlqqvjqwcdjvk"


def generate_otp():
    return str(random.randint(100000, 999999))


def send_otp(receiver_email, otp):

    subject = "Smart Resume Analyzer - Password Reset OTP"

    body = f"""
Hello,

Your OTP is: {otp}

This OTP is valid for 5 minutes.
"""

    msg = MIMEText(body)

    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = receiver_email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()

        server.starttls()
        server.ehlo()

        server.login(EMAIL, APP_PASSWORD)

        server.sendmail(
            EMAIL,
            receiver_email,
            msg.as_string()
        )

        server.quit()

        print("OTP Sent Successfully")

    except Exception as e:
        print("EMAIL ERROR:", e)
        raise