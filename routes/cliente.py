from flask import Blueprint, render_template, request
import json

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/cadastros')
def cadastros():
    """
    Exibe a lista de pessoas cadastradas
    ---
    responses:
      200:
        description: Lista de pessoas cadastradas
        content:
          text/html:
            schema:
              type: string
    """
    with open('db/pessoas.json') as f:
        pessoas = json.load(f)
    return render_template('pessoas.html', pessoas=pessoas)

@cliente_route.route('/inserir')
def inserir():
    """
    Exibe o formulário para inserir um novo cadastro
    ---
    responses:
      200:
        description: Formulário de inserção renderizado com sucesso.
        content:
          text/html:
            schema:
              type: string
    """
    return render_template('form_add.html')

@cliente_route.route('/', methods=['POST'])
def inserirForm():
    """
    Insere um novo cadastro a partir do formulário
    ---
    parameters:
      - name: nome
        in: formData
        type: string
        required: true
      - name: cpf
        in: formData
        type: string
        required: true
      - name: data
        in: formData
        type: string
        required: true
    responses:
      200:
        description: Novo cadastro inserido com sucesso.
        content:
          text/html:
            schema:
              type: string
    """
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    data = request.form.get('data')
    dado = {
        'nome': nome,
        'cpf': cpf,
        'data': data
    }
    with open('db/pessoas.json', 'r') as f:
        novo = json.load(f)
        novo.append(dado)

    with open('db/pessoas.json', 'w') as f:
        json.dump(novo, f)
          
    return render_template('pag.html')

@cliente_route.route('/buscar')
def buscar():
    """
    Exibe o formulário de busca por CPF
    ---
    responses:
      200:
        description: Formulário de busca renderizado com sucesso.
        content:
          text/html:
            schema:
              type: string
    """
    return render_template('form_busca.html')

@cliente_route.route('/id', methods=['POST'])
def buscarForm():
    """
    Busca cadastro por CPF
    ---
    parameters:
      - name: cpf
        in: formData
        type: string
        required: true
    responses:
      200:
        description: Cadastro encontrado com sucesso.
        content:
          text/html:
            schema:
              type: string
      404:
        description: CPF não encontrado.
    """
    cpf = request.form.get('cpf')
    with open('db/pessoas.json', 'r') as f:
        dados = json.load(f)
        
    for pessoa in dados:
        if pessoa.get('cpf') == cpf:
            return render_template('busca_result.html', pessoa=pessoa)
            
    return 'cpf não encontrado', 404
