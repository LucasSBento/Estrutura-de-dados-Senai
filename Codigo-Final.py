from collections import deque

# ========== ESTRUTURAS GLOBAIS ==========
usuarios = [{
    "nome": "admin",
    "idade": "30",
    "email": "admin@example.com",
    "senha": "admin",
    "is_admin": True
}]
usuario_logado = None
produtos = []
metodos_pagamento = deque(["Dinheiro", "Pix", "Cartão"])

# ========== FUNÇÕES DE AUTENTICAÇÃO ==========
def cadastrar_usuario():
    print("\n=== CADASTRO ===")
    nome = input("Digite um nome de usuário: ")
    idade = input("Digite sua idade: ")
    email = input("Digite seu email: ")
    senha = input("Digite uma senha: ")
    
    usuarios.append({
        "nome": nome,
        "idade": idade,
        "email": email,
        "senha": senha,
        "is_admin": False
    })
    print("Usuário cadastrado com sucesso!\n")

def login():
    global usuario_logado
    print("\n=== LOGIN ===")
    nome = input("Usuário: ")
    senha = input("Senha: ")

    for usuario in usuarios:
        if usuario["nome"] == nome and usuario["senha"] == senha:
            usuario_logado = usuario
            print(f"\nBem-vindo(a), {nome}!")
            return
    print("\nCredenciais inválidas!")

def logout():
    global usuario_logado
    usuario_logado = None
    print("\nLogout realizado com sucesso!")

# ========== SISTEMA DE PRODUTOS ==========
def gerenciar_produtos():
    while True:
        print("\n=== GERENCIAR VAGAS ===")
        print("1. Adicionar vaga")
        print("2. Listar vagas")
        print("3. Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            novo_produto = input("Nome da vaga: ")
            produtos.append(novo_produto)
            print(f"'{novo_produto}' adicionado!")
        elif opcao == "2":
            print("\nVagas disponíveis:")
            for idx, item in enumerate(produtos, 1):
                print(f"{idx}. {item}")
        elif opcao == "3":
            break
        else:
            print("Opção inválida!")

# ========== SISTEMA DE CARRINHO ==========
def gerenciar_carrinho():
    carrinho = []
    while True:
        print("\n=== CARRINHO ===")
        print("1. Adicionar vaga")
        print("2. Remover última vaga")
        print("3. Ver carrinho")
        print("4. Finalizar compra")
        print("5. Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            print("\nVagas disponíveis:")
            for idx, item in enumerate(produtos, 1):
                print(f"{idx}. {item}")
            try:
                escolha = int(input("Número da vaga: ")) - 1
                carrinho.append(produtos[escolha])
                print(f"{produtos[escolha]} adicionado!")
            except:
                print("Erro na seleção!")
        
        elif opcao == "2":
            if carrinho:
                print(f"{carrinho.pop()} removido!")
            else:
                print("Carrinho vazio!")
        
        elif opcao == "3":
            print("\nSeu carrinho:")
            for item in carrinho:
                print(f"- {item}")
        
        elif opcao == "4":
            if not carrinho:
                print("Carrinho vazio!")
                continue
                
            print("\n=== PAGAMENTO ===")
            print("Métodos disponíveis:", list(metodos_pagamento))
            
            if metodos_pagamento:
                metodo = metodos_pagamento.popleft()
                print(f"\nPagamento com {metodo} aprovado!")
                
                print("\n=== RESUMO DA COMPRA ===")
                for item in carrinho:
                    print(f"- {item}")
                
                print("\n=== DADOS DO CLIENTE ===")
                print(f"Nome: {usuario_logado['nome']}")
                print(f"Email: {usuario_logado['email']}")
                print("\nObrigado pela compra!")
                return
            else:
                print("Nenhum método disponível!")
        
        elif opcao == "5":
            return
        
        else:
            print("Opção inválida!")

# ========== MENUS PRINCIPAIS ==========
def menu_admin():
    while True:
        print("\n=== PAINEL ADMIN ===")
        print("1. Gerenciar vagas")
        print("2. Ver usuários cadastrados")
        print("3. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            gerenciar_produtos()
        elif opcao == "2":
            print("\nUsuários cadastrados:")
            for user in usuarios:
                print(f"Nome: {user['nome']} | Email: {user['email']}")
        elif opcao == "3":
            return
        else:
            print("Opção inválida!")

def menu_usuario():
    while True:
        print("\n=== LOJA VIRTUAL ===")
        print("1. Ver vagas")
        print("2. Carrinho")
        print("3. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            print("\nVagas disponíveis:")
            for idx, item in enumerate(produtos, 1):
                print(f"{idx}. {item}")
        elif opcao == "2":
            gerenciar_carrinho()
        elif opcao == "3":
            return
        else:
            print("Opção inválida!")

def menu_principal():
    while True:
        print("\n=== SISTEMA DE COMPRAS ===")
        print("1. Login")
        print("2. Cadastrar")
        print("3. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            login()
            if usuario_logado:
                if usuario_logado["is_admin"]:
                    menu_admin()
                else:
                    menu_usuario()
                logout()
        elif opcao == "2":
            cadastrar_usuario()
        elif opcao == "3":
            print("\nSistema encerrado!")
            return
        else:
            print("Opção inválida!")

# ========== INICIO DO SISTEMA ==========
if __name__ == "__main__":
    menu_principal()
