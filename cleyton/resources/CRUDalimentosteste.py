from resources import funcaolimpar as fl
# CRUD de Alimentos
alimentos = {}

# funcao que adiciona um alimento na lista, e verifica se o nome já foi cadastrado
def cadastrar_alimentos():
    while True:
        nome = input("Digite o nome do alimento: ")
        fl.limpar()
        tipo = input("O alimento é vendido por peso ou por unidade? (peso/unidade): ").strip().lower()
        fl.limpar()
        if tipo == "unidade":
            valor = float(input("Digite o valor de cada unidade: ").replace(",", "."))
        elif tipo == "peso":
            valor = float(input("Digite o valor por quilo: ").replace(",", "."))
            fl.limpar()
        else:
            print("Tipo inválido. Por favor, insira 'peso' ou 'unidade'.")
            continue
        if nome in alimentos:
            print("Alimento já cadastrado.")
        else:
            alimentos[nome] = {'tipo': tipo, 'valor': valor}
            print(f"Alimento '{nome}' cadastrado com sucesso.")
            adicionar_mais = input("Deseja adicionar mais um alimento? (s/n): ").strip().lower()
            fl.limpar()
            if adicionar_mais != 's':
                break

# funcao que busca e imprime todos os alimentos cadastrados, junto com seus atributos
def ler_alimento():
    if alimentos:
        for nome, dados in alimentos.items():
            tipo = "Peso" if dados['tipo'] == "peso" else "Unidade"
            print(f"Nome: {nome}, Vendido por: {tipo}, Valor: R${dados['valor']:.2f}")
    else:
        print("Nenhum alimento cadastrado.")

# funcao que atualiza atributos de alimentos já cadastrados
def atualizar_alimento():
    nome = input("Digite o nome do alimento que deseja atualizar: ")
    fl.limpar()
    alimento = alimentos.get(nome)
    
    if alimento:
        tipo = input("Digite o novo tipo (peso/unidade) ou pressione Enter para manter o atual: ").strip().lower()
        fl.limpar()
        if tipo == "":
            tipo = None  # Não atualiza o tipo se o usuário deixar em branco
        
        valor_str = input("Digite o novo valor ou pressione Enter para manter o atual: ").replace(",", ".")
        if valor_str:
            valor = float(valor_str)
        else:
            valor = None  # Não atualiza o valor se o usuário deixar em branco
        if tipo:
            alimento['tipo'] = tipo
        if valor is not None:
            alimento['valor'] = valor
        
        print(f"Alimento '{nome}' atualizado com sucesso.")
        fl.limpar()
    else:
        print("Alimento não encontrado.")

# funcao que acessa a lista de alimentos com o nome e o deleta
def deletar_alimento():
    nome = input("Digite o nome do alimento que deseja deletar: ")
    if nome in alimentos:
        del alimentos[nome]
        print(f"Alimento '{nome}' deletado com sucesso.")
        fl.limpar()
    else:
        print("Alimento não encontrado.")

# Menu principal
def loop_menu_admin():
    while True:
        print("\n--- Menu CRUD de Alimentos ---")
        print("1 - Cadastrar Alimentos")
        print("2 - Ler Alimento")
        print("3 - Atualizar Alimento")
        print("4 - Deletar Alimento")
        print("5 - Sair")
        
        escolhamenu = int(input("Insira o comando: "))
        fl.limpar()
        if escolhamenu == 1:
            cadastrar_alimentos()
        elif escolhamenu == 2:
            ler_alimento()
        elif escolhamenu == 3:
            atualizar_alimento()
        elif escolhamenu == 4:
            deletar_alimento()
        elif escolhamenu == 5:
            print("Saindo do sistema...")
            break
        else:
            print("Comando inválido, por favor insira um número de 1 a 5.")


# funcoes: `ler_alimento`, `cadastrar alimentos`, `deletar alimentos` `atualizar_alimento` e `loop_menu_admin`.
