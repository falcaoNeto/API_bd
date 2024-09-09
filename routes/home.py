from flask import Blueprint, render_template

home_route = Blueprint('home', __name__)

@home_route.route('/')
def main():
    return render_template('pag.html')



