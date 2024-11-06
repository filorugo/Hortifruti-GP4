import sqlite3  # Importa o módulo sqlite3 para manipulação do banco de dados SQLite

# Conecta ao banco de dados 'estoque.db' e cria a tabela de produtos se ainda não existir
conexao = sqlite3.connect("estoque.db")  # Estabelece a conexão com o banco de dados 'estoque.db'
cursor = conexao.cursor()  # Cria um cursor para executar comandos SQL
cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome TEXT NOT NULL, 
        quantidade INTEGER NOT NULL, 
        preco REAL NOT NULL  
    )
''')  # Cria a tabela 'produtos' com as colunas especificadas, caso ela ainda não exista
conexao.commit()  # Confirma (commita) as alterações no banco de dados
conexao.close()  # Fecha a conexão com o banco de dados após criar a tabela

# Função para adicionar um produto ao banco de dados
def adicionar_produto(nome, quantidade, preco):
    conexao = sqlite3.connect("estoque.db")  # Abre uma nova conexão com o banco de dados
    cursor = conexao.cursor()  # Cria um cursor para executar comandos SQL
    cursor.execute('''
    INSERT INTO produtos (nome, quantidade, preco)
    VALUES (?, ?, ?)
    ''', (nome, quantidade, preco))  # Insere um novo produto com os valores fornecidos
    conexao.commit()  # Confirma as alterações no banco de dados
    conexao.close()  # Fecha a conexão com o banco de dados

# Função para listar todos os produtos cadastrados
def listar_produtos():
    conexao = sqlite3.connect("estoque.db")  # Abre uma nova conexão com o banco de dados
    cursor = conexao.cursor()  # Cria um cursor para executar comandos SQL
    cursor.execute('SELECT * FROM produtos')  # Seleciona todos os registros da tabela 'produtos'
    produtos = cursor.fetchall()  # Recupera todos os registros selecionados
    for produto in produtos:  # Itera sobre cada produto
        print(f"ID: {produto[0]} | Nome: {produto[1]}  | Quantidade: {produto[2]} | Preço: {produto[3]}")
    conexao.close()  # Fecha a conexão com o banco de dados

# Função para atualizar a quantidade de um produto específico
def atualizar_quantidade(id_produto, nova_quantidade):
    conexao = sqlite3.connect("estoque.db")  # Abre uma nova conexão com o banco de dados
    cursor = conexao.cursor()  # Cria um cursor para executar comandos SQL
    cursor.execute('''
        UPDATE produtos
        SET quantidade = ?
        WHERE id = ?
    ''', (nova_quantidade, id_produto))  # Atualiza a quantidade do produto com o 'id' especificado
    conexao.commit()  # Confirma as alterações no banco de dados
    conexao.close()  # Fecha a conexão com o banco de dados

# Função para remover um produto específico do banco de dados
def remover_produto(id_produto):
    conexao = sqlite3.connect("estoque.db")  # Abre uma nova conexão com o banco de dados
    cursor = conexao.cursor()  # Cria um cursor para executar comandos SQL
    cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))  # Deleta o produto com o 'id' especificado
    conexao.commit()  # Confirma as alterações no banco de dados
    conexao.close()  # Fecha a conexão com o banco de dados

# Função de menu interativo para o usuário
def menu():
    while True:  # Loop infinito para exibir o menu até que o usuário escolha sair
        print("\nSistema de Estoque")
        print("1. Adicionar Produtos")
        print("2. Listar Produtos")
        print("3. Atualizar Quantidade")
        print("4. Remover Produto")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")  # Recebe a escolha do usuário

        # Verifica qual opção foi selecionada e chama a função correspondente
        if escolha == "1":
            nome = input("Nome do Produto: ")  # Recebe o nome do produto
            quantidade = int(input("Quantidade: "))  # Recebe a quantidade do produto
            preco = float(input("Preço: "))  # Recebe o preço do produto
            adicionar_produto(nome, quantidade, preco)  # Chama a função para adicionar o produto
        elif escolha == "2":
            listar_produtos()  # Chama a função para listar todos os produtos
        elif escolha == "3":
            id_produto = int(input("ID do produto: "))  # Recebe o ID do produto a ser atualizado
            nova_quantidade = int(input("Nova quantidade: "))  # Recebe a nova quantidade
            atualizar_quantidade(id_produto, nova_quantidade)  # Chama a função para atualizar a quantidade
        elif escolha == "4":
            id_produto = int(input("ID do produto: "))  # Recebe o ID do produto a ser removido
            remover_produto(id_produto)  # Chama a função para remover o produto
        elif escolha == "5":
            break  # Sai do loop se o usuário escolher a opção de sair
        else:
            print("Opção Inválida")  # Informa o usuário caso a opção seja inválida

# Executa o menu interativo para o usuário
menu()
