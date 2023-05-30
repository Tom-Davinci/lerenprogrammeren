def errInput(msg:str, error:list, trueFalse:bool) -> str:
    while True:
        x = input(msg).lower()
        if bool(x in error) == trueFalse:
            return x
        else:
            print("Dat herken ik niet!")

def intInput(msg:str) -> int:
    while True:
        try:
            x = int( input(msg))
            return x
        except:
            print("Dat herken ik niet!")

def vraagAantalBolletjes() -> int:
    while True:
        aantalBolletjes = intInput("Hoeveel bolletjes wilt u?\n")
        if aantalBolletjes > 8:
            print("Te veel bolletjes!")
        elif aantalBolletjes < 1:
            print("Te weinig bolletjes!")
        else:
            return aantalBolletjes

def bepBakjeHoorntje(bolletjes:int) -> str:
    if bolletjes <= 4:
        return errInput("Hoorntje of Bakje?\n",["hoorntje", "bakje"], True)
    else:
        return "bakje"

def addBonnetje(bakjeHoorntje : str, bonnetje : dict) -> dict:
    bonnetje[bakjeHoorntje] += 1
    return bonnetje

def printBonnetje(bonnetje : dict, aantalBolletjes : int, toppings : dict) -> str:
    end = f"-------['Papi Gelatto']-------\n"

    if bonnetje["a"] != 0:
        end += f"Aarbei:   {bonnetje['a']} x $1,10 = ${round(bonnetje['a'] * 1.10, 2)}\n"

    if bonnetje["c"] != 0:
        end += f"Chocolade   {bonnetje['c']} x $1,10 = ${round(bonnetje['c'] * 1.10, 2)}\n"

    if bonnetje["v"] != 0:
        end += f"Vanille:   {bonnetje['v']} x $1,10 = ${round(bonnetje['v'] * 1.10, 2)}\n"

    if bonnetje["m"] != 0:
        end += f"Munt:   {bonnetje['m']} x $1,10 = ${round(bonnetje['m'] * 1.10, 2)}\n"

    if bonnetje["bakje"] != 0:
        end += f"bakje(s):   {bonnetje['bakje']} x $0.75= ${round(bonnetje['bakje'] * 0.75, 2)}\n"
    
    if bonnetje["hoorntje"] != 0:
        end += f"hoortnje(s):   {bonnetje['hoorntje']} x $1,25 = ${round(bonnetje['hoorntje'] * 1.25, 2)}\n"

    if toppings["slagroom"] > 0 or toppings["sprinkels"] > 0 or toppings["caraHoorn"] > 0 or toppings["caraBak"]:
        end += toppingBonnetje(toppings)

    end += f"totaal = ${round(aantalBolletjes * 1.10 + bonnetje['bakje'] * 0.75 + bonnetje['hoorntje'] * 1.25, 2)}"
    return end

def smaakBolletjes(aantalBolletjes : int, bonnetje : dict) -> dict:
    for x in range(1, aantalBolletjes + 1):
        smaak = errInput(f"Welke smaak wilt u voor bolletje #{x}?\nA) Aardbei\nC) Chocolade\nM) Munt\nV) vanille\n", ["a","c","m","v"], True)
        bonnetje[smaak] += 1
    return bonnetje

def toppingAdd(toppings : dict, bakjeHoorntje : str, aantalBolletjes : int) -> dict:
    topping = errInput("Welke Toppings wilt u:\nSlagroom\nSprinkels\nCaramel\n", ["slagroom", "sprinkels", "caramel"], True)
    if topping == "slagroom":
        toppings[topping] += 1
    elif topping == "sprinkels":
        toppings[topping] += (1 * aantalBolletjes)
    else:
        if bakjeHoorntje == "bakje":
            toppings["caraBak"] += 1
        else:
            toppings["caraHoorn"] += 1
    return toppings

def toppingBonnetje(toppings : dict) -> str:
    total = 0
    total += toppings["slagroom"] * 0.5
    total += toppings["sprinkels"] * 0.3
    total += toppings["caraBak"] * 0.9
    total += toppings["caraHoorn"] * 0.6
    return f"Toppings = ${round(total, 2)}\n"