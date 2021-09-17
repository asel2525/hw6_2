import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from decouple import config


from_email = config('from_email',default='')
password = config('password',default='')

# print(from_email, password)

msg = MIMEMultipart()

to_email = 'aselalybaeva42@gmail.com'
message = 'Привет, это отправка смс через smtplib!123'

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
server.login(from_email, password)
server.sendmail(from_email, to_email, msg.as_string())
server.quit()