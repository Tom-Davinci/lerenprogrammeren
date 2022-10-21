from fruitmand import fruitmand

lengte = 0

for index in range(0, len(fruitmand)):
    test = len( fruitmand[index].get("name"))
    if test > lengte:
        lengte = test

for index in range(0, len(fruitmand)):
    if lengte == len( fruitmand[index].get("name")):
        naam = fruitmand[index].get("name")
        kleur = fruitmand[index].get("color")
        gewicht = fruitmand[index].get("weight")
        break

gewicht /= 1000

kleur_translation = {
    "yellow" : "geele",
    "green" : "groene",
    "red" : "rode",
    "brown" : "bruine",
    "black" : " zwarte",
    "purple" : "paarse",
    "pink" : "roze"
}

kleur = kleur_translation[kleur]

print(f'De "{naam}" ({lengte} letters) heeft een {kleur} kleur en een gewicht van {gewicht} kg.')