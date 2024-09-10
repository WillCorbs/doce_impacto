from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from config import db

login_blueprint = Blueprint('login', __name__)


@login_blueprint.route('/', methods=['GET'])
def login():
    return render_template('login.html')

@login_blueprint.route('/read-login-form', methods=['GET', 'POST'])
def read_login_form():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        cursor = db.cursor(dictionary=True)
        cursor.execute(f'''
            SELECT *
            FROM USUARIOS
            WHERE EMAIL = '{email}'
                AND SENHA = '{senha}';
        ''')
        usuario = cursor.fetchone()
        print(usuario)

        if usuario:
            return render_template('index.html')
        
        else:
            return redirect(url_for('login.login'))
    
    return render_template('login.html')


@login_blueprint.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@login_blueprint.route('/cadastro', methods=['GET'])
def cadastro():
    return render_template('cadastro.html')
