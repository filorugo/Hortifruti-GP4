from resources import funcaolimpar as fl
from resources import crud_alimentos as ca
from resources import cadastro_de_forn as cf
from resources import tela_login_v3 as tl
import sqlite3

# Criação da conexão e cursor
conexao = sqlite3.connect('hortifruti.db')
cur = conexao.cursor()

# Criação da tabela 'doacoes' se ela não existir
cur.execute("""
CREATE TABLE IF NOT EXISTS doacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    alimento_id INTEGER NOT NULL,
    tipo TEXT NOT NULL,
    quantidade_ou_peso REAL NOT NULL,
    data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (alimento_id) REFERENCES alimentos(id)
)
""")
conexao.commit()  # Corrigido para utilizar 'conexao.commit()'

# Menu estoque
def loop_menu_estoque():
    while True:
        print("\n--- Menu Estoque ---")
        print("1 - Visualizar Alimentos")
        print("2 - Visualizar Fornecedores")
        print("3 - Registrar Doação")
        print("4 - Registrar Descarte")
        print("5 - Sair")
        
        escolhamenu = int(input("Insira o comando: "))
        fl.limpar()
        if escolhamenu == 1:
            ca.ler_alimento()
        elif escolhamenu == 2:
            cf.listar_fornecedores()
        elif escolhamenu == 3:
            registrar_doacao(conexao)
        elif escolhamenu == 4:
            registrar_descarte(conexao)
        elif escolhamenu == 5:
            conexao.close()
            tl.usuario = None
            return
        else:
            print("Comando inválido, por favor insira um número de 1 a 5.")

# Registrar Doação
def registrar_doacao(con):
    cur = con.cursor()
    print("\n--- Registrar Doação ---")
    ca.ler_alimento()  # Exibe lista com ID
    alimento_id = int(input("Insira o ID do alimento para doação: "))
    
    # Verifica o tipo de alimento pelo ID
    cur.execute("SELECT tipo FROM alimentos WHERE id = ?", (alimento_id,))
    resultado = cur.fetchone()
    
    if resultado:
        tipo = resultado[0]
        if tipo == "peso":
            quantidade = float(input("Insira o peso do alimento (kg): "))
        else:
            quantidade = int(input("Insira a quantidade do alimento: "))
        
        cur.execute("INSERT INTO doacoes (alimento_id, tipo, quantidade_ou_peso) VALUES (?, ?, ?)",
                    (alimento_id, tipo, quantidade))
        con.commit()  # Correção: commit deve ser feito em 'con'
        print(f"Doação registrada: {quantidade} {tipo} de alimento ID {alimento_id}.")
    else:
        print("ID de alimento não encontrado.")

# Registrar Descarte
def registrar_descarte(con):
    cur = con.cursor()
    print("\n--- Registrar Descarte ---")
    ca.ler_alimento()  # Exibe lista com ID
    alimento_id = int(input("Insira o ID do alimento descartado: "))
    
    # Verifica o tipo de alimento pelo ID
    cur.execute("SELECT tipo FROM alimentos WHERE id = ?", (alimento_id,))
    resultado = cur.fetchone()
    
    if resultado:
        tipo = resultado[0]
        if tipo == "peso":
            quantidade = float(input("Insira o peso do alimento (kg): "))
        else:
            quantidade = int(input("Insira a quantidade do alimento: "))
        
        cur.execute("INSERT INTO descartes (alimento_id, tipo, quantidade_ou_peso) VALUES (?, ?, ?)",
                    (alimento_id, tipo, quantidade))
        con.commit()  # Correção: commit deve ser feito em 'con'
        print(f"Descarte registrado: {quantidade} {tipo} de alimento ID {alimento_id}.")
    else:
        print("ID de alimento não encontrado.")
