GEWONNEN = 3
VERLOREN = 0

def intinput():
    while True:
        try:
            x = int( input("Voer een nummer in: "))
            return x
        except:
            print("Voer een geldig nummer in")

groepA = []
while True:
    land = input("Voer hier een land in\n").lower()
    if land not in groepA:
        groepA.append(land)
        if len(groepA) >= 3:
            break
    else:
        print("Nieuw land invoeren!")

print(f"Wedstrijd 1 score {groepA[0]} - {groepA[1]}")
print(f"Score {groepA[0]}")
score1 = intinput()
print(f"Score {groepA[1]}")
score2 = intinput()