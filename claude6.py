# DESAFIO 6 - Soma dos pares
# Mostre a soma de todos os números pares de 1 a 20.
# Informações: range(), operador % (resto da divisão), acumulador.

par = 0
números = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for n in números:
    if n %2 != 0:
        continue
    par += n
    print (par)
     
