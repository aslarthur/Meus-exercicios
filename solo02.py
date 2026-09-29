# Ler o preço do produto (float) e a quantidade (int)

# Calcular o total: preço * quantidade

# Se o total for maior que 100:
    # calcular o desconto (10% do total) e subtrair do total
    # mostrar o valor final com desconto

# Senão:
    # mostrar o total sem desconto


produto = str(input("Digite o produto: "))
valor = float(input("Digite o valor do produto: R$"))
quantidade = int(input("Digite a quantidade: "))

novo_valor = (valor * quantidade ) 
valor_total =  valor * quantidade - novo_valor * 10 /100

if novo_valor > 100:
    print (f"O valor final é de R${valor_total}")

else:
    valor_normal = valor * quantidade
    print (f"O valor final é de R${valor_normal}")