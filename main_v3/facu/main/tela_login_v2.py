from resources import crud_alimentos as ad
from resources import funcaolimpar as fl
from resources import spinner as sp
import hashlib
import sqlite3
import os
import time
from time import sleep

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

# Conectar ao banco de dados (ele cria o arquivo se não existir)
con = sqlite3.connect("usuarios.db")
cur = con.cursor()

# Criar a tabela de usuários, se não existir
cur.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
)
""")

# Exemplo: Inserir usuários com `INSERT OR IGNORE` para evitar duplicatas
usuarios = [
    ('admin', '123'),
    ('estoque', '123'),
    ('caixa', '123')
]

cur.executemany("INSERT OR IGNORE INTO usuarios (usuario, senha) VALUES (?, ?)", usuarios)

# Confirmar as alterações e fechar a conexão
con.commit()
con.close()
'''''''''

# Função para gerar o hash da senha
def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

# Função para verificar se a senha corresponde ao hash armazenado
def verificar_senha(senha_digitada, senha_armazenada):
    return gerar_hash(senha_digitada) == senha_armazenada

# Função de login com limite de tentativas
def logar():
    for tentativas_usuario in range(3):  # Limite de 3 tentativas para o usuário
        usuario = input('Por favor, insira o usuário: ')
        cur.execute('SELECT senha FROM usuarios WHERE usuario = ?', (usuario,))
        resultado = cur.fetchone()
        
        if resultado:  # Se o usuário existe no banco
            senha_armazenada = resultado[0]
            
            for tentativas_senha in range(3):  # Limite de 3 tentativas para a senha
                senha = input(f'Usuário válido ({usuario}), insira a senha: ')
                
                if verificar_senha(senha, senha_armazenada):
                    print(f'Bem-vindo, {usuario}!')
                    
                    # Ações para cada tipo de usuário
                    if usuario == 'admin':
                        print('Acesso ao menu de administrador.')
                        ad.loop_menu_admin()  # Exemplo de chamada para menu de administrador
                    elif usuario == 'estoque':
                        print('Bem-vindo ao estoque!')
                        return
                    elif usuario == 'caixa':
                        print('Bem-vindo ao caixa!')
                        return
                    return  # Sai do loop se o login for bem-sucedido
                
                # Senha incorreta
                print(f'Senha incorreta. Tentativa {tentativas_senha + 1} de 3.')
            
            # Três tentativas de senha incorreta
            print('Você excedeu o número de tentativas de senha. Tente novamente mais tarde.')
            return  # Bloqueia o login após 3 tentativas de senha incorreta
        
        else:
            print('Usuário inválido, por favor tente novamente.')
    
    # Três tentativas de usuário incorreto
    print('Você excedeu o número de tentativas de login. Tente novamente mais tarde.')

# Exemplo de chamada da função de login
logar()

# Fechando a conexão com o banco de dados
con.close()

'''''''''