import random

namen, eind = [], {}

while True:
    naam = input("Voer hier een naam in om toe te voegen:\n").lower()
    if naam in namen:
        print("Naam zit er al in!")
    else:
        namen.append(naam)
    verder = input("Nog een naam?\n").lower()
    if verder in ["n", "no", "nee"]:
        if len(namen) > 2:
            break
        else:
            print("Meer dan 2 namen!")

shuffling = True
while shuffling:
    namen_shuffle = random.sample(namen, len(namen))
    shuffling = False
    for i in range( len(namen)):
        if namen_shuffle[i] == namen[i]:
            shuffling = True

for i in range( len(namen)):
    eind.update({namen[i] : namen_shuffle[i]})

print(eind)