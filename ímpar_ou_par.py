while True:
    número = int(input("Digite um número par: "))
    if número %2 == 0:
        print ("Você digitou um número par. Obrigado!")
        break
    else:
        print ("Você digitou um número ímpar. Tente novamente")
print ("Fim do programa ")