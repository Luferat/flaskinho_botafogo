from pathlib import Path
from flask import Flask, render_template
from controllers.contact import contact_controller
from controllers.home import home_controller
import tools.init_db as init_db


DB_PATH = Path("data/app.db")

# Inicialização do banco, se não existir
if not DB_PATH.exists():
    init_db.init_db()

app = Flask(__name__)


@app.route('/')
def home():
    # Aqui entra a lógica para a página inicial
    # Códigos Python
    return home_controller()


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    # Chama o controller (controlers.contact.py) que processa esta rota
    return contact_controller()


if __name__ == '__main__':
    app.run(debug=True)
