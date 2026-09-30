#VARIAVEIS

nome_padaria = "Padaria Pão Quente"
p1 = "pão de forma"
v1 = 5
p2 = "pão de queijo"
v2 = 4
p3 = "sonho"
v3 = 6
p4 = "coxinha"
v4 = 7
p5 = "broa doce"
v5 = 5

#PRODUTOS E VALORES

print ("______________________________")
print (f"Bem vindo(a) a {nome_padaria}")
print ("______________________________")
print ("PRODUTOS:")
print ("______________________________")
print (f"{p1} R${v1}")
print ("______________________________")
print (f"{p2} R${v2}")
print ("______________________________")
print (f"{p3} R${v3}")
print ("______________________________")
print (f"{p4} R${v4}")
print ("______________________________")
print (f"{p5} R${v5}")
print ("______________________________")

#USER

produto = input("Digite o produto que irá querer: ").lower()

print ("______________________________")
quantidade = int(input("Digite a quantidade do produto: "))
print ("______________________________")

if produto == p1:
    novo_valorp1 = v1 * quantidade
    print (f"O total da compra é de R${novo_valorp1}")
    print ("______________________________")
elif produto == p2:
    novo_valorp2 = v2 * quantidade
    print (f"O total da compra é de R${novo_valorp2}")
    print ("______________________________")
elif produto == p3:
    novo_valorp3 = v3 * quantidade
    print (f"O total da compra é de R${novo_valorp3}")
    print ("______________________________")
elif produto == p4:
    novo_valorp4 = v4 * quantidade
    print (f"O total da compra é de R${novo_valorp4}")
    print ("______________________________")
elif produto == p5:
    novo_valorp5 = v5 * quantidade
    print (f"O valor total da compra é de R${novo_valorp5}")
    print ("______________________________")
else:
    print("Produto não encontrado!")
    print("______________________________")
