#AQUI NÓS IMPORTAMOS TODAS AS BIBLIOTECAS QUE VAMOS PRCISAR DURANTE O DESENVOLVIMENTO DO NOSSO PROJETO
from flask import (Flask, render_template)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == 'main':
    app.run(debug=True)
