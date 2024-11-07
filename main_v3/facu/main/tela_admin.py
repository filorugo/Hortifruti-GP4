from resources import funcaolimpar as fl
from resources import loop_menu_crud_alimentos
from resources import loop_menu_crud_fornecedor
import sqlite3
import time
from time import sleep

# Menu administrador
def loop_menu_admin():
    while True:
        print("\n--- Menu Administrador ---")
        print("1 - CRUD alimentos")
        print("2 - CRUD fornecedores")
        print("3 - Atualizar senhas")
        print("4 - Outros sistemas")
        print("5 - Sair")
        
        escolhamenu = int(input("Insira o comando: "))
        fl.limpar()
        if escolhamenu == 1:
            loop_menu_crud_alimentos()
        elif escolhamenu == 2:
            loop_menu_crud_fornecedor()
        elif escolhamenu == 3:
            atualizar_alimento()
        elif escolhamenu == 4:
            deletar_alimento()
        elif escolhamenu == 5:
            print("Saindo do sistema...")
            return
        else:
            print("Comando inválido, por favor insira um número de 1 a 5.")

# Menu administrador
def loop_menu_senhas():
    while True:
        print("\n--- Menu Atualização de senhas ---")
        print("1 - Atualizar senha do Admin")
        print("2 - Atualizar senha do Estoque")
        print("3 - Atualizar senha do Caixa")
        print("4 - Voltar")
        
        escolhamenu = int(input("Insira o comando: "))
        fl.limpar()
        if escolhamenu == 1:
            loop_menu_crud_alimentos()
        elif escolhamenu == 2:
            loop_menu_crud_fornecedor()
        elif escolhamenu == 3:
            atualizar_alimento()
        elif escolhamenu == 4:
            deletar_alimento()
        elif escolhamenu == 5:
            print("Saindo do sistema...")
            break
        else:
            print("Comando inválido, por favor insira um número de 1 a 5.")
