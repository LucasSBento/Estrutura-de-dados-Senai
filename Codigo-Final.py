from collections import deque

# ========== ESTRUTURAS DE DADOS ==========
# Matriz de usuários [nome, idade, email, senha, is_admin]
usuarios = [
    ["admin", "17", "admin@example.com", "admin", True]
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
        False
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

# ========== SISTEMA DE MÉTODOS DE PAGAMENTO ==========
def gerenciar_metodos_pagamento():
    while True:
        print("\n=== GERENCIAR MÉTODOS DE PAGAMENTO ===")
        print("1. Adicionar método de pagamento")
        print("2. Listar métodos de pagamento")
        print("3. Remover método de pagamento")
        print("4. Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            novo_metodo = input("Digite o nome do novo método de pagamento: ").strip()
            if novo_metodo:
                metodos_pagamento.append(novo_metodo)
                print(f"Método '{novo_metodo}' adicionado com sucesso!")
            else:
                print("Nome inválido!")
        elif opcao == "2":
            if metodos_pagamento:
                print("\nMétodos de pagamento disponíveis (ordem de uso):")
                for i, metodo in enumerate(metodos_pagamento, 1):
                    print(f"{i}. {metodo}")
            else:
                print("Nenhum método de pagamento cadastrado!")
        elif opcao == "3":
            if not metodos_pagamento:
                print("Nenhum método de pagamento para remover!")
                continue
            print("\nMétodos de pagamento disponíveis:")
            for i, metodo in enumerate(metodos_pagamento, 1):
                print(f"{i}. {metodo}")
            try:
                escolha = int(input("Número do método para remover: ")) - 1
                if 0 <= escolha < len(metodos_pagamento):
                    removido = metodos_pagamento[escolha]
                    # Como deque não suporta remoção por índice diretamente, convertemos para lista temporariamente
                    temp = list(metodos_pagamento)
                    temp.pop(escolha)
                    metodos_pagamento.clear()
                    metodos_pagamento.extend(temp)
                    print(f"Método '{removido}' removido com sucesso!")
                else:
                    print("Número inválido!")
            except:
                print("Entrada inválida!")
        elif opcao == "4":
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
            if not produtos:
                print("Nenhuma vaga disponível para candidatura!")
                continue
            print("\nVagas disponíveis:")
            for i, vaga in enumerate(produtos, 1):
                print(f"{i}. {vaga}")
            try:
                escolha = int(input("Número da vaga: ")) - 1
                if 0 <= escolha < len(produtos):
                    carrinho.append(produtos[escolha])
                    print(f"Candidatura para '{produtos[escolha]}' realizada!")
                else:
                    print("Seleção inválida!")
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

            if not metodos_pagamento:
                print("Nenhum método de pagamento disponível! Contate o administrador.")
                continue

            print("\n=== PROCESSO DE INSCRIÇÃO ===")
            print("Escolha o método de pagamento disponível:")
            for i, metodo in enumerate(metodos_pagamento, 1):
                print(f"{i}. {metodo}")
            try:
                escolha = int(input("Número do método de pagamento: ")) - 1
                if 0 <= escolha < len(metodos_pagamento):
                    metodo = metodos_pagamento[escolha]
                    # Remove o método escolhido da fila
                    temp = list(metodos_pagamento)
                    temp.pop(escolha)
                    metodos_pagamento.clear()
                    metodos_pagamento.extend(temp)

                    print(f"\nProcessando pagamento via {metodo}...")

                    print("\n=== RESUMO FINAL ===")
                    print("Vagas:", ", ".join(carrinho))
                    print("\nDados do Candidato:")
                    print(f"Nome: {usuario_logado[0]}")
                    print(f"Email: {usuario_logado[2]}")
                    print("\nInscrição concluída com sucesso!")
                    carrinho.clear()
                else:
                    print("Método de pagamento inválido!")
            except:
                print("Entrada inválida!")

        elif opcao == "5":
            return

        else:
            print("Opção inválida!")

# ========== MENUS ==========
def menu_admin():
    while True:
        print("\n=== PAINEL ADMIN ===")
        print("1. Gerenciar vagas")
        print("2. Gerenciar métodos de pagamento")
        print("3. Ver candidatos")
        print("4. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            gerenciar_vagas()
        elif opcao == "2":
            gerenciar_metodos_pagamento()
        elif opcao == "3":
            print("\nCandidatos cadastrados:")
            for user in usuarios:
                print(f"Nome: {user[0]} | Email: {user[2]}")
        elif opcao == "4":
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
