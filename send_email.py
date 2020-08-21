from email.mime.text import MIMEText
import smtplib

def send_email(email, sleep, average, count):
    from_email = 'nurumiiigf@gmail.com'
    from_password = 'xxx'
    to_email = email
    subject = 'Sleept Time Collector'
    message = 'Hello, your sleep time is <strong>{} h</strong> per night night. The average sleep is <strong>{} h</strong> per night tho, and this calculated from <strong>{}</strong> people.'.format(sleep, average, count)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)