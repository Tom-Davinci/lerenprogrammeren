from fruitmand import fruitmand
import random

while True:
    try:
        aantal = int( input("Voer hier een nummer in: "))
        break
    except:
        print("Geldig nummer invoeren")

for i in range(0, aantal):
    rnd = random.randint(0, len(fruitmand) - 1)
    print(fruitmand[rnd].get("name"))