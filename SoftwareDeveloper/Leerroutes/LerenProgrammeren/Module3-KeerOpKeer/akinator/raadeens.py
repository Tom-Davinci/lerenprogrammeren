import random

while True:
    try:
        rondes = int( input("Voer in hoeveel rondes u wilt spelen (maximaal 20): "))
        if rondes <= 20 and rondes > 0:
            break
        else:
            print("Boven de 0 en onder de 20!")
    except:
        print("Geldig nummer invoeren!")

score = 0
teller = 1
print("Gok een getal tussen de 0 en 1000!")
while teller <= rondes:
    print(f"Ronde {teller}")
    rndnummer = random.randint(0, 1000)
    aantal_gokken = 1
    while aantal_gokken <= 10:
        while True:
            try:    
                gok = int( input(f"Voer hier je gok in (gok {aantal_gokken}): "))
                break
            except:
                print("Geldig nummer invoeren")
        
        if gok == rndnummer:
            print("Goed geraden! Score + 1")
            score += 1
            aantal_gokken += 10
            break

        if rndnummer > gok:
            afstand = rndnummer - gok
            print("Hoger")
        elif rndnummer < gok:
            afstand = gok - rndnummer
            print("Lager")

        if afstand < 50 and afstand > 20:
            print("Je bent warm") 
        elif afstand < 20:
            print("Je bent heel warm")
        aantal_gokken += 1
    print(f"Het getal was: {rndnummer}")
    print(f"Dit is uw score: {score}")
    if rondes != teller:
        while True:
            nog_een_keer = input("Wilt u nog een keer: ").lower()
            if nog_een_keer in ["ja", "nee"]:
                break
            else:
                print("Geldig antwoord invoeren [Ja, Nee]")
            
        if nog_een_keer == "nee":
            print(f"Uw eindscore was: {score}")
            print("Bedankt voor het spelen!")
    teller += 1

print(f"Uw eindscore was: {score}")
print("Bedankt voor het spelen!")