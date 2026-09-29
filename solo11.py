senha_correta = 1982
senha_digitada = int(input("Digite a senha: "))

while True: 
  if senha_digitada == senha_correta:
    print ("Senha correta!")
    break
  else:
    print ("Senha incorreta! Tentativas restantes: 2")
    senha_digitada = int(input("Digite sua senha novamente: "))
    if senha_digitada != senha_correta:
      print ("Senha incorreta! Tentativas restantes: 1")
      senha_digitada = int(input("Digite sua senha novamente: "))
      if senha_digitada != senha_correta:
        print ("Senha incorreta! Tentativas restantes: 0")
        print ("Cofre trancado!")
        break