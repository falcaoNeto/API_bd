from flask import Flask
from flasgger import Swagger
from routes.home import home_route
from routes.cliente import cliente_route

app = Flask(__name__)

# Inicializa o Swagger
swagger = Swagger(app)

app.register_blueprint(home_route)
app.register_blueprint(cliente_route)

app.run(debug=True)
