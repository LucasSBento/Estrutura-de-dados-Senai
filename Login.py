# Lista de usuários (cada usuário é uma tupla: (nome, senha))
usuarios = []

# Variável para armazenar usuário logado
usuario_logado = None

def cadastrar_usuario():
    nome = input("Digite um nome de usuário: ")
    senha = input("Digite uma senha: ")
    usuarios.append((nome, senha))
    print("Usuário cadastrado com sucesso!\n")

def login():
    global usuario_logado
    if usuario_logado:
        print(f"Usuário já está logado: {usuario_logado}\n")
        return

    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if (nome, senha) in usuarios:
        usuario_logado = nome
        print(f"Login bem-sucedido! Bem-vindo, {nome}.\n")
    else:
        print("Usuário ou senha incorretos.\n")

def logout():
    global usuario_logado
    if usuario_logado:
        print(f"Usuário {usuario_logado} saiu com sucesso.\n")
        usuario_logado = None
    else:
        print("Nenhum usuário está logado no momento.\n")

def menu():
    while True:
        print("==== MENU ====")
        print("1. Cadastrar usuário")
        print("2. Login")
        print("3. Logout")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            login()
        elif opcao == '3':
            logout()
        elif opcao == '4':
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida!\n")

# Inicia o programa
menu()
