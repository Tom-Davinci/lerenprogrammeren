import random

kleuren = ("oranje", "blauwe", "groene", "bruine")

while True:
    try:
        aantal = int( input("Aantal M&M's in de zak: "))
        break
    except:
        print("Geldig nummer invoeren.")

mmlist = []

for i in range(0, aantal):
    rnd = random.randint(1, 4)
    if rnd == 1:
        mmlist.append(kleuren[0])
    if rnd == 2:
        mmlist.append(kleuren[1])
    if rnd == 3:
        mmlist.append(kleuren[2])
    if rnd == 4:
        mmlist.append(kleuren[3])

print("Zak van M&M's: ")
for index in range(0, aantal):
    print(mmlist[index],"M&M")