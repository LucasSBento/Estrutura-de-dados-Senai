#lista_de_produtos (adm)

vetor = []
adicionar = input("deseja adicionar uma vaga a lista? s-sim n-não: ")
while (adicionar == "s"):
  adicionando = input("Digite o nome da vaga: ")
  vetor.append(adicionando)
  adicionar = input("deseja adicionar uma vaga a lista? s-sim n-não: ")
vetor.sort()
print(vetor)

#lista_de_produtos (cliente)

import sys
import random
vaga_desejada = input("deseja se candidatar a qual vaga? 1-Pedreiro 2-Programador 3-Engenheiro: ")
if (vaga_desejada == "1"):
  print("Pedreiro")
elif (vaga_desejada == "2"):
  print("Programador")
elif (vaga_desejada == "3"):
  print("Engenheiro")
else:
  sys.exit("vaga não encontrada")
vetor = ["Marcos","Pablo_clone","Pablo","Luiz"]
entrada = input("deseja se candidatar a vaga? s-sim n-não: ")
while (entrada == "s"):
  adicionando = input("Digite o seu nome: ")
  print("inscrição efetuada")
  vetor.append(adicionando)
  break
random.shuffle(vetor)
print("lista de participantes: " ,vetor)
