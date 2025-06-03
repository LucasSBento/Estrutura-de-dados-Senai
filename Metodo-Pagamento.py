#Métodos de pagamento
metodos = ["dinheiro", "pix"]

print("Escolha um método de pagamento do salário:")
print(metodos)

escolha = input("Digite o nome do método: ")

if escolha in metodos:
    print("Você escolheu:", escolha)
else:
    print("Método inválido.")
