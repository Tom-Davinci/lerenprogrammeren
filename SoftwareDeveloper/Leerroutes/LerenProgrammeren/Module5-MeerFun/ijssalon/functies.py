def errInput(msg:str, error:list, trueFalse:bool) -> str:
    while True:
        x = input(msg).lower()
        if bool(x in error) == trueFalse:
            return x
        else:
            print("Dat is geen optie die we aanbieden!")

def intInput(msg:str) -> int:
    while True:
        try:
            x = int( input(msg))
            return x
        except:
            print("Dat is geen optie die we aanbieden!")

def vraagAantalBolletjes(zakelijk:bool) -> int:
    while True:
        if zakelijk:
            aantalBolletjes = intInput("Hoeveel liter ijs wilt u?\n")
        else:
            aantalBolletjes = intInput("Hoeveel bolletjes wilt u?\n")
        if aantalBolletjes > 8:
            print("Te veel bolletjes!")
        elif aantalBolletjes < 1:
            print("Te weinig bolletjes!")
        else:
            return aantalBolletjes

def bepBakjeHoorntje(bolletjes:int, zakelijk:bool) -> str:
    if zakelijk:
        return "null"
    if bolletjes <= 4:
        return errInput("Hoorntje of Bakje?\n",["hoorntje", "bakje"], True)
    else:
        return "bakje"

def addBonnetje(bakjeHoorntje : str, bonnetje : dict, zakelijk:bool) -> dict:
    if zakelijk:
        return bonnetje
    else:
        bonnetje[bakjeHoorntje] += 1
    return bonnetje

def printBonnetje(bonnetje : dict, aantalBolletjes : int, toppings : dict, zakelijk:bool) -> str:
    end = f"-------['Papi Gelatto']-------\n"

    if zakelijk:
        if bonnetje["a"] != 0:
            end += f"Aarbei:   {bonnetje['a']} x $9,80 = ${round(bonnetje['a'] * 9.80, 2)}\n"

        if bonnetje["c"] != 0:
            end += f"Chocolade   {bonnetje['c']} x $9,80 = ${round(bonnetje['c'] * 9.80, 2)}\n"

        if bonnetje["v"] != 0:
            end += f"Vanille:   {bonnetje['v']} x $9,80 = ${round(bonnetje['v'] * 9.80, 2)}\n"

        end += "\n"
        
        end += f"totaal = ${round(aantalBolletjes * 9.80, 2)}\n"
        end += f"btw (6%) = ${round((aantalBolletjes * 9.80) * 0.06, 2)}"
    
    else:
        if bonnetje["a"] != 0:
            end += f"Aarbei:   {bonnetje['a']} x $0,95 = ${round(bonnetje['a'] * 0.95, 2)}\n"
        
        if bonnetje["c"] != 0:
            end += f"Chocolade   {bonnetje['c']} x $0,95 = ${round(bonnetje['c'] * 0.95, 2)}\n"

        if bonnetje["v"] != 0:
            end += f"Vanille:   {bonnetje['v']} x $0,95 = ${round(bonnetje['v'] * 0.95, 2)}\n"

        if bonnetje["bakje"] != 0:
            end += f"bakje(s):   {bonnetje['bakje']} x $0.75= ${round(bonnetje['bakje'] * 0.75, 2)}\n"
    
        if bonnetje["hoorntje"] != 0:
            end += f"hoortnje(s):   {bonnetje['hoorntje']} x $1,25 = ${round(bonnetje['hoorntje'] * 1.25, 2)}\n"

        if toppings["slagroom"] > 0 or toppings["sprinkels"] > 0 or toppings["caraHoorn"] > 0 or toppings["caraBak"]:
            end += toppingBonnetje(toppings)

        end += f"totaal = ${round(aantalBolletjes * 1.10 + bonnetje['bakje'] * 0.75 + bonnetje['hoorntje'] * 1.25, 2)}"
    return end

def smaakBolletjes(aantalBolletjes : int, bonnetje : dict, zakelijk:bool) -> dict:
    for x in range(1, aantalBolletjes + 1):
        if zakelijk:
            smaak = errInput(f"Welke smaak wilt u voor liter #{x}?\nA) Aardbei\nC) Chocolade\nV) vanille\n", ["a","c","v"], True)
        else:
            smaak = errInput(f"Welke smaak wilt u voor bolletje #{x}?\nA) Aardbei\nC) Chocolade\nV) vanille\n", ["a","c","v"], True)
        bonnetje[smaak] += 1
    return bonnetje

def toppingAdd(toppings : dict, bakjeHoorntje : str, aantalBolletjes : int, zakelijk:bool) -> dict:
    if zakelijk:
        return "null"
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
    if toppings == "null":
        return "null"
    total = 0
    total += toppings["slagroom"] * 0.5
    total += toppings["sprinkels"] * 0.3
    total += toppings["caraBak"] * 0.9
    total += toppings["caraHoorn"] * 0.6
    return f"Toppings = ${round(total, 2)}\n"

def zakelijkCheck()-> str:
    zakelijk = errInput("Bent u een 1) particuliere of 2) zakelijke klant?\n", ["particulier", "zakelijk", "1", "2"], True)
    if zakelijk == "particulier" or zakelijk == "1":
        zakelijk = False
    else:
        zakelijk = True
    return zakelijk