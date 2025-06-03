#Carrinho_de_compras
carrinho = []

def add():
    nome = input("Digite o nome do item que deseja adicionar: ")
    carrinho.append(nome)
    print("Item",nome, "adicionado ao carrinho.")

def remover():
    if not carrinho:
        print("A pilha está vazia. Nenhum item para remover.")
    else:
        removido = carrinho.pop()
        print("Item",removido,"removido do carrinho.")

def listar():
    if not carrinho:
        print("O carrinho está vazio.")
    else:
        print("Itens do carrinho:")
        for i, item in enumerate(reversed(carrinho), start=1):
            print(i,item)

def esvaziar():
    carrinho.clear()
    print("O carrinho foi esvaziado com sucesso!")

def menu():
    while True:
        print("\n=== MENU DO CARRINHO ===")
        print("1 - Adicionar item ")
        print("2 - Remover último item")
        print("3 - Listar itens")
        print("4 - Esvaziar carrinho")
        print("5 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            add()
        elif opcao == "2":
            remover()
        elif opcao == "3":
            listar()
        elif opcao == "4":
            esvaziar()
        elif opcao == "5":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
menu()
