from http import server
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.office365.com"
port = "587"
login = "blakewebassociation@outlook.com"
senha = "Kaga@2019"

server = smtplib.SMTP(host, port)

server.ehlo()
server.starttls()
server.login(login, senha)

corpo = "email teste hahahahaha"
email_msg = MIMEMultipart()
email_msg['From'] = login
email_msg['To'] = "rezbosa@gmail.com"
email_msg['Subject'] = "email teste"
email_msg.attach(MIMEText(corpo, 'plain'))

server.sendmail(email_msg["From"], email_msg["To"], email_msg.as_string())

server.quit()

