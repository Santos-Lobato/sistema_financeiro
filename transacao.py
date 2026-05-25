from datetime import datetime
import sqlite3

class Transacao:
    def __init__(self, descricao, valor, data, tipo, categoria_id):

        if valor <= 0:
            raise ValueError("Valor deve ser maior que zero.")

        try:
            datetime.strptime(data, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Data inválida. Use o formato AAAA-MM-DD.")

        tipos_validos = ["Receita", "Despesa"]
        if tipo.capitalize() not in tipos_validos:
            raise ValueError("Tipo inválido. Use Receita ou Despesa.")


        self.descricao = descricao
        self.valor = valor
        self.data = data
        self.tipo = tipo.capitalize()
        self.categoria_id = categoria_id


    def cadastrar(self):
        conexao = sqlite3.connect("financeiro.db")
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO transacoes (descricao, valor, data, tipo, categoria_id) VALUES (?, ?, ?, ?, ?)",
            (self.descricao, self.valor, self.data, self.tipo, self.categoria_id)
        )
        conexao.commit()
        conexao.close()


    @classmethod
    def listar(cls):
        conexao = sqlite3.connect("financeiro.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM transacoes")
        transacoes = cursor.fetchall()
        conexao.close()
        return transacoes

    @classmethod
    def deletar(cls, id):
        conexao = sqlite3.connect("financeiro.db")
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM transacoes WHERE id = ?", (id,))
        conexao.commit()
        conexao.close()

    @classmethod
    def atualizar(cls, id, descricao, valor, data, tipo, categoria_id):
        if valor <= 0:
            raise ValueError("Valor deve ser maior que zero.")

        try:
            datetime.strptime(data, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Data inválida. Use o formato AAAA-MM-DD.")

        tipos_validos = ["Receita", "Despesa"]
        if tipo.capitalize() not in tipos_validos:
            raise ValueError("Tipo inválido. Use Receita ou Despesa.")

        conexao = sqlite3.connect("financeiro.db")
        cursor = conexao.cursor()
        cursor.execute(
            "UPDATE transacoes SET descricao = ?, valor = ?, data = ?, tipo = ?, categoria_id = ? WHERE id = ?", (
                descricao, valor, data, tipo.capitalize(), categoria_id, id
            )
        )
        conexao.commit()
        conexao.close()