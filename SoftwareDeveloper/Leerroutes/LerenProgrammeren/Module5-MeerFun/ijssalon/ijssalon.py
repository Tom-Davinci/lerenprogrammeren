from functies import *

nogEen = "ja"
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

while nogEen == "ja":
    aantalBolletjes = vraagAantalBolletjes()
    bonnetje = smaakBolletjes(aantalBolletjes, bonnetje)
    bakjeHoorntje = bepBakjeHoorntje(aantalBolletjes)
    toppings = toppingAdd(toppings, bakjeHoorntje, aantalBolletjes)
    print(f"Hier is uw {bakjeHoorntje} met {aantalBolletjes} bollen!")
    bonnetje = addBonnetje(bakjeHoorntje, bonnetje)
    totaleBolletjes += aantalBolletjes
    nogEen = errInput("Wilt u nog een keer bestellen?\n", ["ja", "nee"], True)

print(printBonnetje(bonnetje, totaleBolletjes, toppings))