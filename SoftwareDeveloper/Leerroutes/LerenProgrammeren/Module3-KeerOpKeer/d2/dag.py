dayarr = ["ma","di","wo","do","vr","za","zo"]

while True:
    day = input("Voer hier de dag in: ").lower()
    if day in dayarr:
        break
    else:
        print("Afkorting van de dag invoeren [ma, di, wo, enz.].")

index = 0
while True:
    print(dayarr[index])
    if dayarr[index] == day:
        break
    index += 1