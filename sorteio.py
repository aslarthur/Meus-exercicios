from random import choice
lista = [1,2,3,4,5,6,7,8,9,10]
sorteado = choice(lista)
digitado = int(input("Digite um número: "))
while True:
    if digitado > sorteado:
        print ("Mais baixo!")
        digitado = int(input("Digite um número: "))
    elif digitado < sorteado:
        print ("Mais alto!")
        digitado = int(input("Digite um número: "))
    else:
        print ("Você acertou!")
        break
