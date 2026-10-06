# BLOCO 1: FUNÇÕES
def l():
    print("-=" * 40)

def e():
    print()


# BLOCO 2: VARIÁVEIS
nome_da_padaria = "Padaria Mel de Abelha"

produtos = {
    "PÃO FRANCÊS": 3.63,
    "BAGUETE": 5.73,
    "SONHO": 9.42,
    "PÃO DE QUEIJO": 1.54,
    "MISTO QUENTE": 3.56
}

viagem_custo = 9.87


# BLOCO 3: IDENTIFICAÇÃO
l()
print(f"Bem-vindo à {nome_da_padaria}!")
l()


# BLOCO 4: PEDIDO
while True:
    print("PRODUTOS:")
    e()

    for nome, preco in produtos.items():
        print(f"{nome.title()} R${preco:.2f} (unidade)")

    e()

    produto = input("Digite o produto que irá querer: ").strip().upper()

    if produto not in produtos:
        print("Produto não encontrado. Tente novamente.")
        e()
        continue

    try:
        quantidade = int(input("Digite a quantidade: "))
    except ValueError:
        print("Digite a quantidade usando um número inteiro.")
        e()
        continue

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        e()
        continue

    total = produtos[produto] * quantidade + viagem_custo

    print(f"Subtotal: R${produtos[produto] * quantidade:.2f}")
    print(f"Taxa de viagem: R${viagem_custo:.2f}")
    print(f"Total: R${total:.2f}")
    break