from flask import Blueprint, render_template

home_route = Blueprint('home', __name__)

@home_route.route('/')
def main():
    """
    Página principal
    ---
    responses:
      200:
        description: Página inicial renderizada com sucesso.
        content:
          text/html:
            schema:
              type: string
    """
    return render_template('pag.html')
