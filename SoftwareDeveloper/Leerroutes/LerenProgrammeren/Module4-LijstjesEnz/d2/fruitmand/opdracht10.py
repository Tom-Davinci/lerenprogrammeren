from fruitmand import fruitmand

gewicht = []

for index in range(0, len(fruitmand)):
    gewicht.append( fruitmand[index].get('weight'))

gewicht.sort(reverse = True)

for index in range(0, len(gewicht)):
    test = gewicht[index]
    for i in range(0, len(fruitmand)):
        if fruitmand[i].get('weight') == test:
            print(fruitmand[i].get('name'), test)