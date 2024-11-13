from resources import funcaolimpar as fl
from resources import crud_alimentos as ca
from resources import cadastro_de_forn as cf
from resources import tela_estoque as te
from resources import tela_login_v3 as tl
import sqlite3
import hashlib

conexao = sqlite3.connect('hortifruti.db')
cur = conexao.cursor()

# Função para gerar o hash da senha
def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def loop_menu_admin():
    while True:
        print("\n--- Menu Administrador ---")
        print("1 - CRUD alimentos")
        print("2 - CRUD fornecedores")
        print("3 - Atualizar senhas")
        print("4 - Outros sistemas")
        print("5 - Voltar")
        
        escolhamenu = int(input("Insira o comando: "))
        fl.limpar()
        if escolhamenu == 1:
            ca.loop_menu_crud_alimentos()
        elif escolhamenu == 2:
            cf.loop_menu_crud_fornecedor()
        elif escolhamenu == 3:
            loop_menu_senhas()
        elif escolhamenu == 4:
            loop_menu_outros()
        elif escolhamenu == 5:
            conexao.close()
            tl.usuario = None
            return
        else:
            print("Comando inválido, por favor insira um número de 1 a 5.")

# Função para verificar a senha atual e atualizar a senha
def atualizar_senha(usuario):
    senha_atual = input("Digite sua senha atual: ")

    # Conectando ao banco para buscar a senha armazenada do usuário
    cur.execute("SELECT senha FROM usuarios WHERE usuario = ?", (usuario,))
    senha_armazenada = cur.fetchone()[0]
    
    # Verificar se a senha atual corresponde ao hash armazenado
    if gerar_hash(senha_atual) == senha_armazenada:
        # Solicitar nova senha e confirmação
        nova_senha = input("Digite a nova senha: ")
        confirmacao_senha = input("Confirme a nova senha: ")
        
        if nova_senha == confirmacao_senha:
            nova_senha_hash = gerar_hash(nova_senha)
            cur.execute("UPDATE usuarios SET senha = ? WHERE usuario = ?", (nova_senha_hash, usuario))
            conexao.commit()  # Alterado para 'conexao.commit()'
            print("Senha atualizada com sucesso!")
        else:
            print("As senhas não coincidem. Tente novamente.")
    else:
        print("Senha atual incorreta. Tente novamente.")




def loop_menu_outros():
    while True:
        print("\n--- Menu Outros Sistemas ---")
        print("1 - Menu Estoque")
        print("2 - Menu caixa")
        print("3 - Voltar")
        
        escolha = int(input("Escolha uma opção: "))
        fl.limpar()
        
        if escolha == 1:
            te.loop_menu_estoque()
        elif escolha == 2:
            print('Não disponível')
        elif escolha == 3:
            return
        else:
            print("Opção inválida, por favor insira um número de 1 a 3.")

# Menu de atualização de senhas
def loop_menu_senhas():
    while True:
        print("\n--- Menu Atualização de Senhas ---")
        print("1 - Atualizar senha do Admin")
        print("2 - Atualizar senha do Estoque")
        print("3 - Atualizar senha do Caixa")
        print("4 - Voltar")
        
        escolha = int(input("Escolha uma opção: "))
        fl.limpar()
        
        if escolha == 1:
            atualizar_senha('admin')
        elif escolha == 2:
            atualizar_senha('estoque')
        elif escolha == 3:
            atualizar_senha('caixa')
        elif escolha == 4:
            fl.limpar()
            conexao.close()
            tl.usuario = None
            return
        else:
            print("Opção inválida, por favor insira um número de 1 a 4.")




