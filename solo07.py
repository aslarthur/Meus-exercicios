num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
c = input("Digite a operação. Opções:\n+\n-\n*\n/\nDigite aqui: ")

while True:
    if c == "+":
        print ("{} + {} = {}".format (num1, num2, num1 + num2))
        break
    elif c == "-":
        print ("{} - {} = {}".format(num1, num2, num1 - num2))
        break
    elif c == "*":
        print ("{} * {} = {}".format (num1, num2, num1 * num2))
        break
    elif c == "/":
        print ("{} / {} = {}".format (num1, num2, num1 / num2))
        break
    else:
        print ("Não encontrado.")
        c = input("Digite a operação novamente. Opções: \n+\n-\n*\n/\nDigite aqui: ")