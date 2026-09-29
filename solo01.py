# Ler o ano de nascimento (int) e calcular a idade (2026 - ano)

# Se idade < 18: menor de idade
# Senão: maior de idade + calcular quanto falta pra 65 (65 - idade)
    # Se esse valor for positivo, mostrar quanto falta
    # Se for zero ou negativo, avisar que já passou dos 65

idade = int(input("Digite sua idade: "))
if idade < 18:
    print ("Menor de idade")
elif idade < 65:
    ano = 65 - idade
    print (f"Faltam {ano} anos para você fazer 65 anos!")
else:
    print ("Você já passou dos 65")