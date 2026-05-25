from categoria import Categoria
from transacao import Transacao
from relatorio import Relatorio


def menu():
    while True:
        print("\n=== SISTEMA FINANCEIRO ===")
        print("1. Cadastrar categoria")
        print("2. Listar categorias")
        print("3. Editar categoria")
        print("4. Deletar categoria")
        print("5. Cadastrar transação")
        print("6. Listar transações")
        print("7. Editar transação")
        print("8. Deletar transação")
        print("9. Ver balanço geral")
        print("10. Ver por categoria")
        print("11. Ver por período")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ")

        match opcao:
            case "1":
                nome = input("Nome da categoria: ")
                tipo = input("Tipo (Receita/Despesa): ")
                try:
                    Categoria(nome, tipo).cadastrar()
                    print("Categoria cadastrada!")
                except ValueError as e:
                    print(f"Erro: {e}")

            case "2":
                categorias = Categoria.listar()
                for c in categorias:
                    print(c)
            case "3":
                try:
                    id = int(input("ID da categoria: "))
                    nome = input("Novo nome da categoria: ")
                    tipo = input("Novo tipo (Receita/Despesa): ")
                    Categoria.atualizar(id, nome, tipo)
                    print("Categoria atualizada com sucesso!")
                except ValueError as e:
                    print(f"Erro: {e}")


            case "4":
                try:
                    id = int(input("ID da categoria: "))
                    Categoria.deletar(id)
                    print("Categoria deletada com sucesso!")
                except ValueError as e:
                    print(f"Erro: {e}")


            case "5":
                try:
                    descricao = input("Descrição: ")
                    valor = float(input("Valor: "))
                    data = input("Data (AAAA-MM-DD): ")
                    tipo = input("Tipo (Receita/Despesa): ")
                    categoria_id = int(input("ID da categoria: "))
                    Transacao(descricao, valor, data, tipo, categoria_id).cadastrar()
                    print("Transação cadastrada!")
                except ValueError as e:
                    print(f"Erro: {e}")

            case "6":
                transacoes = Transacao.listar()
                for t in transacoes:
                    print(t)

            case "7":
                try:
                    id = int(input("ID da transação: "))
                    descricao = input("Nova descrição: ")
                    valor = float(input("Novo valor: "))
                    data = input("Nova data (AAAA-MM-DD): ")
                    tipo = input("Novo tipo (Receita/Despesa): ")
                    categoria_id = int(input("Novo ID da categoria: "))
                    Transacao.atualizar(id, descricao, valor, data, tipo, categoria_id)
                    print("Transação atualizada com sucesso!")
                except ValueError as e:
                    print(f"Erro: {e}")

            case "8":
                try:
                    id = int(input("ID da transação: "))
                    Transacao.deletar(id)
                    print("Transação deletada com sucesso!")
                except ValueError as e:
                    print(f"Erro: {e}")

            case "9":
                balanco = Relatorio.balanco_geral()
                print(f"Receitas: R$ {balanco['receitas']}")
                print(f"Despesas: R$ {balanco['despesas']}")
                print(f"Saldo:    R$ {balanco['saldo']}")

            case "10":
                por_categoria = Relatorio.por_categoria()
                for c in por_categoria:
                    print(c)

            case "11":
                inicio = input("Data início (AAAA-MM-DD): ")
                fim = input("Data fim (AAAA-MM-DD): ")
                transacoes = Relatorio.por_periodo(inicio, fim)
                for t in transacoes:
                    print(t)

            case "0":
                print("Saindo...")
                break

            case _:
                print("Opção inválida.")


if __name__ == "__main__":
    menu()

    
