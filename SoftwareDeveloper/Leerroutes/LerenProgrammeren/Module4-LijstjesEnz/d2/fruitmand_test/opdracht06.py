from fruitmand import fruitmand

for index in range(0, len(fruitmand)):
    if fruitmand[index].get("name") == "appel":
        print(fruitmand[index].get("weight"))