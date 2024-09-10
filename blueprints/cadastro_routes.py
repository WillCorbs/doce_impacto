from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from config import mysql, db

cadastro_blueprint = Blueprint('cadastro', __name__)

@cadastro_blueprint.route('/criar-usuario', methods=['POST'])
def criar_usuario():
    if request.method == 'POST':
        dados = request.form

        query = f"""
            INSERT INTO USUARIOS(
                NOME,
                EMAIL,
                SENHA,
                TELEFONE,
                SEXO,
                DATA_NASC,
                CURSO_CARGO,
                TURNO,
                TIPO
            )
            VALUES(
                '{dados['nome']}',
                '{dados['email']}',
                '{dados['senha']}',
                {dados['telefone']},
                '{dados['genero']}',
                '{dados['data_nasc']}',
                '{dados['curso_cargo']}',
                '{dados['turno']}',
                1
            );
        """

        cursor = db.cursor(dictionary=True)
        cursor.execute(f'''
            SELECT *
            FROM USUARIOS
            WHERE EMAIL = '{dados['email']}';
        ''')
        usuario = cursor.fetchone()

        if usuario:
            return redirect(url_for('login.cadastro'))
        
        else:
            cur = mysql.connection.cursor()
            cur.execute(query)
            mysql.connection.commit()

            return redirect(url_for('login.login'))
    
    return render_template('cadastro.html')
