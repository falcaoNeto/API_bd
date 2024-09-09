from flask import Blueprint, render_template, request
import json

cliente_route = Blueprint('cliente', __name__)


@cliente_route.route('/cadastros')
def cadastros():
    with open('db/pessoas.json') as f:
        pessoas = json.load(f)
    return render_template('pessoas.html', pessoas=pessoas)

@cliente_route.route('/inserir')
def inserir():
    return render_template('form_add.html')

@cliente_route.route('/', methods=['POST'])
def inserirForm():
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
    return render_template('form_busca.html')

@cliente_route.route('/id', methods=['POST'])
def buscarForm():
    cpf = request.form.get('cpf')
    with open('db/pessoas.json', 'r') as f:
            dados = json.load(f)
        
    for pessoa in dados:
            if pessoa.get('cpf') == cpf:
                return render_template('busca_result.html', pessoa=pessoa)    
    return 'cpf não encontrado'
