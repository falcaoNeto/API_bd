from flask import Flask
from routes.home import home_route
from routes.cliente import cliente_route


app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(cliente_route)

app.run(debug=True)























#@app.route('/')
# def main():

#     return render_template('pag.html')

#@app.route('/cadastros')
# def cadastros():
#     titulo = 'cadastros'
#     pessoas = [
#         {"nome": "Maria", "cpf": "01007251204"},
#         {"nome": "Joao", "cpf": "05124857501"},
#         {"nome": "Carlos", "cpf": "09562485780"},
#     ]

#     return render_template('index.html', titulo=titulo, pessoas=pessoas)