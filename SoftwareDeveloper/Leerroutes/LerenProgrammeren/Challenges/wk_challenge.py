GEWONNEN = 3
VERLOREN = 0

groepA = []
while True:
    land = input("Voer hier een land in\n").lower()
    if land not in groepA:
        groepA.append(land)
        if len(groepA) >= 3:
            break
    else:
        print("Nieuw land invoeren!")

print(groepA)