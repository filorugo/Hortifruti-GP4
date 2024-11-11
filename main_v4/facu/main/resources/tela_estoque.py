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

