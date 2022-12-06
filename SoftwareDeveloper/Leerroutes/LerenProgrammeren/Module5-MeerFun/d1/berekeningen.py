def addidtion(num1 : int, num2 : int):
    end = num1 + num2
    return end

def subtraction(num1 : int, num2 : int):
    end = num1 - num2
    return end

def multiplication(num1 : int, num2 : int):
    end = num1 * num2
    return end

def division(num1 : int, num2 : int):
    end = num1 / num2
    return end

def numin():
    while True:
        try:
            num = float( input("Voer een nummer in: "))
            break
        except:
            print("Geldig nummer invoeren")
    return num

firstround = True

n1, n2 = False, False

while True:
    if firstround:
        choice = input("Wat wil je doen?\nA) getallen optellen,\nB) getallen aftrekken,\nC) getallen vermenigvuldigen,\nD) getallen delen\nE) getal ophogen,\nF) getal verlagen,\nG) getal verdubbelen,\nH) getal halveren?\n").lower()
    else:
        choice = input(f"Wil je wat met de uitkomst ({n1}) doen? \nA) getallen optellen,\nB) getallen aftrekken,\nC) getallen vermenigvuldigen,\nD) getallen delen\nE) getal ophogen,\nF) getal verlagen,\nG) getal verdubbelen,\nH) getal halveren\nI) niets\n").lower()

    if choice in ("e", "f"):
        n2 = 1
    elif choice in ("g", "h"):
        n2 = 2
    elif choice == "i":
        quit()
    
    if n1 == False:
        n1 = numin()
    
    if n2 == False:
        n2 = numin()
    
    if choice in ("a", "e"):
        antw = addidtion(n1, n2)
        som = "+"
    elif choice in ("b", "f"):
        antw = subtraction(n1, n2)
        som = "-"
    elif choice in ("c", "g"):
        antw = multiplication(n1, n2)
        som = "x"
    elif choice in ("d", "h"):
        antw = division(n1, n2)
        som = "/"
    
    print(f"{n1} {som} {n2} = {antw}")
    n1 = antw
    n2 = False
    firstround = False