#grappige opdracht :D

geel = input("Is de kaas geel? (Y/N)")

if geel == "n":
    schimmel = input("heeft de kaas blauwe schimmel?(Y/N)")

    if schimmel == "y":
        korst = input("heeft de kaas een korst? (Y/N)")

        if korst == "y":
            print("Blue de Rochbaron")
        
        else:
            print("Foume d'Ambert")
    
    else:
        korst1 = input("heeft de kaas een korst? (Y/N)")

        if korst1 == "y":
            print("Camembert")
        
        else:
            print("Mozzarella")

if geel == "y":
    gaten = input("Zitten er gaten in? (Y/N)")

    if gaten == "y":
        duur = input("Is de kaas belachelijk duur? (Y/N)")

        if duur == "y":
            print("Emmenthaler")
        
        else:
            print("Leerdammer")
    
    else:
        steen = input("Is de kaas hard als steen? (Y/N)")

        if steen == "y":
            print("Parmigiano Reggiano")
        
        else:
            print("Goudse kaas")
