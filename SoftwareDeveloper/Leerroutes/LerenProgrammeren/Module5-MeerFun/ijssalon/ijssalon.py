from functies import *

nogEen = "ja"
zakelijk = ""
bonnetje = {
    "a" : 0,
    "c" : 0,
    "v" : 0,
    "m" : 0,
    "bakje" : 0,
    "hoorntje" : 0
}

toppings = {
    "slagroom" : 0,
    "sprinkels" : 0,
    "caraHoorn" : 0,
    "caraBak" : 0
}

totaleBolletjes = 0

print("Welkom bij Papi Gelato!")

zakelijk = zakelijkCheck()

while nogEen == "ja":
    aantalBolletjes = vraagAantalBolletjes(zakelijk)
    bonnetje = smaakBolletjes(aantalBolletjes, bonnetje, zakelijk)
    bakjeHoorntje = bepBakjeHoorntje(aantalBolletjes, zakelijk)
    toppings = toppingAdd(toppings, bakjeHoorntje, aantalBolletjes, zakelijk)
    if not zakelijk:
        print(f"Hier is uw {bakjeHoorntje} met {aantalBolletjes} bollen!")
    bonnetje = addBonnetje(bakjeHoorntje, bonnetje, zakelijk)
    totaleBolletjes += aantalBolletjes
    if zakelijk:
        nogEen = "nee"
    else:
        nogEen = errInput("Wilt u nog een keer bestellen?\n", ["ja", "nee"], True)


print(printBonnetje(bonnetje, totaleBolletjes, toppings, zakelijk))