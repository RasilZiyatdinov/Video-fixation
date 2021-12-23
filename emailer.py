from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
import os

def send_email(send_to, label, text, image_bytes):
    
    msg = MIMEMultipart()
    
    password = os.getenv('FROMMAILPASS')
    msg['From'] = os.getenv('FROMMAIL')
    msg['To'] = send_to
    msg['Subject'] = "Уведомление об объекте [{}]".format(label)

    try:
        msg.attach(MIMEText(text))
        
        msg.attach(MIMEImage(image_bytes))

        server = smtplib.SMTP('smtp.gmail.com: 587')

        server.starttls()

        server.login(msg['From'], password)

        server.sendmail(msg['From'], msg['To'], msg.as_string())

        server.quit()

        print("Письмо отправлено")
    except:
        print("Письмо не отправлено")
