import random 

kleuren = ["rood", "blauw", "groen", "geel", "bruin", "oranje"]
mmdict = {}

while True:
    try:
        aantal = int( input("Hoeveel m&m's zitten in de zak: "))
        break
    except:
        print("Geldig nummer invoeren")

for index in range(0, len(kleuren)):
    mmdict.update({kleuren[index] : 0})

for index in range(0, aantal):
    rndnum = random.randint(len(kleuren) - 1)
    mmdict[kleuren[rndnum]] += 1

print(mmdict)