#Carrinho_de_compras
carrinho = []

def add():
    nome = input("Digite o nome do item que deseja adicionar: ")
    carrinho.append(nome)
    print("Vaga",nome, "adicionada ao candidato.")

def remover():
    if not carrinho:
        print("A pilha está vazia. Nenhuma vaga para remover.")
    else:
        removido = carrinho.pop()
        print("Vaga",removido,"removida da candidatação.")

def listar():
    if not carrinho:
        print("A candidatação está vazia.")
    else:
        print("Vagas do candidato:")
        for i, item in enumerate(reversed(carrinho), start=1):
            print(i,item)

def esvaziar():
    carrinho.clear()
    print("As candidatações foram esvaziadas com sucesso!")

def menu():
    while True:
        print("\n=== MENU DO CANDIDATO ===")
        print("1 - Candidatar vaga ")
        print("2 - Remover último candidatação")
        print("3 - Listar candidaturas")
        print("4 - Esvaziar candidatações")
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

