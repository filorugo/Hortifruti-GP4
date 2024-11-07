from resources import funcaolimpar as fl
import time
from time import sleep
import sqlite3

# Menu administrador
def loop_menu_admin():
    while True:
        print("\n--- Menu Estoque ---")
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
            break
        else:
            print("Comando inválido, por favor insira um número de 1 a 5.")

