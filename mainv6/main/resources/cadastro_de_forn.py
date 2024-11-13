import sqlite3  # Importa o módulo sqlite3 para trabalhar com bancos de dados SQLite
from resources import funcaolimpar as fl
# Conecta ou cria um banco de dados chamado fornecedores.db
conexao = sqlite3.connect('hortifruti.db')  # Conecta ao banco de dados (ou cria, se não existir)
cursor = conexao.cursor()  # Cria um cursor para realizar operações no banco

# Cria a tabela de fornecedores caso não exista
cursor.execute('''
CREATE TABLE IF NOT EXISTS fornecedores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- ID único e autoincrementado para cada fornecedor
    nome TEXT NOT NULL,  -- Nome do fornecedor, campo obrigatório
    cnpj TEXT NOT NULL UNIQUE,  -- CNPJ do fornecedor, campo único e obrigatório
    telefone TEXT  -- Telefone do fornecedor, campo opcional
)
''')
conexao.commit()  # Confirma (commita) a criação da tabela no banco de dados

# Função para cadastrar um fornecedor
def cadastrar_fornecedor():
    # Solicita ao usuário as informações do fornecedor
    nome = input("Digite o nome do fornecedor: ")
    cnpj = input("Digite o CNPJ do fornecedor: ")
    telefone = input("Digite o telefone do fornecedor: ")
    try:
        # Insere as informações do fornecedor na tabela
        cursor.execute('''
        INSERT INTO fornecedores (nome, cnpj, telefone)
        VALUES (?, ?, ?)
        ''', (nome, cnpj, telefone))
        conexao.commit()  # Salva as alterações no banco de dados
        print("Fornecedor cadastrado com sucesso!")  # Confirmação de cadastro
    except sqlite3.IntegrityError:  # Captura erros de integridade, como CNPJ duplicado
        print("Erro: CNPJ já cadastrado.")  # Mensagem de erro para CNPJ duplicado

# Função para listar todos os fornecedores
def listar_fornecedores():
    cursor.execute("SELECT * FROM fornecedores")  # Busca todos os fornecedores na tabela
    fornecedores = cursor.fetchall()  # Recupera todos os registros encontrados
    if fornecedores:
        # Itera sobre a lista de fornecedores e exibe cada um
        for fornecedor in fornecedores:
            print(f"ID: {fornecedor[0]}, Nome: {fornecedor[1]}, CNPJ: {fornecedor[2]}, Telefone: {fornecedor[3]}")
    else:
        print("Nenhum fornecedor cadastrado.")  # Informa se não há fornecedores cadastrados

# Função para atualizar um fornecedor pelo ID
def atualizar_fornecedor():
    # Solicita o ID e os novos dados do fornecedor
    fornecedor_id = input("Digite o ID do fornecedor que deseja atualizar: ")
    nome = input("Digite o novo nome do fornecedor: ")
    cnpj = input("Digite o novo CNPJ do fornecedor: ")
    telefone = input("Digite o novo telefone do fornecedor: ")
    # Atualiza os dados do fornecedor com o ID informado
    cursor.execute('''
    UPDATE fornecedores
    SET nome = ?, cnpj = ?, telefone = ?
    WHERE id = ?
    ''', (nome, cnpj, telefone, fornecedor_id))
    conexao.commit()  # Salva as alterações no banco de dados
    if cursor.rowcount > 0:
        print("Fornecedor atualizado com sucesso!")  # Confirmação de atualização
    else:
        print("Fornecedor não encontrado.")  # Mensagem se o fornecedor não foi encontrado

# Função para deletar um fornecedor pelo ID
def deletar_fornecedor():
    # Solicita o ID do fornecedor a ser deletado
    fornecedor_id = input("Digite o ID do fornecedor que deseja deletar: ")
    cursor.execute('''
    DELETE FROM fornecedores
    WHERE id = ?
    ''', (fornecedor_id,))  # Deleta o fornecedor com o ID informado
    conexao.commit()  # Salva as alterações no banco de dados
    if cursor.rowcount > 0:
        print("Fornecedor deletado com sucesso!")  # Confirmação de exclusão
    else:
        print("Fornecedor não encontrado.")  # Mensagem se o fornecedor não foi encontrado



# função para registrar alimentos para doação
def registrar_doacao():
    alimento = input("Insira o nome do alimento para doação: ")
    tipo = input("O alimento é vendido por peso ou quantidade? (peso/quantidade): ").strip().lower()

    if tipo == "peso":
        peso = float(input("Insira o peso do alimento (kg): "))
        # Aqui você pode inserir o alimento e o peso no banco de dados ou em uma lista de registros
        print(f"{alimento} de {peso} kg registrado para doação.")
    elif tipo == "quantidade":
        quantidade = int(input("Insira a quantidade do alimento: "))
        print(f"{quantidade} unidades de {alimento} registradas para doação.")
    else:
        print("Tipo inválido. Insira 'peso' ou 'quantidade'.")

# função para registrar alimentos descartados
def registrar_descarte():
    alimento = input("Insira o nome do alimento descartado: ")
    tipo = input("O alimento é vendido por peso ou quantidade? (peso/quantidade): ").strip().lower()

    if tipo == "peso":
        peso = float(input("Insira o peso do alimento (kg): "))
        print(f"{alimento} de {peso} kg registrado como descartado.")
    elif tipo == "quantidade":
        quantidade = int(input("Insira a quantidade do alimento: "))
        print(f"{quantidade} unidades de {alimento} registradas como descartadas.")
    else:
        print("Tipo inválido. Insira 'peso' ou 'quantidade'.")



# Menu principal para interação com o usuário
def loop_menu_crud_fornecedor():
    while True:  # Loop principal do menu, repetido até a opção "Sair" ser escolhida
        # Exibe as opções do menu
        print("\n=== Menu de Fornecedores ===")
        print("1. Cadastrar fornecedor")
        print("2. Listar fornecedores")
        print("3. Atualizar fornecedor")
        print("4. Deletar fornecedor")
        print("5. Voltar")
        
        opcao = input("Escolha uma opção: ")  # Solicita a escolha do usuário
        
        # Executa a função correspondente à opção escolhida
        if opcao == "1":
            cadastrar_fornecedor()
        elif opcao == "2":
            listar_fornecedores()
        elif opcao == "3":
            atualizar_fornecedor()
        elif opcao == "4":
            deletar_fornecedor()
        elif opcao == "5":
            conexao.close()
            fl.limpar()
            return
        else:
            print("Opção inválida. Tente novamente.")  # Mensagem para opção inválida

