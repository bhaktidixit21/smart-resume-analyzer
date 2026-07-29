import smtplib

EMAIL = "bhaktidixit21@gmail.com"
APP_PASSWORD = "cychlqqvjqwcdjvk"

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, APP_PASSWORD)
    print("Login Successful")
    server.quit()

except Exception as e:
    print(e)