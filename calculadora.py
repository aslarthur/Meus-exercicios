print ()
print ("Sejá bem vindo(a) a minha calculadora!")

while True: 
    print ()
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    print ()
    print ("OPERADORES: ")
    print ("1. +")
    print ("2. -")
    print ("3. *")
    print ("4. /")
    print ("5. //")
    print("6. %")
    print ()
    op1 = num1 + num2
    op2 = num1 - num2
    op3 = num1 * num2
    op4 = num1 / num2
    op5 = num1 // num2
    op6 = num1 % num2
    op = input("Digite o número do operador que ia querer: ")
    print()
    if op == "1":
        print ("{} + {} = {}".format (num1, num2, op1 ))
  
    elif op == "2":
        print ("{} - {} = {}".format (num1, num2, op2))

    elif op == "3":
        print ("{} x {} = {}".format (num1, num2, op3))
  
    elif op == "4":
        print ("{} / {} = {:.2f}".format (num1, num2, op4))

    elif op == "5":
        print ("{} // {} = {}".format (num1, num2, op5))

    elif op == "6":
        print ("{} % {} = {}".format (num1, num2, op6 ))

    else:
        print ("Operador não encontrado. Tente novamente")
    print ()
    print ("Deseja continuar?")
    print ()
    print ("1. Sim")
    print ("2. Não")
    print ()
    sn = input("Digite o número da resposta: ")
    print ()
    if sn == "1":
        print ("Ótimo!")
        continue
    else:
        print ("Tudo bem. Até a próxima!")
        break