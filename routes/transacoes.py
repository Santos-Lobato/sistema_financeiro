from flask import Blueprint, render_template, request, redirect, url_for
from transacao import Transacao
from categoria import Categoria

transacoes_bp = Blueprint("transacoes", __name__)

@transacoes_bp.route("/transacoes")
def listar():
    transacoes = Transacao.listar()
    categorias = Categoria.listar()
    return render_template("transacoes.html", transacoes=transacoes, categorias=categorias)

@transacoes_bp.route("/transacoes/cadastrar", methods=["POST"])
def cadastrar():
    descricao = request.form.get("descricao")
    valor = float(request.form.get("valor"))
    data = request.form.get("data")
    tipo = request.form.get("tipo")
    categoria_id = int(request.form.get("categoria_id"))
    try:
        Transacao(descricao, valor, data, tipo, categoria_id).cadastrar()
    except ValueError as e:
        return redirect(url_for("transacoes.listar", erro=str(e)))
    return redirect(url_for("transacoes.listar"))

@transacoes_bp.route("/transacoes/editar", methods=["POST"])
def editar():
    id = int(request.form.get("id"))
    descricao = request.form.get("descricao")
    valor = float(request.form.get("valor"))
    data = request.form.get("data")
    tipo = request.form.get("tipo")
    categoria_id = int(request.form.get("categoria_id"))
    try:
        Transacao.atualizar(id, descricao, valor, data, tipo, categoria_id)
    except ValueError as e:
        return redirect(url_for("transacoes.listar", erro=str(e)))
    return redirect(url_for("transacoes.listar"))

@transacoes_bp.route("/transacoes/deletar", methods=["POST"])
def deletar():
    id = int(request.form.get("id"))
    try:
        Transacao.deletar(id)
    except ValueError as e:
        return redirect(url_for("transacoes.listar", erro=str(e)))
    return redirect(url_for("transacoes.listar"))