#AQUI NÓS IMPORTAMOS TODAS AS BIBLIOTECAS QUE VAMOS PRCISAR DURANTE O DESENVOLVIMENTO DO NOSSO PROJETO
from crypt import methods
from flask import (Flask, render_template, request)
from http import server
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(name, email, phone):
    host = "smtp.office365.com"
    port = "587"
    login = "blakewebassociation@outlook.com"
    senha = "Kaga@2019"
    name = name
    email = email
    phone = phone

    server = smtplib.SMTP(host, port)

    server.ehlo()
    server.starttls()
    server.login(login, senha)

    corpo = '''Nome: {name}
    Email: {email}
    Número de telefone: {phone}'''
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = "matheusercolani@gmail.com"
    email_msg['Subject'] = "Matheus você tem um novo cliente"
    email_msg.attach(MIMEText(corpo, 'plain'))

    server.sendmail(email_msg["From"], email_msg["To"], email_msg.as_string())

    server.quit()



app = Flask(__name__)

@app.route('/', methods = ('GET', 'POST'))
def index():
    if request.method =='POST':
        form = request.form
        dados_client = send_email(form['nome'], form['email'], form['phone'])
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
