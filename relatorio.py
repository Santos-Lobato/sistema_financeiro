import sqlite3

class Relatorio:

    @classmethod
    def balanco_geral(cls):
        conexao = sqlite3.connect("financeiro.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT tipo, SUM(valor) FROM transacoes GROUP BY tipo")
        resultado = cursor.fetchall()
        conexao.close()

        receitas = 0
        despesas = 0

        for tipo, total in resultado:
            if tipo == "Receita":
                receitas = total
            elif tipo == "Despesa":
                despesas = total

        saldo = receitas - despesas
        return {"receitas": receitas, "despesas": despesas, "saldo": saldo}

    @classmethod
    def por_categoria(cls):
        conexao = sqlite3.connect("financeiro.db")
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT categorias.nome, SUM(transacoes.valor)
            FROM transacoes
            JOIN categorias ON transacoes.categoria_id = categorias.id
            GROUP BY categorias.nome
        """)
        resultado = cursor.fetchall()
        conexao.close()
        return resultado

    @classmethod
    def por_periodo(cls, data_inicio, data_fim):
        conexao = sqlite3.connect("financeiro.db")
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM transacoes
            WHERE data BETWEEN ? AND ?
            ORDER BY data
        """, (data_inicio, data_fim))
        resultado = cursor.fetchall()
        conexao.close()
        return resultado








