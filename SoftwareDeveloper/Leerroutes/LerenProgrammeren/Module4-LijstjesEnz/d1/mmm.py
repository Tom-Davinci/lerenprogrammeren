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
    rnd = random.randint(0, 3)
    mmlist.append(kleuren[rnd])

print("Zak van M&M's: ")
for index in range(0, aantal):
    print(mmlist[index],"M&M")