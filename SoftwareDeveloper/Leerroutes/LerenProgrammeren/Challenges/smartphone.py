while True:
    try:
        iphone = round( float( input("Prijs van de iPhone: ") ), 2 )
        break
    except:
        print("Geldig bedrag invoeren")

while True:
    try:
        samsung = round( float( input("Prijs van de Samsung: ") ), 2)
        break
    except:
        print("Geldig bedrag invoeren")

while True:
    try:
        zenfone = round( float( input("Prijs van de Zenfone: ") ), 2)
        break
    except:
        print("Geldig bedrag invoeren")

if iphone > samsung and iphone > zenfone:
    print(f"De iPhone is het duurst, de telefoon kost: {iphone}")
    if samsung > zenfone:
        print(f"De Samsung zit in het midden, de telefoon kost: {samsung}")
        print(f"De Zenfone is het goedkoopst, de telefoon kost: {zenfone}")
    else:
        print(f"De Zenfone zit in het midden, de telefoon kost: {zenfone}")
        print(f"De Samsung is het goedkoopst, de telefoon kost: {samsung}")
elif samsung > iphone and samsung > zenfone:
    print(f"De Samsung is het duurst, de telefoon kost: {samsung}")
    if iphone > zenfone:
        print(f"De iPhone zit in het midden, de telefoon kost: {iphone}")
        print(f"De Zenfone is het goedkoopst, de telefoon kost: {zenfone}")
    else:
        print(f"De Zenfone zit in het midden, de telefoon kost: {zenfone}")
        print(f"De iPhone is het goedkoopst, de telefoon kost: {iphone}")       
elif zenfone > samsung and zenfone > iphone:
    print(f"De Zenfone is het duurst, de telefoon kost: {zenfone}")
    if samsung > iphone:
        print(f"De Samsung zit in het midden, de telefoon kost: {samsung}")
        print(f"De iPhone is het goedkoopst, de telefoon kost: {iphone}")
    else:
        print(f"De iPhone zit in het midden, de telefoon kost: {iphone}")
        print(f"De Samsung is het goedkoopst, de telefoon kost: {samsung}")
else:
    print("De telefoons zijn even duur, kies de iPhone")
    quit()
# kon de berekning van de laatste uitbreiding niet bedenken
# maar geen verrassingen natuurlijk :)

if samsung > 900 and iphone > 900 and zenfone > 900:
    print("Koop geen van de telefoons ze zijn te duur!")
    quit()

advies = round( iphone - samsung, 2)

if advies < 0:
    advies = samsung - iphone
    print(f"Het advies is dus de iPhone te kopen. Deze is namelijk {advies} goedkoper dan de Samsung.")
elif advies > 50:
    print(f"Het advies is dus de Samsung te kopen. Deze is namelijk {advies} goedkoper dan de iPhone.")
elif advies <= 50:
    print(f"Het advies is dus de iPhone te kopen. Deze is namelijk {advies} duurder dan de Samsung.")