def floatinput(maat): #string
    while True:
        try:
            x = float( input(f"Voer hier de {maat} van het zwembad in: "))
            return x
        except:
            print("Geldig nummer invoeren")

hoogte = floatinput("hoogte")
breedte = floatinput("breedte")
diepte = floatinput("diepte")
afstand = 60

tegel = "rood"
kuub = hoogte * breedte * diepte
vierkant_meter = hoogte * breedte
kosten_uitgraven = round( kuub * 25, 2)
kosten_afvoeren = round( kuub * 32.50, 2)

if afstand < 50:
    if kuub < 20:
        kosten_voorrij = 100 + afstand * 1.25
    else:
        kosten_voorrij = 250 + afstand * 2.15
else:
    if kuub < 20:
        kosten_voorrij = 100 + afstand * 1.15,
    else:
        kosten_voorrij = 250 + afstand * 2.05
kosten_voorrij = round(kosten_voorrij, 2)

if kuub < 20:
    if tegel == "rood":
        kosten_beton = vierkant_meter * 250 + vierkant_meter * 25
    else:
        kosten_beton = vierkant_meter * 250 + vierkant_meter * 100
else:
    if tegel == "rood":
        kosten_beton = vierkant_meter * 200 + vierkant_meter * 20
    else:
        kosten_beton = vierkant_meter * 200 + vierkant_meter * 125
kosten_beton = round(kosten_beton, 2)

kosten_totaal = kosten_uitgraven + kosten_afvoeren + kosten_beton + kosten_voorrij

print(f"Kosten voor een zwembad van {hoogte} bij {breedte} bij {diepte} meter (inhoud: xx m3)")
print(f"Uitgraven: {kosten_uitgraven} eur")
print(f"Afvoeren grond: {kosten_afvoeren} eur")
print(f"Voorrij kosten: {kosten_voorrij} eur")
print(f"Beton + tegel (xx m2) {kosten_beton} eur")
print(f"Totaal: {kosten_totaal} eur")