# CRUD de Fornecedores

fornecedores = {}

def criar_fornecedor(id, nome, telefone):
    if id in fornecedores:
        print("Fornecedor já cadastrado.")
    else:
        fornecedores[id] = {'nome': nome, 'telefone': telefone}
        print("Fornecedor cadastrado com sucesso.")

def ler_fornecedor(id):
    fornecedor = fornecedores.get(id)
    if fornecedor:
        print(f"ID: {id}, Nome: {fornecedor['nome']}, Telefone: {fornecedor['telefone']}")
    else:
        print("Fornecedor não encontrado.")

def atualizar_fornecedor(id, nome=None, telefone=None):
    fornecedor = fornecedores.get(id)
    if fornecedor:
        if nome:
            fornecedor['nome'] = nome
        if telefone:
            fornecedor['telefone'] = telefone
        print("Fornecedor atualizado com sucesso.")
    else:
        print("Fornecedor não encontrado.")

def deletar_fornecedor(id):
    if id in fornecedores:
        del fornecedores[id]
        print("Fornecedor deletado com sucesso.")
    else:
        print("Fornecedor não encontrado.")

# Exemplo de uso
criar_fornecedor(1, "Fornecedor A", "123456789")
ler_fornecedor(1)
atualizar_fornecedor(1, telefone="987654321")
ler_fornecedor(1)
deletar_fornecedor(1)
ler_fornecedor(1)