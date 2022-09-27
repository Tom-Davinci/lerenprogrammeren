while True:
    day = input("Voer hier de dag in: ").lower()
    if day in ["ma","di","wo","do","vr","za","zo"]:
        break
    else:
        print("Afkorting van de dag invoeren [ma, di, wo, enz.].")