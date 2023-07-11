from decouple import config
import smtplib
import imghdr
from email.message import EmailMessage
PASSWORD = config("PASSWORD")
SENDER = config("SENDER")
RECEIVER = config("RECEIVER")

def send_email(image_location):
    email_message = EmailMessage()
    email_message["Subject"] = "New Customer showed up!"
    email_message.set_content("I just saw something in the screen!")

    with open(image_location, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email(image_location="images/Picture with object")
    