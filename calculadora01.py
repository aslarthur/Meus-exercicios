print ()
print ("Bem vindo(a) a calculadora.py!")
print ()
while True:
    n1 = float(input("Digite um número: "))
    print ()
n2 = float(input("Digite outro número: "))
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
op5 = n1 % n2

op = input("Digite o número do operador que ira querer: ")
print ()
if op == "1":
    print (f"{n1} + {n2} = {op1}")