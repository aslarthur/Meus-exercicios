# Peça pro usuário digitar o nome e guarde numa variável

# Transforme essa variável em maiúsculas e mostre na tela

# Transforme a mesma variável em minúsculas e mostre na tela

# Conte quantos caracteres tem essa variável e mostre o total
# (se o nome tiver espaço, a contagem normalmente inclui ele também -
# se quiser só as letras, precisa tirar o espaço antes de contar)

print ("____________________________")
nome = input("Digite seu nome: ")
print ("____________________________")

maiúsculas = nome.upper()
minúsculas = nome.lower()
letras = len (nome.replace(" ", ""))
espaço = len (nome)
normal = nome.title()

print (maiúsculas)
print ("____________________________")
print (minúsculas)
print ("____________________________")
print (letras)
print ("____________________________")
print (espaço)
print ("____________________________")
print (normal)
print ("____________________________")