dagen = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")

print("Alle dagen in de week:")
for index in range(0, 7):
    print(dagen[index])

print("Alle werkdagen in de week:")
for index in range(0, 5):
    print(dagen[index])

print("Alle weekend dagen in de week:")
for index in range(5, 7):
    print(dagen[index])

print("Alle dagen van de week in omgekeerde volgorde:")
for index in range(6, -1, -1):
    print(dagen[index])

print("Alle werkdagen van de week in omgekeerde volgorde:")
for index in range(4, -1, -1):
    print(dagen[index])

print("Alle weekendsagen in de week in omgekeerde volgorde:")
for index in range(6, 4, -1):
    print(dagen[index])