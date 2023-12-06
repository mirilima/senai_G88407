# dicionário de itens do menu e preços
menu = {
    'Hambúrguer': 15,
    'milkshakeG': 12,
    'Refri': 4,
    'Batata FritaM': 10,
    'Sobremesa': 14
}
# armazenar o pedido do cliente
pedido = {}
# para exibir o menu
def exibir_menu():

    print("Menu:")
    for item, preco in menu.items():
        print(f" {item}: R${preco} ")
# adicionando um item ao pedido
def adicionar_item():
    item = input("Insira um item do menu: ")
    if item in menu:
        if item in pedido:
            pedido[item] += 1
        else:
            pedido[item] = 1
        print(f"{item} foi adicionado ao pedido.")
    else:
        print("Item não encontrado no menu.")

# para remover um item do pedido
def remover_item():
    item = input("Insira um item do menu para remover: ")
    if item in pedido and pedido[item] > 0:
        pedido[item] -= 1
        print(f"Uma unidade de {item} foi removida do pedido.")
    else:
        print("Item não encontrado no pedido ou quantidade insuficiente.")

# para exibir o pedido
def exibir_pedido():
    print("Pedido:")
    for item, quantidade in pedido.items():
        preco_total = quantidade * menu[item]
        print(f"{item} - Quantidade: {quantidade} - Preço total: R${preco_total}")

# calcular o total do pedido
def calcular_total():
    total = 0
    for item, quantidade in pedido.items():
        total += quantidade * menu[item]
    print(f"Total do pedido: R${total}")
# Menu principal
while True:
    print("\nMenu Principal:\n")
    print("1. Exibir Menu")
    print("2. Adicionar Item ao Pedido")
    print("3. Remover Item do Pedido")
    print("4. Exibir Pedido")
    print("5. Calcular Total do Pedido")
    print("6. Encerrar Pedido e Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        exibir_menu()
    elif opcao == '2':
        adicionar_item()
    elif opcao == '3':
        remover_item()
    elif opcao == '4':
        exibir_pedido()
    elif opcao == '5':
        calcular_total()
    elif opcao == '6':
        print("Encerrando o pedido. Obrigado!")
        break
    else:
        print("Opção inválida. Tente novamente.")