from flask import (Flask, render_template, request)
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# class Cliente():
#     nome = ""
#     email = ""
#     phone = ""

#     def __init__(self, nome, email, phone):
#         self.nome = nome
#         self.email = email
#         self.phone = phone

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

    # corpo = f'''
    # Nome: {name}
    # Email: {email}
    # Número de telefone: {phone}'''
    # email_msg = MIMEMultipart()
    # email_msg['From'] = login
    # email_msg['To'] = "rezbosa@gmail.com"
    # email_msg['Subject'] = "Matheus você tem um novo cliente"
    # email_msg.attach(MIMEText(corpo, 'plain'))

    # server.sendmail(email_msg["From"], email_msg["To"], email_msg.as_string())

    server.quit()



app = Flask(__name__)

@app.route('/', methods = ('GET', 'POST'))
def index():
    nome_cliente = None
    if request.method =='POST':
        form = request.form
        send_email(form['nome'], form['email'], form['phone'])
        nome_cliente = form['nome']
    return render_template('index.html', nome_cliente = nome_cliente)

if __name__ == '__main__':
    app.run(debug=True)
