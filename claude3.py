# EXERCÍCIO 3 - Maior de dois
# Peça duas idades e diga quem é mais velho.
# Resolução:
# 1. Peça as duas idades com int(input())
# 2. Use if idade1 > idade2
# 3. Use elif idade2 > idade1
# 4. Use else para quando forem iguais
idade1 = int(input("Digite a primeira idade: "))
idade2 = int(input("Digite a segunda idade: "))
if idade1 > idade2:
    print (f"\033[32m{idade1}\033[m é \033[31mMAIOR\033[m que \033[33m{idade2}\033[m")
elif idade1 < idade2:
    print (f"\033[32m{idade2}\033[m é \033[31mMAIOR\033[m que \033[33m{idade1}\033[m ")
else:
    print (f"\033[32m{idade1}\033[m é \033[31mIGUAL\033[m a \033[33m{idade2}\033[m")