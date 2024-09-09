from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 8000
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'DOCE_IMPACTO'

mysql = MySQL(app)
