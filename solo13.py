n = float(input("Digite a primeira nota: "))
n1 = float(input("Digite a segunda nota: "))
t = (n1 + n) / 2
if t >= 6:
    print ("passou!")
elif t >= 4:
    print ("Recuperação")
else:
    print ("Reprovado.")
