from collections import deque

# ========== ESTRUTURAS DE DADOS ==========
# Matriz de usuários [nome, idade, email, senha, is_admin]
usuarios = [
    ["admin", "30", "admin@example.com", "admin", True]
]

# Vetor para produtos (vagas)
produtos = []

# Pilha para carrinho (LIFO)
carrinho = []

# Fila para métodos de pagamento (FIFO)
metodos_pagamento = deque(["Dinheiro", "Pix", "Cartão"])

# Variável para controle de login
usuario_logado = None

# ========== SISTEMA DE AUTENTICAÇÃO ==========
def cadastrar_usuario():
    print("\n=== CADASTRO ===")
    novo_usuario = [
        input("Digite um nome de usuário: "),
        input("Digite sua idade: "),
        input("Digite seu email: "),
        input("Digite uma senha: "),
        False  # is_admin
    ]
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!\n")

def login():
    global usuario_logado
    print("\n=== LOGIN ===")
    nome = input("Usuário: ")
    senha = input("Senha: ")

    for user in usuarios:
        if user[0] == nome and user[3] == senha:
            usuario_logado = user
            print(f"\nBem-vindo(a), {nome}!")
            return
    print("\nCredenciais inválidas!")

def logout():
    global usuario_logado
    usuario_logado = None
    print("\nLogout realizado com sucesso!")

# ========== SISTEMA DE VAGAS ==========
def gerenciar_vagas():
    while True:
        print("\n=== GERENCIAR VAGAS ===")
        print("1. Adicionar vaga")
        print("2. Listar vagas")
        print("3. Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            produtos.append(input("Nome da vaga: "))
            print("Vaga adicionada!")
        elif opcao == "2":
            print("\nVagas disponíveis:" if produtos else "\nNenhuma vaga cadastrada")
            for i, vaga in enumerate(produtos, 1):
                print(f"{i}. {vaga}")
        elif opcao == "3":
            break
        else:
            print("Opção inválida!")

# ========== SISTEMA DE CARRINHO ==========
def gerenciar_candidaturas():
    while True:
        print("\n=== CARRINHO DE VAGAS ===")
        print("1. Candidatar-se a vaga")
        print("2. Remover última candidatura")
        print("3. Ver candidaturas")
        print("4. Finalizar inscrições")
        print("5. Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            print("\nVagas disponíveis:")
            for i, vaga in enumerate(produtos, 1):
                print(f"{i}. {vaga}")
            try:
                escolha = int(input("Número da vaga: ")) - 1
                carrinho.append(produtos[escolha])
                print(f"Candidatura para '{produtos[escolha]}' realizada!")
            except:
                print("Seleção inválida!")
        
        elif opcao == "2":
            if carrinho:
                print(f"Candidatura removida: {carrinho.pop()}")
            else:
                print("Carrinho vazio!")
        
        elif opcao == "3":
            print("\nSuas candidaturas:" if carrinho else "\nNenhuma candidatura")
            for vaga in reversed(carrinho):
                print(f"- {vaga}")
        
        elif opcao == "4":
            if not carrinho:
                print("Nenhuma candidatura para processar!")
                continue

            print("\n=== PROCESSO DE INSCRIÇÃO ===")
            while metodos_pagamento:
                metodo = metodos_pagamento.popleft()
                print(f"\nProcessando pagamento via {metodo}...")
                
                print("\n=== RESUMO FINAL ===")
                print("Vagas:", ", ".join(carrinho))
                print("\nDados do Candidato:")
                print(f"Nome: {usuario_logado[0]}")
                print(f"Email: {usuario_logado[2]}")
                print("\nInscrição concluída com sucesso!")
                carrinho.clear()
                return
            
            print("Nenhum método de pagamento disponível!")
        
        elif opcao == "5":
            return
        
        else:
            print("Opção inválida!")

# ========== MENUS ==========
def menu_admin():
    while True:
        print("\n=== PAINEL ADMIN ===")
        print("1. Gerenciar vagas")
        print("2. Ver candidatos")
        print("3. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            gerenciar_vagas()
        elif opcao == "2":
            print("\nCandidatos cadastrados:")
            for user in usuarios:
                print(f"Nome: {user[0]} | Email: {user[2]}")
        elif opcao == "3":
            return
        else:
            print("Opção inválida!")

def menu_usuario():
    while True:
        print("\n=== SISTEMA DE VAGAS ===")
        print("1. Ver vagas disponíveis")
        print("2. Gerenciar candidaturas")
        print("3. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            print("\nVagas disponíveis:" if produtos else "\nNenhuma vaga disponível")
            for i, vaga in enumerate(produtos, 1):
                print(f"{i}. {vaga}")
        elif opcao == "2":
            gerenciar_candidaturas()
        elif opcao == "3":
            return
        else:
            print("Opção inválida!")

def menu_principal():
    while True:
        print("\n=== SISTEMA DE RECRUTAMENTO ===")
        print("1. Login")
        print("2. Cadastrar")
        print("3. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            login()
            if usuario_logado:
                if usuario_logado[4]:  # Acessa is_admin
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

# ========== EXECUÇÃO ==========
if __name__ == "__main__":
    menu_principal()
