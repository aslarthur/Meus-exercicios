print ()
print ("Welcome to my calculator!")
print ()
while True: 
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    number3 = number1 + number2
    number4 = number1 - number2
    number5 = number1 * number2
    number6 = number1 / number2
    number7 = number1 // number2
    number8 = number1 % number2

    print ()
    print ("OPERATORS:")
    print ("1. +")
    print ("2. -")
    print ("3. *")
    print ("4. /")
    print ("5. //")
    print ("6. %")
    print ()

    operator = input("Enter the number of the chosen operator: ")

    print ()
    print ("calculating...")
    print ()

    import time
    time.sleep(5)

    if operator == "1":
        print (f"{number1} + {number2} = {number3}")

    elif operator == "2":
        print (f"{number1} - {number2} = {number4}")

    elif operator == "3":
        print (f"{number1} * {number2} = {number5}")

    elif operator == "4":
        print (f"{number1} / {number2} = {number6}")

    elif operator == "5":
        print (f"{number1} // {number2} = {number7}")

    elif operator == "6":
        print (f"{number1} % {number2} = {number8}")
    
    else:
        print ("Operator not found. Please try again.")
        print ()
    print ()
    print ("Do you want continue?")
    print ("1. Yes")
    print ("2. No")
    yn = input("insert: ")
    if yn == "1":
        print ()
        print ("I am happy!")
        print ()
        continue
    else:
        print ("All good!")