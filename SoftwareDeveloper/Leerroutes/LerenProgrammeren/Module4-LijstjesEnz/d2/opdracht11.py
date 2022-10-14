from fruitmand import fruitmand

kleuren = []

for index in range(0, len(fruitmand)):
    kleuren.append(fruitmand[index].get("color"))

while True:
    kleur = input("Voer hier een kleur in: ").lower()
    if kleur in kleuren:
        break
    else:
        print(f"De kleur {kleur} zit er niet in de fruitmand")

rond, niet_rond, wel_rond = 0, 0, 0

for index in range(0, len(fruitmand)):
    test = fruitmand[index].get("color")
    if test == kleur:
        if fruitmand[index].get("round"):
            rond += 1
            wel_rond += 1
        else:
            rond -= 1
            niet_rond += 1

if rond > 0:
    print(f"Er zijn {rond} meer ronde vruchten dan niet ronde vruchten in de kleur {kleur}")
elif rond < 0:
    rond = abs(rond)
    print(f"Er zijn {rond} minder ronde vruchten dan niet ronde vruchten in de kleur {kleur}")
else:
    print(f"Er zijn {wel_rond} ronde vruchten en {niet_rond} niet ronde vruchten in de kleur {kleur}")
