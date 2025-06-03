# Cada usuário será representado por uma linha da matriz
usuarios = []

# Coletar dados de 3 usuários como exemplo
for i in range(3):
    print(f"\nDigite os dados do usuário {i+1}:")
    nome = input("Nome: ")
    idade = input("Idade: ")
    email = input("Email: ")

    # Cada usuário é uma lista (linha da matriz)
    usuario = [nome, idade, email]
    usuarios.append(usuario)

# Exibir os dados em formato de matriz
print("\n=== MATRIZ DE USUÁRIOS ===")
print("Nome\tIdade\tEmail")
for usuario in usuarios:
    print(f"{usuario[0]}\t{usuario[1]}\t{usuario[2]}")
