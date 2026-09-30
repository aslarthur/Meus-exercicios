#VARIAVEIS

nome_padaria = "Padaria Pão Quente"
p1 = "Pão de forma"
v1 = 5
p2 = "Pão de queijo"
v2 = 4
p3 = "Sonho"
v3 = 6
p4 = "Coxinha"
v4 = 7
p5 = "Broa doce"
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
produto = input("Digite o produto que ira querer: ".lower())
print ("______________________________")
quantidade = int(input("Digite a quantidade do produto: "))
print ("______________________________")
if produto == p1:
    novo_valorp1 = v1 * quantidade
    print ("______________________________")
    print (f"O total da compra é de R${novo_valorp1}")
    print ("______________________________")