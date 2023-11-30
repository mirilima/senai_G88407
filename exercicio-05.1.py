#usuarios
usuarios ={}
usuario = input("insira seu usuario:\n")
senha = input("insira sua senha:\n")

#cadastro de usuarios

def novos_usuarios():
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    usuarios[nome] = senha
    print("Usuário cadastrado com sucesso!")

    # login

def fazer_login():
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    if nome in usuarios and usuarios[nome] == senha:
        print("Login bem-sucedido!")
    else:
        print("Nome de usuário ou senha incorretos.")

        # menu principal
        
while True:
    print("Menu Principal:")
    print("1. Criar novo usuário")
    print("2. Fazer login")
    print("3. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        novos_usuarios()

    elif escolha == "2":
        fazer_login()

    elif escolha == "3":
        print("Saindo do programa. Até mais!")
        break # para sair do loop

    else:
        print("Opção inválida. Escolha novamente.")
