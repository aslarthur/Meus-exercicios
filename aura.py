num = int(input("Qual você prefere: \n67\n42\ndigite aqui: "))

if num == 67:
    print ("SIX SEVEN")
elif num == 42:
    print ("FOUR TWO")
else:
    print ("Meme não encontrado. Vamos para o próximo")
print ("______________________")
print("AURA -100: FRACO")
print ("______________________")
print("AURA 0: NORMAL")
print ("______________________")
print("AURA 100: INICIANTE")
print ("______________________")
print("AURA 500: FORTE")
print ("______________________")
print("AURA 1000: ABSURDO")
print ("______________________")
print("AURA 5000: LENDÁRIO")
print ("______________________")
print("AURA 10000: MÍTICO")
print ("______________________")
print("AURA 50000: DIVINO")
print ("______________________")
print("AURA 100000: SUPREMO")
print ("______________________")
print("AURA 1000000: INFINITO")
print ("______________________")

aura = int(input("Digite o número da sua AURA: "))

while True:

    if aura == -100:
        print("Fraco")
        break

    elif aura == 0:
        print("Normal")
        break

    elif aura == 100:
        print("Iniciante")
        break

    elif aura == 500:
        print("Forte")
        break

    elif aura == 1000:
        print("Absurdo")
        break

    elif aura == 5000:
        print("Lendário")
        break

    elif aura == 10000:
        print("Mítico")
        break

    elif aura == 50000:
        print("Divino")
        break

    elif aura == 100000:
        print("Supremo")
        break

    elif aura == 1000000:
        print("Fah")
        break

    else:
        print("Aura não encontrada. Tente novamente")
        aura = int(input("Digite o número da sua AURA: "))