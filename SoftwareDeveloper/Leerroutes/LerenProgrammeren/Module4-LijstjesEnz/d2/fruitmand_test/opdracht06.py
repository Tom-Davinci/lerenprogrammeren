from fruitmand import fruitmand

for fruit in fruitmand:
    if fruit.get('name') == "appel":
        print(fruit.get('weight'))