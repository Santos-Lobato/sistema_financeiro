from flask import Blueprint, render_template, request
from relatorio import Relatorio

relatorios_bp = Blueprint("relatorios", __name__)

@relatorios_bp.route("/relatorios")
def index():
    balanco = Relatorio.balanco_geral()
    por_categoria = Relatorio.por_categoria()

    data_inicio = request.args.get("data_inicio")
    data_fim = request.args.get("data_fim")
    por_periodo = None

    if data_inicio and data_fim:
        por_periodo = Relatorio.por_periodo(data_inicio, data_fim)

    return render_template("relatorios.html",
                           balanco=balanco,
                           por_categoria=por_categoria,
                           por_periodo=por_periodo,
                           data_inicio=data_inicio,
                           data_fim=data_fim)