print ("____________________________________________________")
email = input("Digite seu email: ")
print ("____________________________________________________")
senha = input("Digite sua senha: ")
print ("_____________________________")
confirmação = input("Confirme sua senha: ")
print ("___________________________")

while confirmação != senha:
    print ("As senhas não coincidem! ")
    print ("_______________________")
    senha = input("Digite a senha novamente: ")
    print ("__________________________________")
    confirmação= input("Confirme a senha: ")
    print ("__________________________________")
if senha == confirmação:
    print ("Bem vindo! Olhe os programas abaixo: ")
    print ("___________________________________")
    print ("Programa 1: Tabuada")
    print ("___________________________________")
    num = int(input("Digite um número: "))
    print ("___________________________________")
    num1 = num * 1
    num2 = num * 2
    num3 = num * 3
    num4 = num * 4
    num5 = num * 5
    num6 = num * 6
    num7 = num * 7
    num8 = num * 8
    num9 = num * 9
    num10 = num * 10
    print ("{} x {} = {}".format (num, 1, num1))
    print ("____________________")
    print ("{} x {} = {}".format (num, 2, num2))
    print ("____________________")
    print ("{} x {} = {}".format (num, 3, num3))
    print ("____________________")
    print ("{} x {} = {}".format (num, 4, num4))
    print ("____________________")
    print ("{} x {} = {}".format (num, 5, num5))
    print ("____________________")
    print ("{} x {} = {}".format (num, 6, num6))
    print ("____________________")
    print ("{} x {} = {}".format (num, 7, num7))
    print ("____________________")
    print ("{} x {} = {}".format (num, 8, num8))
    print ("____________________")
    print ("{} x {} = {}".format (num, 9, num9))
    print ("____________________")
    print ("{} x {} = {}".format (num, 10, num10))
    print ("________________________________")
    print ("Programa 2: Confirmação de idade")
    print ("________________________________")
    idade = int(input("Digite sua idade: "))
    print ("________________________________")
    if idade <=17:
     print ("Leia a biblia cedo amiginho!")
     print ("_______________________________")
    else:
       print ("Já leu a biblia hoje irmão?")
    print ("________________________________")
    print ("Programa 3: Ano de nascimento")
    print ("________________________________")
    nascimento = int(input("Digite sua idade novamente: "))
    ano_nascimento = 2026 - idade
    print ("__________________________________")
    print ("Que legal! Você nasceu em {}!".format (ano_nascimento))
    print ("__________________________________")
    print ("Programa  4: lista")
    print ("__________________________________")
    p1 = input("Digite o primeiro produto: ")
    print ("__________________________________")
    v1 = float(input("Digite o valor de {} R$".format (p1)))
    print ("__________________________________")
    p2 = input("Digite o segundo produto: ")
    print ("__________________________________")
    v2 = float(input("Digite o valor de {} R$".format (p2)))
    print ("__________________________________")
    p3 = input("Digite o terceiro produto: ")
    print ("__________________________________")
    v3 = float(input("Digite o valor de {} R$".format(p3)))
    valortotal = v1 + v2 + v3
    print ("__________________________________")
    print ("O valor total é de R${}".format (valortotal))
    print ("__________________________________")
    import math
    print ("Programa 5: Soma de 2 números")
    print ("__________________________________")
    nume = int(input("Digite um número: "))
    print ("__________________________________")
    num0 = int(input("Digite outro número: "))
    print ("__________________________________")
    s = nume + num0
    d = nume / num0
    m = nume * num0
    sub = nume - num0
    div = nume // num0
    r = nume % num0
    raiz = nume ** 0.5
    i = int(nume)
    ant = nume - 1
    suc = nume + 1
    print ("{} + {} = {}".format (nume, num0, s))
    print ("__________________________________")
    print ("{} / {} = {}".format (nume, num0, d))
    print ("__________________________________")
    print ("{} x {} = {}".format (nume, num0, m))
    print ("__________________________________")
    print ("{} - {} = {}".format (nume, num0, sub))
    print ("__________________________________")
    print ("{} // {} = {}".format (nume, num0, div))
    print ("__________________________________")
    print ("{} % {} = {}".format (nume, num0, r))
    print ("__________________________________")
    print ("√ {} = {}".format (nume, raiz))
    print ("__________________________________")
    print ("int {} = {}".format (nume, i))
    print ("__________________________________")
    print ("Antecessor de {} = {}".format (nume, ant))
    print ("__________________________________")
    print ("Sucessor de {} = {}".format (nume, suc))
    print ("__________________________________")
    print ("Programa 6: Sorteio")
    print ("__________________________________")
    from random import choice
    n1 = input("Digite o primeiro aluno: ")
    print ("__________________________________")
    n2 = input("Digite o segundo aluno: ")
    print ("__________________________________")
    n3 = input("Digite o terceiro aluno: ")
    print ("__________________________________")
    n4 = input("Digite o quarto aluno: ")
    print ("__________________________________")
    lista = [n1, n2, n3, n4]
    sorteado = choice(lista)
    print ("O sorteado foi: {}".format (sorteado))
    print ("__________________________________")
    print ("Programa 7: Embaralhando os nomes")
    from random import shuffle
    print ("__________________________________")
    nome1 = input("Digite o primeiro nome: ")
    print ("__________________________________")
    nome2 = input("Digite o segundo nome: ")
    print ("__________________________________")
    nome3 = input("Digite o terceiro nome: ")
    print ("__________________________________")
    nome4 = input("Digite o quarto nome: ")
    print ("__________________________________")
    lista1 = [nome1, nome2, nome3, nome4]
    shuffle (lista1)
    print ("A ordem é: {}".format (lista1))
    print ("__________________________________")
    print ("Programa 8: Tocando um MP3")
    print ("__________________________________")
    import os
    music = r"arthur.mp3"
    os.startfile (music)