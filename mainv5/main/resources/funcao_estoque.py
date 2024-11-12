
# função para registrar alimentos para doação
def registrar_doacao():
    alimento = input("Insira o nome do alimento para doação: ")
    tipo = input("O alimento é vendido por peso ou quantidade? (peso/quantidade): ").strip().lower()

    if tipo == "peso":
        peso = float(input("Insira o peso do alimento (kg): "))
        # Aqui você pode inserir o alimento e o peso no banco de dados ou em uma lista de registros
        print(f"{alimento} de {peso} kg registrado para doação.")
    elif tipo == "quantidade":
        quantidade = int(input("Insira a quantidade do alimento: "))
        print(f"{quantidade} unidades de {alimento} registradas para doação.")
    else:
        print("Tipo inválido. Insira 'peso' ou 'quantidade'.")

# função para registrar alimentos descartados
def registrar_descarte():
    alimento = input("Insira o nome do alimento descartado: ")
    tipo = input("O alimento é vendido por peso ou quantidade? (peso/quantidade): ").strip().lower()

    if tipo == "peso":
        peso = float(input("Insira o peso do alimento (kg): "))
        print(f"{alimento} de {peso} kg registrado como descartado.")
    elif tipo == "quantidade":
        quantidade = int(input("Insira a quantidade do alimento: "))
        print(f"{quantidade} unidades de {alimento} registradas como descartadas.")
    else:
        print("Tipo inválido. Insira 'peso' ou 'quantidade'.")