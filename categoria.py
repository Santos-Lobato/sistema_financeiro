import sqlite3

class Categoria:
    def __init__(self, nome, tipo):
        tipos_validos = ["Receita", "Despesa"]
        if tipo.capitalize() not in tipos_validos:
            raise ValueError("Tipo inválido. Use Receita ou Despesa.")

        self.nome = nome.capitalize()
        self.tipo = tipo.capitalize()


    def cadastrar(self):
        conexao = sqlite3.connect("financeiro.db")
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO categorias (nome, tipo) VALUES (?, ?)",
                       (self.nome, self.tipo))
        conexao.commit()
        conexao.close()

    @classmethod
    def listar(cls):
        conexao = sqlite3.connect("financeiro.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM categorias")
        categorias = cursor.fetchall()
        conexao.close()
        return categorias

    @classmethod
    def deletar(cls, id):
        conexao = sqlite3.connect("financeiro.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT COUNT(*) FROM transacoes WHERE categoria_id = ?", (id,))
        if cursor.fetchone()[0] > 0:
            conexao.close()
            raise ValueError("Categoria possui transações vinculadas e não pode ser deletada.")
        cursor.execute("DELETE FROM categorias WHERE id = ?", (id,))
        conexao.commit()
        conexao.close()

    @classmethod
    def atualizar(cls, id, novo_nome, novo_tipo):
        tipos_validos = ["Receita", "Despesa"]
        if novo_tipo.capitalize() not in tipos_validos:
            raise ValueError("Tipo inválido. Use Receita ou Despesa.")

        conexao = sqlite3.connect("financeiro.db")
        cursor = conexao.cursor()
        cursor.execute("UPDATE categorias SET nome = ?, tipo = ? WHERE id = ?",
                       (novo_nome.capitalize(), novo_tipo.capitalize(), id))
        conexao.commit()
        conexao.close()