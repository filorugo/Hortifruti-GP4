from resources import tela_admin as ta
from resources import funcaolimpar as fl
from resources import tela_estoque as te
from resources import siscaixa1 as fc
import hashlib
import sqlite3


# Função de limpeza de tela
def limpar_tela():
    fl.limpar()

# Exibindo o banner de login
def exibir_banner():
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
    
# Conectando ao banco de dados
def conectar_db():
    con = sqlite3.connect("hortifruti.db")
    cur = con.cursor()

    # Criando a tabela de usuários, se não existir
    cur.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        usuario TEXT PRIMARY KEY,
        senha TEXT NOT NULL
    )
    """)
    return con, cur

# Função para gerar o hash da senha
def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

# Função para verificar a senha
def verificar_senha(senha_digitada, senha_armazenada):
    senha_hash_digitada = gerar_hash(senha_digitada)
    return senha_hash_digitada == senha_armazenada

# Função de login
def logar():
    # Exibe o banner inicial
    exibir_banner()
    
    # Conectando ao banco de dados
    con, cur = conectar_db()
    
    for tentativas_usuario in range(3):  # Limite de 3 tentativas para o usuário
        usuario = input('Por favor, insira o usuário: ')
        cur.execute('SELECT senha FROM usuarios WHERE usuario = ?', (usuario,))
        resultado = cur.fetchone()
        
        if resultado:  # Se o usuário existe no banco
            senha_armazenada = resultado[0]
            
            for tentativas_senha in range(3):  # Limite de 3 tentativas para a senha
                senha = input(f'Usuário válido ({usuario}), insira a senha: ')
                
                if verificar_senha(senha, senha_armazenada):
                    print(f'Bem-vindo, {usuario}!\n')
                    
                    # Ações para cada tipo de usuário
                    if usuario == 'admin':
                        ta.loop_menu_admin()  # Exemplo de chamada para menu de administrador
                    elif usuario == 'estoque':
                        te.loop_menu_estoque()  # Exemplo de chamada para menu de estoque
                    elif usuario == 'caixa':
                        fc.loop_menu_caixa()
                    return  # Sai do loop de login
                # Senha incorreta
                print(f'Senha incorreta. Tentativa {tentativas_senha + 1} de 3.')
            
            # Excede o número de tentativas de senha incorretas
            print('Você excedeu o número de tentativas de senha. Tente novamente mais tarde.')
            return  # Bloqueia o login após 3 tentativas de senha incorreta
        
        else:
            print('Usuário inválido, por favor tente novamente.')
    
    # Excede o número de tentativas de usuário incorretos
    print('Você excedeu o número de tentativas de login. Tente novamente mais tarde.')
    # Fechando a conexão com o banco de dados
    con.close()

# Executa a função de login
logar()

