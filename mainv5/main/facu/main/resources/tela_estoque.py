from resources import funcaolimpar as fl
from resources import crud_alimentos as ca
from resources import funcao_estoque as fe

import sqlite3

conexao = sqlite3.connect('hortifruti.db')

# Menu estoque
def loop_menu_estoque():
    while True:
        print("\n--- Menu Estoque ---")
        print("1 - Vizualizar Alimentos")
        print("2 - Vizualizar fornecedores")
        print("3 - Relatório alimentos p/ doação")
        print("4 - Relatório alimentos estragados")
        print("5 - Sair")
        
        escolhamenu = int(input("Insira o comando: "))
        fl.limpar()
        if escolhamenu == 1:
            ca.ler_alimento()
        elif escolhamenu == 2:
            ca.listar_fornecedores()
        elif escolhamenu == 3:
            fe.registrar_doacao()
        elif escolhamenu == 4:
            fe.registrar_descarte()
        elif escolhamenu == 5:
            print("Saindo do sistema...")
            conexao.close()
        else:
            print("Comando inválido, por favor insira um número de 1 a 5.")


def conectar_db():
    con = sqlite3.connect("hortifruti.db")
    cur = con.cursor()
    # Criando a tabela de doações, se não existir
    cur.execute("""
    CREATE TABLE IF NOT EXISTS doacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        alimento TEXT NOT NULL,
        tipo TEXT NOT NULL,
        quantidade_ou_peso REAL NOT NULL,
        data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    return con, cur


def registrar_doacao(con, cur):
    alimento = input("Insira o nome do alimento para doação: ")
    tipo = input("O alimento é vendido por peso ou quantidade? (peso/quantidade): ").strip().lower()

    if tipo == "peso":
        peso = float(input("Insira o peso do alimento (kg): "))
        # Salvando no banco de dados
        cur.execute("INSERT INTO doacoes (alimento, tipo, quantidade_ou_peso) VALUES (?, ?, ?)", (alimento, tipo, peso))
        con.commit()
        print(f"{alimento} de {peso} kg registrado para doação.")
    elif tipo == "quantidade":
        quantidade = int(input("Insira a quantidade do alimento: "))
        # Salvando no banco de dados
        cur.execute("INSERT INTO doacoes (alimento, tipo, quantidade_ou_peso) VALUES (?, ?, ?)", (alimento, tipo, quantidade))
        con.commit()
        print(f"{quantidade} unidades de {alimento} registradas para doação.")
    else:
        print("Tipo inválido. Insira 'peso' ou 'quantidade'.")
# função para registrar alimentos descartados
def registrar_descarte(con, cur):
    alimento = input("Insira o nome do alimento descartado: ")
    tipo = input("O alimento é vendido por peso ou quantidade? (peso/quantidade): ").strip().lower()

    if tipo == "peso":
        peso = float(input("Insira o peso do alimento (kg): "))
        # Salvando no banco de dados
        cur.execute("INSERT INTO doacoes (alimento, tipo, quantidade_ou_peso) VALUES (?, ?, ?)", (alimento, tipo, peso))
        con.commit()
        print(f"{alimento} de {peso} kg registrado como descartado.")
    elif tipo == "quantidade":
        quantidade = int(input("Insira a quantidade do alimento: "))
        # Salvando no banco de dados
        cur.execute("INSERT INTO doacoes (alimento, tipo, quantidade_ou_peso) VALUES (?, ?, ?)", (alimento, tipo, quantidade))
        con.commit()
        print(f"{quantidade} unidades de {alimento} registradas como descartadas.")
    else:
        print("Tipo inválido. Insira 'peso' ou 'quantidade'.")