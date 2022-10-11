import random 

kleuren = ["rood", "blauw", "groen", "geel", "bruin"]
mmdict = {}

while True:
    try:
        aantal = int( input("Hoeveel m&m's zitten in de zak: "))
        break
    except:
        print("Geldig nummer invoeren")

for index in range(0, 5):
    mmdict.update({kleuren[index] : 0})

for index in range(0, aantal):
    rndnum = random.randint(0, 4)
    if rndnum == 0:
        mmdict["rood"] += 1
    elif rndnum == 1:
        mmdict["blauw"] += 1
    elif rndnum == 2:
        mmdict["groen"] += 1
    elif rndnum == 3:
        mmdict["geel"] += 1
    elif rndnum == 4:
        mmdict["bruin"] += 1

print(mmdict)