from resources import funcaolimpar as fl
from resources import tela_login_v3 as tl
from datetime import datetime
import sqlite3

# Conectando ao banco de dados ou criando-o se não existir
conexao = sqlite3.connect('hortifruti.db')
cursor = conexao.cursor()

# Criando a tabela 'vendas' se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data_hora TEXT NOT NULL,
        nome TEXT NOT NULL,
        quantidade REAL NOT NULL,
        preco_unitario REAL NOT NULL,
        preco_total REAL NOT NULL
    )
''')
conexao.commit()





# Exibir produtos disponíveis (puxando os produtos do banco de dados)
def exibir_produtos(con):
    print("\n--- Produtos Disponíveis ---")
    cursor = con.cursor()
    cursor.execute("SELECT id, nome, tipo, valor FROM alimentos")
    produtos = cursor.fetchall()
    for produto in produtos:
        id, nome, tipo, valor = produto
        print(f"{id} - {nome} | R${valor:.2f} ({tipo})")

# Registrar venda no sistema de caixa
def registrar_venda(con):
    exibir_produtos(con)
    total_venda = 0
    vendas_registradas = []  # Lista para armazenar detalhes das vendas

    while True:
        try:
            codigo_produto = int(input("Digite o código do produto (ou 0 para finalizar): "))
            if codigo_produto == 0:
                break
            
            cursor = con.cursor()
            cursor.execute("SELECT nome, valor, tipo FROM alimentos WHERE id = ?", (codigo_produto,))
            produto = cursor.fetchone()

            if produto:
                nome, preco_unitario, tipo_venda = produto
                quantidade = float(input(f"Digite a quantidade para {nome} ({tipo_venda}): "))
                preco_total = quantidade * preco_unitario
                total_venda += preco_total
                data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Adiciona os detalhes da venda na lista
                vendas_registradas.append((data_hora, nome, quantidade, preco_unitario, preco_total))
                
                print(f"{nome} adicionado: {quantidade} x R${preco_unitario:.2f} = R${preco_total:.2f}")
            else:
                print("Código de produto inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

    # Inserir todas as vendas registradas de uma vez na tabela de vendas
    if vendas_registradas:
        cursor.executemany('''
            INSERT INTO vendas (data_hora, nome, quantidade, preco_unitario, preco_total)
            VALUES (?, ?, ?, ?, ?)
        ''', vendas_registradas)
        con.commit()
        print(f"\nTotal da venda: R${total_venda:.2f}")

# Menu do sistema de caixa
def loop_menu_caixa():
    con = sqlite3.connect('hortifruti.db')
    while True:
        print("\n--- Sistema de Caixa ---")
        print("1 - Registrar venda")
        print("2 - Exibir produtos disponíveis")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")
        fl.limpar()

        if opcao == "1":
            registrar_venda(con)
        elif opcao == "2":
            exibir_produtos(con)
        elif opcao == "3":
            con.close()
            tl.usuario = None
            return
        else:
            print("Opção inválida. Por favor, insira uma opção válida.")
