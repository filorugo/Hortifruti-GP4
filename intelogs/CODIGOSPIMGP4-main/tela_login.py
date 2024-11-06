print("""
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
print()
print()
print()
print()
print()
# Definindo os usuários e suas respectivas senhas para fins de teste
usuarios_senhas = {
    'admin': 'admin123',
    'caixa': 'caixa123',
    'estoque': 'estoque123',
    'caixa2': 'caixa2123',
    'caixa3': 'caixa3123'
}

# Função de login que valida o usuário e a senha
def logar(usuario):
    if usuario in usuarios_senhas:
        senha = input('Usuário válido, insira a senha: ')
        if senha == usuarios_senhas[usuario]:
            print(f'Bem-vindo, {usuario}!')
        else:
            print('Senha incorreta. Tente novamente.')
    else:
        print('Usuário inválido, por favor tente novamente.')

# Solicitando o nome de usuário
usuario = input('Por favor, insira o usuário: ')
logar(usuario)



