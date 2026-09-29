#Adição + 

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
soma = a + b
print("O resultado da adição é:", soma)
# Soma os dois valores digitados. Simples: a + b.

#Subtração -

c = int(input("Digite um número: "))
d = int(input("Digite outro número: "))
sub = c - d 
print("O resultado da subtração é:", sub)
# Subtrai o segundo número do primeiro: c - d.

#Multiplicação *

e = int(input("Digite um número: "))
f = int(input("Digite outro número: "))
mult = e * f
print("O resultado da multiplicação é:", mult)
# Multiplica os dois valores: e * f.

#Divisão /

g = int(input("Digite um número: "))
h = int(input("Digite outro número: "))
div = g / h  
print("O resultado da divisão é:", div)
# Divide g por h. Em Python, / SEMPRE retorna float (número decimal),
# mesmo que o resultado seja "exato" (ex: 10/2 = 5.0, não 5).

#Divisão inteira //

i = int(input("Digite um número: "))
j = int(input("Digite outro número: "))
div_int = i // j
print("O resultado da divisão inteira é:", div_int)
# Faz a divisão e descarta a parte decimal (arredonda pra baixo).
# Ex: 7 // 2 = 3 (não 3.5).

#Módulo (resto da divisão) %

k = int(input("Digite um número: "))
l = int(input("Digite outro número: "))
resto = k % l
print("O resto da divisão é:", resto)
# Retorna o RESTO da divisão entre k e l.
# Ex: 7 % 2 = 1 (7 dividido por 2 dá 3, sobra 1).
# Muito usado para saber se um número é par/ímpar: n % 2 == 0.

#Concatenação de strings (+)

nome = "Arthur"
sobrenome = "Santana"
resultado = nome + " " + sobrenome
print(resultado)
# O + entre strings não soma números, ele JUNTA (concatena) os textos.

#Multiplicação / Repetição de strings


nome = "Arthur" 
sobrenome = "Santana"
resultado = (nome + " ") * 3 + sobrenome
print(resultado)

# O * entre uma string e um número REPETE a string aquele número de vezes.
# Aqui, "Arthur " é repetido 3 vezes antes de juntar com o sobrenome.