import random

naam = input("Wat is je naam?\n")
aantal = int( input("Hoeveel complimenten?\n"))

complimenten = [f"Je bent geweldig {naam}!",f"Je bent erg lief {naam}!",f"Je bent super cool {naam}!",f"Super gaaf {naam}!"]

teller = 0
lastrnd = "filler"

while teller <= aantal:
    rnd = random.randint(0, 3)
    if lastrnd != rnd:
        print( complimenten[rnd])
        teller += 1
    lastrnd = rnd