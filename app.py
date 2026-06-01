import os
from flask import Flask
from dotenv import load_dotenv
from banco import criar_banco
from routes.categorias import categorias_bp
from routes.transacoes import transacoes_bp
from routes.relatorios import relatorios_bp

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

app.register_blueprint(categorias_bp)
app.register_blueprint(transacoes_bp)
app.register_blueprint(relatorios_bp)

criar_banco()

if __name__ == '__main__':
    app.run(debug=True)

    