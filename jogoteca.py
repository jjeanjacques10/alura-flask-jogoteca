from flask import Flask
from flask_mysqldb import MySQL

#Instanciando o objeto Flask
app = Flask(__name__)
app.config.from_pyfile('config.py')

db = MySQL(app)

from views import *

if __name__ == '__main__':
    #Rodando a aplicação(Online)
    #app.run(host='192.168.10.110', port=8065)
    #Rodando a aplicação(Local)
    app.run(debug = True, host = '0.0.0.0', port=8080)
