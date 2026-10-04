def l():
    print ("-=" * 76)
def e():
    print()
while True:
    e()
    l()
    print (f"\033[32mSeja muito bem vindo(a) a o meu programa!\033[m \033[33mAqui eu vou fazer um resumo de códigos que eu estou\033[m \033[31maprendendo ao longo da minha jornada!\033[m")
    l()
    e()
    print (f"\033[1;37mP\033[m\033[1;31mR\033[m\033[1;32mO\033[m\033[1;33mG\033[m\033[1;34mR\033[mA\033[1;35mM\033[m\033[1;36mA\033[m\033[1;30mS\033[m:")
    e()
    print (f"1. \033[4;1;37mTabuada\033[m")
    print (f"2. \033[4;1;31mCalculadora\033[m")
    print (f"3. \033[4;1;32mDobro e triplo\033[m")
    print (f"4. \033[4;1;33mMédia de notas\033[m")
    print (f"5. \033[4;1;34mReais para dolar\033[m")
    print (f"6. \033[4;1;35mPar ou ímpar\033[m")
    print (f"7. \033[4;1;36mPadaria\033[m")
    print (f"8. \033[4;1;30mLista de compras (com valor total)\033[m ")
    print (f"9. \033[4;1;37mSortear aluno\033[m")
    print (f"10. \033[4;1;31mAdivinhar número\033[m")
    print (f"11. \033[4;1;32mCofre com 3 tentativas de senha\033[m")
    print (f"12. \033[4;1;33mSistema de cores\033[m")
    print (f"13. \033[4;1;34mConfirmar idade\033[m")
    print (f"14. \033[4;1;35mCadastro com confirmação\033[m")
    print (f"15. \033[4;1;36mAnalisar nome\033[m")
    e()
    l()
    programa = int(input("Digite o número do programa que ira querer: "))
    l()
    
    if programa == 1:
        num = int(input("Digite o número que ira querer: "))
        e()
        for n in range (1, 11):
            
            print (f"{num} x {n} = {num * n}")
            l()
    elif programa == 2:
        print (f"\033[31mBem vindo(a)\033[m \033[32ma\033[m \033[33mminha calculadora!\033[m ")
        l()
        e()
        n1 = float(input("Digite um número: "))
        l()
        n2 = float(input("Digite outro número: "))
        l()
        e()
        print ("OPERADORES:")
        print ("1. +")
        print ("2. -")
        print ("3. x")
        print ("4. /")
        print ("5. //")
        print ("6. %")
        e()
        l()
        op = int(input("Digite o número do operador: "))
        l()
        if op == 1:
            print (f"{n1} + {n2} = {n1 + n2:.2f}")
        elif op == 2:
            print (f"{n1} - {n2} = {n1 - n2:.2f}")
        elif op == 3:
            print (f"{n1} x {n2} = {n1 * n2:.2f}")
        elif op == 4:
            print (f"{n1} / {n2} = {n1 / n2:.2f}")
        elif op == 5:
            print (f"{n1} // {n2} = {n1 // n2}")
        elif op == 6:
            print (f"{n1} % {n2} = {n1 % n2}")  
        l()
    elif programa == 3:
        
        num = int(input("Digite um número: "))
        l()
        print (f"O dobro de {num} é {num * 2}")
        l()
        print (f"E o triplo de {num} é {num * 3}")
        
    elif programa == 4:
        nota1 = float(input("Digite a primeira nota: "))
        l()
        nota2 = float(input("Digite a segunda nota: "))
        l()
        média = (nota1 + nota2) / 2
        print (f"Sua média é de {média}")
        l()
        if média >= 7:
            print (f"\033[32mAprovado!\033[m")
        elif média >= 5:
            print (f"\033[33mRecuperação!\033[m")
        else:
            print (f"\033[31mReprovado!\033[m")
    elif programa == 5:
        real = float(input("Digite quantos R$ você tem: R$"))
        dolar =  real / 5.21
        l() 
        print (f"Com R${real:.2f} você pode comprar US${dolar:.2f}")
    elif programa == 6:
        n = int(input("Digite um número par: "))
        l()
        if n %2 ==0:
            print ("Esté número é um número \033[33mPAR!\033[m")
        else:
            print (f"Este número é um número \033[32mÍMPAR!\033[m")
    elif programa == 7:
        
        print (f"\033[33mCOFFEE SHOP\033[m")
        l()
        print (f"\033[32mSabores café:\033[m ")
        
        p1 = "Café Extra Forte"
        v1 = 5.92
        p2 = "Café Com Leite"
        v2 = 6.38
        p3 = "Café Frio"
        v3 = 10.93
        e()
        print (f"{p1} ")
        print (f"{p2} ")
        print (f"{p3} ")
        e()
        l()
        novo_produto = str(input("Digite o produto que ira querer: "))
        produto = novo_produto.upper().strip()
        l()
        e()
        if produto == "CAFÉ EXTRA FORTE":
            print (f"R${v1} qual vai ser a forma de pagamento? ")
        elif produto == "CAFÉ COM LEITE":
            print (f"R${v2} qual vai ser a forma de pagamento? ")
        elif produto == "CAFÉ FRIO":
            print (f"R${v3} qual vai ser a forma de pagamento")   
        else:
            print (f"\033[31mNão encontrado! Tente novamente.\033[m")    
    elif programa == 8:
        p1 = str(input("Digite o primeiro produto: "))
        l()
        v1 = float(input(f"Digite o valor de {p1}: R$")) 
        l()
        p2 = str(input("Digite o segundo produto: "))
        l()
        v2 = float(input(f"Digite o valor de {p2}: R$"))    
        l()
        p3 = str(input("Digite o terceiro produto: "))
        l()
        v3 = float(input(f"Digite o valor de {p3}: R$"))
        v = v1 + v2 + v3
        l()
        print (f"O valor total é de R${v}")
    elif programa == 9:
        from random import choice

        n1 = str(input("Digite o primeiro nome: "))
        l()
        n2 = str(input("Digite o segundo nome: "))
        l()
        n3 = str(input("Digite o terceiro nome: "))
        l()
        n4 = str(input("Digite o quarto nome: "))
        l()
        n5 = str(input("Digite o quinto nome: "))
        l()
        lista = [n1, n2, n3, n4, n5]
        sorteado = choice(lista)
        l()
        print (f"O sorteado foi: {sorteado}")
    elif programa == 10:
        import random 
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        escolhido = random.choice(lista)
        
        num = int(input("Digite um número de 1 a 10: "))
        l()
        if num == escolhido:
            print (f"Você \033[32mGANHOU\033[m de mim!")
        elif num != escolhido:
            print (f"Eu \033[33mGANHEI\033[m de você! eu pensei no número {escolhido}")
        else:
            print ("Número não encontrado! Tente novamente.")
        l()
    elif programa == 11:
        senha = "Mia K."
        l()
        cofre = input("Digite a senha do cofre: ")
        l()
        tentativas = 3
        while cofre != senha:
            tentativas -= 1
            print (f"Senha incorreta! Restam {tentativas} tentativas. Tente novamente: ")
            l()
            
            cofre = input("Digite a senha do cofre: ")
            l()
            if tentativas == 0:
                print ("Cofre trancado!")
                break
        if cofre == senha:
            print ("Você acertou!")
        l()
    elif programa == 12:
        l()
        print(f"\033[1;31mBem\033[m \033[1;32mvindo\033[m \033[1;33mao\033[m \033[1;34msistema\033[m \033[1;35mde\033[m \033[1;36mcores!\033[m ")
        l()
        print (f"\033[1;4;31mT\033[m\033[1;4;32mE\033[m\033[1;4;33mX\033[m\033[1;4;34mT\033[m\033[1;4;35mO\033[m\033[1;4;36mS\033[m: ")
        l()
        e()
        print (f"1. \033[1;37mBranco\033[m")
        print (f"2. \033[1;31mVermelho\033[m")
        print (f"3. \033[1;32mVerde\033[m")
        print (f"4. \033[1;33mAmarelo\033[m")
        print (f"5. \033[1;34mAzul\033[m")
        print (f"6. \033[1;35mRoxo\033[m")
        print (f"7. \033[1;36mAzul Claro\033[m")
        print (f"8. \033[1;30mCinza\033[m")
        e()
        nova_cor = input("Digite a cor que ira querer: ")
        cor = nova_cor.upper().strip()
        if cor == "BRANCO":
            código = "37"
            
        elif cor == "VERMELHO":
            código = "31"
            
        elif cor == "VERDE":
            código = "32"
            
        elif cor == "AMARELO":
            código = "33"
            
        elif cor == "AZUL":
            código = "34"
            
        elif cor == "ROXO":
            código = "35"
            
        elif cor == "AZUL CLARO":
            código = "36"
            
        elif cor == "CINZA":
            código = "30"
        else:
            print (f"\033[1;31mNão encontrado. Tente novamente!")
        
        print (f"\033[47mF\033[m\033[41mU\033[m\033[42mN\033[m\033[43mD\033[m\033[44mO\033[m\033[45mS\033[m\033[46m:\033[m")
        e()
        print (f"1. \033[1;37;47mBranco\033[m")
        print (f"2. \033[1;41mVermelho\033[m")
        print (f"3. \033[1;42mVerde\033[m")
        print (f"4. \033[1;43mAmarelo\033[m")
        print (f"5. \033[1;44mAzul\033[m")
        print (f"6. \033[1;45mRoxo\033[m")
        print (f"7. \033[1;46mAzul claro\033[m")
        print (f"8. \033[1;30;40mCinza\033[m")
        e()
        novo_fundo = input("Digite a cor do fundo: ")
        fundo = novo_fundo.upper().strip()
        l()
        if fundo == "BRANCO": 
            print (f"\033[1;{código};47mFUNDO: {fundo} COR: {cor} \033[m")
        elif fundo == "VERMELHO":
            print (f"\033[1;{código};41mFUNDO: {fundo} COR: {cor} \033[m")
        elif fundo == "VERDE":
            print (f"\033[1;{código};42mFUNDO: {fundo} COR: {cor} \033[m")
        elif fundo == "AMARELO":
            print (f"\033[1;{código};43mFUNDO: {fundo} COR: {cor} \033[m")
        elif fundo == "AZUL":
            print (f"\033[1;{código};44mFUNDO: {fundo} COR: {cor} \033[m")
        elif fundo == "ROXO":
            print (f"\033[1;{código};45mFUNDO: {fundo} COR: {cor} \033[m")
        elif fundo == "AZUL CLARO":
            print (f"\033[1;{código};46mFUNDO: {fundo} COR: {cor} \033[m")
        elif fundo == "CINZA":
            print (f"\033[1;{código};40mFUNDO: {fundo} COR: {cor} \033[m")
        else:
            print (f"\033[1;31mNão encontrado. Tente novamente ")
    else:
        print (f"\033[31mPrograma não encontrado. Tente novamente!\033[m ")
        break
    e()
    e()
    l()
    print ("Deseja continuar?")
    l()
    print ("1. Sim")
    l()
    print ("2. Não")
    l()
    sn = int(input("Digite o número da resposta aqui: "))
    l()
    if sn == 1:
        continue
    elif sn == 2:
        print ("Tudo bem! Até a próxima.")
        l()
        break
    else:
        print ("Opção inválida! Tente novamente.")
        l()
        break
        
e()