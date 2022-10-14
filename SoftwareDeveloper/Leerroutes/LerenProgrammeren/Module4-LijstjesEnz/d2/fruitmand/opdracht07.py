from fruitmand import fruitmand

for index in range(0, len(fruitmand)):
    if fruitmand[index].get("round"):
        print(fruitmand[index].get("name"))