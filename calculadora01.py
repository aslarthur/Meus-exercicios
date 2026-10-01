print ()
print ("Bem vindo(a) a calculadora01.py!")
print ()
while True:
    n1 = int(input("Digite um número: "))
    print ()
    n2 = int(input("Digite outro número: "))
    print()
    print ("OPERADORES:")
    print ("1. +")
    print ("2. -")
    print ("3. x")
    print ("4. /")
    print ("5. //")
    print ("6. %")
    print ()
    op1 = n1 + n2
    op2 = n1 - n2
    op3 = n1 * n2
    op4 = n1 / n2
    op5 = n1 // n2
    op6 = n1 % n2

    op = input("Digite o número do operador que ira querer: ")
    print ()
    if op == "1":
        print (f"{n1} + {n2} = {op1}")
     
    elif op == "2":
        print (f"{n1} - {n2} = {op2}")
    
    elif op == "3":
        print (f"{n1} x {n2} = {op3}")
     
    elif op == "4":
        print (f"{n1} / {n2} = {op4}")
    
    elif op == "5":
        print (f"{n1} // {n2} = {op5}")
    
    elif op == "6":
        print (f"{n1} % {n2} = {op6}")
    
    else:
        print ("Operador não encontrado. Tente novamente")
    print ()
    print ("Quer continuar?")
    print ()
    print ("1. Sim")
    print ("2. Não")
    print ()
    sn = input("Digite o número da sua resposta aqui: ")
    if sn == "1":
        print ()
        print ("Ótimo!")
        print ()
        continue
    else:
        print ()
        print ("Tudo bem. Até a próxima")
        print ()
        break