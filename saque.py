valor1 = int(input("Digite quanto dinheiro você quer sacar: R$"))
saldo = 210 
múltiplo = valor1 % 5 == 0 
restante = valor1 % 100

if valor1 <= saldo and múltiplo:
    print ("Saque efetuado com sucesso!")
    print ("Agora você tem R${}".format (saldo - valor1))
    print ("Você consegue ter {} notas de 100.".format (valor1 // 100))
    print ("Você consegue ter {} notas de 50.".format (valor1 //  50))
    print ("Você consegue ter {} notas de 20.".format (valor1 // 20))
    print ("Você consegue ter {} notas de 10.".format (valor1 //  10))
    print ("Você consegue ter {} notas de 5.".format (valor1 //  5))
    print ("Você consegue ter {} notas de 2.".format (valor1 // 2))
    print ("O restante é R${}".format (restante))
else:
    print ("Você não tem esse valor.")