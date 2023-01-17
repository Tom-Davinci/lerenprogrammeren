def agename() -> list[dict]:
    names = []
    while True:
        name = input("Voer hier een naam in:\n").lower()
        age = input("Voer hier een leeftijd in:\n")
        if age == "stop" or name == "stop":
            break
        else:
            age = int(age)
            names.append({"name" : name , "age" : age})
    return names

names = agename()
for data in names:
    name = data["name"]
    age = data["age"]
    print(f"{name} is {age} jaar")