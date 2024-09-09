from flask import Blueprint, request, jsonify, render_template, redirect, url_for

login_blueprint = Blueprint('login', __name__)


@login_blueprint.route('/', methods=['GET'])
def login():
    return render_template('login.html')

@login_blueprint.route('/read_login_form', methods=['GET', 'POST'])
def read_login_form():
    if request.method == 'POST':
        return redirect(url_for('login.index'))
    
    return render_template('index.html')

@login_blueprint.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@login_blueprint.route('/cadastro', methods=['GET'])
def cadastro():
    return render_template('cadastro.html')
