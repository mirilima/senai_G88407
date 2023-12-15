conta = {
    "saldo":5008,
    "saldo":5088,
    "saldo":5048,
    "saldo":5028
}
valor = conta

def exibir_menu():

    print("Menu:")
    for item,menu in menu.items():
        print(f"{item} ")

def entrar_conta():
    numero = input("Digite o numero da sua conta: ")
    senha = input("Digite a senha: ")
    if numero in conta and numero[conta] == senha:
        print("Bem vindo")
    else:
        print("Numero da conta ou senha incorretos.")

def escolher_a_operação():
    operacao = input("Insira uma operação do menu: ")
    if operacao in operacao:
        if operacao in conta:
           valor[conta]
        else:
            valor[conta]
        print(f"{operacao} foi realizado.")
    else:
        print("operação não encontrado no menu.")

def depositar_dinheiro():
    print("digite o valor a ser depositado\n")
    input("valor:\n")
    print("insira o envelope com o valor na maquina e aguarde\n")
    print("deposito feito com sucesso")

def verificar_saldo():
    total = {}
    for saldo, saldo in conta.items():
        total = saldo
    print(f"Total em conta: R${total}")

def sacar_dinheiro():
    print("qual valor gostaria de sacar:\n")
    input("valor a ser sacado\n")
    print("saque realizado")

while True:
  
    print("\n Menu Principal:\n")
    print("1. verificar Saldo")
    print("2. depositar dinhriro")
    print("3. sacar Dinheiro")
    print("4. sair")
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        verificar_saldo ()
    elif opcao == '2':
        depositar_dinheiro()
    elif opcao == '3':
       sacar_dinheiro()
    elif opcao == '4':
        print("Encerrando operação. Obrigado!")
        break
    else:
        print("Operação inválida. Tente novamente.")