#lista_de_produtos (adm)

vetor = []
adicionar = input("deseja adicionar uma vaga a lista? s-sim n-não: ")
while (adicionar == "s"):
  adicionando = input("Digite o nome da vaga: ")
  vetor.append(adicionando)
  adicionar = input("deseja adicionar uma vaga a lista? s-sim n-não: ")
vetor.sort()
print(vetor)

