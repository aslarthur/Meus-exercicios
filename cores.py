continuar = True
def l1():
    print()
    print ("-=" * 50)
    print()
def l2():
    print ("-=" * 50)
def e3():
    print ()
while continuar: 

    l1()

    print (f"\033[31mSistema \033[m\033[32mDe\033[m\033[33m Cores\033[m")
    l1()
    print (f"\033[36mProgramas:\033[m")
    l1()
    print (f"1. Cor de \033[34mtexto\033[m e \033[34;43mfundo\033[m")
    l1()
    n = str(input("Digite o número do programa que ira querer: "))
    if n == "1":
        while True:
            l2()
            print (f"\033[1;31mC\033[m\033[1;32mO\033[m\033[1;33mR\033[m\033[1;34mE\033[m\033[1;35mS\033[m \033[1;36mD\033[m\033[1;36mE\033[m \033[1;31mT\033[m\033[1;32mE\033[m\033[1;33mX\033[1;34mT\033[m\033[1;35mO\033[m\033[1;36m:\033[m")
            print (f"1. \033[1;4;37mBranco\033[m")
            print (f"2. \033[1;4;31mVermelho\033[m")
            print (f"3. \033[1;4;32mVerde\033[m")
            print (f"4. \033[1;4;33mAmarelo\033[m")
            print (f"5. \033[1;4;34mAzul\033[m")
            print (f"6. \033[1;4;35mRoxo\033[m")
            print (f"7. \033[1;4;36mAzul Claro\033[m")
            print (f"8. \033[1;4;30mCinza\033[m")
            print (f"9. \033[40mSimples\033[m")
            e3()
            nova_cor = str(input(f"Digite a cor de texto que você ira \033[31mquerer\033[m: ")) 
            cor = nova_cor.upper().strip()
            if cor == "BRANCO":
             código = "37"
             break
            elif cor == "VERMELHO":
                código = "31"
                break
            elif cor == "VERDE":
                código = "32"
                break
            elif cor == "AMARELO":
                código = "33"
                break
            elif cor == "AZUL":
                código = "34"
                break
            elif cor == "ROXO":
                código = "35"
                break
            elif cor == "AZUL CLARO":
                código = "36"
                break
            elif cor == "CINZA":
                código = "30"
                break
            elif cor == "SIMPLES":
                código = "30"
                break

            else:
                e3()
                e3()
                e3()
                l1()
                print (f"\033[31;4mNão encontrado! Tente novamente.\033[m")
                continue
    else:
        e3()
        e3()
        e3()
        l1()
        print (f"\033[31;4mNão encontrado! Tente novamente \033[m")
        continue
    while True:
        l2()
        e3()
        print (f"\033[37;1;4;47mF\033[m\033[37;1;4;41mU\033[m\033[37;41;4;2mN\033[m\033[37;1;4;43mD\033[m\033[37;1;4;44mO\033[m\033[37;1;4;45mS\033[m:")
        print (f"1. \033[1;4;47mBranco\033[m")
        print (f"2. \033[1;4;41mVermelho\033[m")
        print (f"3. \033[1;4;42mVerde\033[m")
        print (f"4. \033[1;4;43mAmarelo\033[m")
        print (f"5. \033[1;4;44mAzul\033[m")
        print (f"6. \033[1;4;45mRoxo\033[m ")
        print (f"7. \033[1;4;46mAzul claro\033[m")
        print (f"8. \033[1;4;40mCinza\033[m")
        print (f"9. \033[40mSimples\033[m")
        e3()
        l1()
        novo_fundo = str(input("Digite o fundo que ira querer: "))
        fundo = novo_fundo.upper().strip()
        l1()
        if fundo == "BRANCO":
            print (f"\033[1;4;{código};47mFUNDO: {fundo}, TEXTO: {cor}\033[m")
            break
        elif fundo == "VERMELHO":
            print (f"\033[1;4;{código};41mFUNDO: {fundo}, TEXTO: {cor}\033[m")
            break
        elif fundo == "VERDE":
            print(f"\033[1;4;{código};42mFUNDO: {fundo}, TEXTO: {cor}\033[m")
            break
        elif fundo == "AMARELO":
            print (f"\033[1;4;{código};43mFUNDO: {fundo}, TEXTO: {cor}\033[m")
            break
        elif fundo == "AZUL":
            print (f"\033[1;4;{código};44mFUNDO: {fundo}, TEXTO: {cor}\033[m")
            break
        elif fundo == "ROXO":
            print (f"\033[1;4;{código};45mFUNDO: {fundo}, TEXTO: {cor}\033[m")
            break
        elif fundo == "AZUL CLARO":
            print (f"\033[1;4;{código};46mFUNDO: {fundo}, TEXTO: {cor}\033[m")
            break
        elif fundo == "CINZA":
            print (f"\033[1;4;{código};40mFUNDO: {fundo}, TEXTO: {cor}\033[m")
            break
        elif fundo == "SIMPLES":
            print (f"\033[1;4;{código};40mFUNDO: {fundo}, TEXTO: {cor}\033[m")
            break
        else:
            e3()
            e3()
            e3()
            l1()
            print (f"\033[1;31mNão encontrado! Tente novamente.\033[m")
            continue   
    while True:
        l1()
        print ("Deseja continuar?")
        l1()
        print ("1. Sim")
        l1()
        print ("2. Não")
        l1()
        sim_ou_não = str(input("Digite o número da resposta: "))
        l1()

        if sim_ou_não == "1":
            e3()
            l1()
            print ("Ótimo!")
            l1()
            e3()
            break
        elif sim_ou_não == "2":
            print ("Tudo bem! Até a próxima...")
            l1()
            continuar = False
            break
        else:
            print (f"\033[1;31mNão encontrado! Tente novamente\033[m")
            l1()
            continue

