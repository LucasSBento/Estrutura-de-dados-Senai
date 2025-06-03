#Métodos de pagamento
metodos = ["dinheiro", "pix", "cartão"]

print("Escolha um método de pagamento do salário:")
print(metodos)

escolha = input("Digite o nome do método: ")

if escolha in metodos:
    print("Você escolheu:", escolha)
else:
    print("Método inválido.")



from collections import deque

# Criando a fila de métodos de pagamento
metodos = deque(["dinheiro", "pix", "cartão"])

print("Fila de métodos de pagamento disponíveis:")
print(list(metodos))

# Simulando a escolha do primeiro método da fila (FIFO)
if metodos:
    escolhido = metodos.popleft()  # Remove o primeiro da fila
    print("Método de pagamento processado:", escolhido)
else:
    print("Nenhum método disponível na fila.")
