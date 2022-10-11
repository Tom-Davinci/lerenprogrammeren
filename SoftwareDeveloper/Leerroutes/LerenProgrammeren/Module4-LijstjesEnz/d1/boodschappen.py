boodschappen = {}
toevoegen = True

while toevoegen:
    item = input("Wat wilt u toevoegen: ").lower()
    while True:
        try:
            aantal = int( input("Hoeveel wilt u toevegen: ") )
            break
        except:
            print("Geldig nummer invoeren!")
    boodschappen.update({item : aantal})
    while True:
        keer = input("Wilt u nog wat aan de lijst toevoegen: ").lower()
        if keer in ["j", "ja"]:
            break
        elif keer in ["n", "nee"]:
            toevoegen = False
            break
        else:
            print("Geldig antwoord invoeren [Ja, Nee]")

print("Dit zijn uw boodschappen:")
for index in range(0, len( list(boodschappen.keys()))):
    aantal = list(boodschappen.keys())[index]
    print(aantal, "x", boodschappen[aantal])