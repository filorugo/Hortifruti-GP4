from resources import funcaolimpar as fl
import sqlite3

# conectando ao banco de dados ou criando se nao existir
conexao = sqlite3.connect('hortifruti.db')
cursor = conexao.cursor()

# Criando a tabela 'alimentos' se nao existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS alimentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL UNIQUE,
        tipo TEXT NOT NULL,
        valor REAL NOT NULL
    )
''')
conexao.commit()

# funcao que adiciona um alimento na lista, e verifica se o nome já foi cadastrado
def cadastrar_alimentos():
    while True:
        nome = input("Digite o nome do alimento: ")
        tipo = input("O alimento é vendido por peso ou por unidade? (peso/unidade): ").strip().lower()
        
        if tipo not in ["peso", "unidade"]:
            print("Tipo inválido. Por favor, insira 'peso' ou 'unidade'.")
            continue
        
        valor = float(input(f"Digite o valor por {'quilo' if tipo == 'peso' else 'unidade'}: ").replace(",", "."))
        
        try:
            cursor.execute("INSERT INTO alimentos (nome, tipo, valor) VALUES (?, ?, ?)", (nome, tipo, valor))
            conexao.commit()
            print(f"Alimento '{nome}' cadastrado com sucesso.")
        except sqlite3.IntegrityError:
            print("Alimento já cadastrado.")
        
        adicionar_mais = input("Deseja adicionar mais um alimento? (s/n): ").strip().lower()
        if adicionar_mais != 's':
            break

# funcao que busca e imprime todos os alimentos cadastrados, junto com seus atributos
def ler_alimento():
    cursor.execute("SELECT nome, tipo, valor FROM alimentos")
    alimentos = cursor.fetchall()
    
    if alimentos:
        for alimento in alimentos:
            tipo = "Peso" if alimento[1] == "peso" else "Unidade"
            print(f"Nome: {alimento[0]}, Tipo: {tipo}, Valor: R${alimento[2]:.2f}")
    else:
        print("Nenhum alimento encontrado.")
# funcao que atualiza atributos de alimentos já cadastrados
def atualizar_alimento(nome, tipo=None, valor=None):
    cursor.execute("SELECT * FROM alimentos WHERE nome = ?", (nome,))
    alimento = cursor.fetchone()
    
    if alimento:
        if tipo:
            cursor.execute("UPDATE alimentos SET tipo = ? WHERE nome = ?", (tipo, nome))
        if valor is not None:
            cursor.execute("UPDATE alimentos SET valor = ? WHERE nome = ?", (valor, nome))
        
        conexao.commit()
        print(f"Alimento '{nome}' atualizado com sucesso.")
    else:
        print("Alimento não encontrado.")

# funcao que acessa a lista de alimentos com o nome e o deleta
def deletar_alimento(nome):
    cursor.execute("SELECT * FROM alimentos WHERE nome = ?", (nome,))
    if cursor.fetchone():
        cursor.execute("DELETE FROM alimentos WHERE nome = ?", (nome,))
        conexao.commit()
        print(f"Alimento '{nome}' deletado com sucesso.")
    else:
        print("Alimento não encontrado.")

# Menu principal
def loop_menu_crud_alimentos():
    while True:
        print("\n--- Menu CRUD de Alimentos ---")
        print("1 - Cadastrar Alimentos")
        print("2 - Ler Alimento")
        print("3 - Atualizar Alimento")
        print("4 - Deletar Alimento")
        print("5 - Voltar")
        
        escolhamenu = int(input("Insira o comando: "))
        fl.limpar()
        if escolhamenu == 1:
            cadastrar_alimentos()
        elif escolhamenu == 2:
            ler_alimento()
        elif escolhamenu == 3:
            atualizar_alimento()
        elif escolhamenu == 4:
            deletar_alimento()
        elif escolhamenu == 5:
            conexao.close()
            return
        else:
            print("Comando inválido, por favor insira um número de 1 a 5.")


# funcoes: `ler_alimento`, `cadastrar alimentos`, `deletar alimentos` `atualizar_alimento` e `loop_menu_admin`.
