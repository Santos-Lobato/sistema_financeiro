from flask import Blueprint, render_template, request, redirect, url_for
from categoria import Categoria

categorias_bp = Blueprint("categorias", __name__)

@categorias_bp.route("/categorias")
def listar():
    categorias = Categoria.listar()
    return render_template("categorias.html", categorias=categorias)

@categorias_bp.route("/categorias/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form.get("nome")
    tipo = request.form.get("tipo")
    try:
        Categoria(nome, tipo).cadastrar()
    except ValueError as e:
        return redirect(url_for("categorias.listar", erro=str(e)))
    return redirect(url_for("categorias.listar"))

@categorias_bp.route("/categorias/editar", methods=["POST"])
def editar():
    id = int(request.form.get("id"))
    nome = request.form.get("nome")
    tipo = request.form.get("tipo")
    try:
        Categoria.atualizar(id, nome, tipo)
    except ValueError as e:
        return redirect(url_for("categorias.listar", erro=str(e)))
    return redirect(url_for("categorias.listar"))

@categorias_bp.route("/categorias/deletar", methods=["POST"])
def deletar():
    id = int(request.form.get("id"))
    try:
        Categoria.deletar(id)
    except ValueError as e:
        return redirect(url_for("categorias.listar", erro=str(e)))
    return redirect(url_for("categorias.listar"))
    


