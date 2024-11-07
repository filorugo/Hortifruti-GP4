from resources import CRUDalimentosteste as ad
from resources import funcaolimpar as fl
import hashlib
import sqlite3
import os


print("""
      

                                     __.....__    /|                  
                                 .-''         '.  ||                  
                                /     .-''"'-.  `.||                  
                               /     /________\   ||  __       __     
                               |                  ||/'__ '. .:--.'.   
                               \    .-------------|:/`  '. / |   \ |  
                                \    '-.____...---||     | `" __ | |  
                                 `.             .'||\    / '.'.''| |  
                                   `''-...... -'  |/\'..' // /   | |_ 
                                                  '  `'-'` \ \._,\ '/ 
                                                            `--'  `"  
 _____                                                                                                  _____ 
( ___ )                                                                                                ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   |  ___                             ___              .-.                             ___            |   | 
 |   | (   )                           (   )      .-.   /    \                          (   )      .-.  |   | 
 |   |  | | .-.     .--.    ___ .-.     | |_     ( __)  | .`. ;   ___ .-.     ___  ___   | |_     ( __) |   | 
 |   |  | |/   \   /    \  (   )   \   (   __)   (''")  | |(___) (   )   \   (   )(   ) (   __)   (''") |   | 
 |   |  |  .-. .  |  .-. ;  | ' .-. ;   | |       | |   | |_      | ' .-. ;   | |  | |   | |       | |  |   | 
 |   |  | |  | |  | |  | |  |  / (___)  | | ___   | |  (   __)    |  / (___)  | |  | |   | | ___   | |  |   | 
 |   |  | |  | |  | |  | |  | |         | |(   )  | |   | |       | |         | |  | |   | |(   )  | |  |   | 
 |   |  | |  | |  | |  | |  | |         | | | |   | |   | |       | |         | |  | |   | | | |   | |  |   | 
 |   |  | |  | |  | '  | |  | |         | ' | |   | |   | |       | |         | |  ; '   | ' | |   | |  |   | 
 |   |  | |  | |  '  `-' /  | |         ' `-' ;   | |   | |       | |         ' `-'  /   ' `-' ;   | |  |   | 
 |   | (___)(___)  `.__.'  (___)         `.__.   (___) (___)     (___)         '.__.'     `.__.   (___) |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                                                                                (_____)

      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
""")



# definindo os usuarios e suas senhas
usuarios_senhas = {
    'admin': '123',
    'estoque': '123',
    'caixa': '123',

}

# funcao de login que valida o usuario e a senha
def logar():
    for tentativas in range(3):  # Limite de 3 tentativas para o usuário
        usuario = input('Por favor, insira o usuário: ')
        
        if usuario in usuarios_senhas:
            for tentativas_senha in range(3):  # Limite de 3 tentativas para a senha
                senha = input(f'Usuário válido ({usuario}), insira a senha: ')
                if senha == usuarios_senhas[usuario]:
                    print(f'Bem-vindo, {usuario}!')
                    
                    # Ações para cada tipo de usuário
                    if usuario == 'admin':
                        # Ação específica para o admin
                        print('Acesso ao menu de administrador.')
                        ad.loop_menu_admin()
                    elif usuario == 'estoque':
                        # Ação específica para o estoque
                        print('Bem-vindo ao estoque!')
                        return
                    elif usuario == 'caixa':
                        # Ação específica para o caixa
                        print('Bem-vindo ao caixa!')
                        return
                
                # Senha incorreta
                print(f'Senha incorreta. Tentativa {tentativas_senha + 1} de 3.')
            
            # Se as três tentativas de senha falharem
            print('Você excedeu o número de tentativas de senha. Tente novamente mais tarde.')
            return
        else:
            print('Usuário inválido, por favor tente novamente.')
    
    # Se as três tentativas de usuário falharem
    print('Você excedeu o número de tentativas de login. Tente novamente mais tarde.')

# roda a funcao de login
logar()
