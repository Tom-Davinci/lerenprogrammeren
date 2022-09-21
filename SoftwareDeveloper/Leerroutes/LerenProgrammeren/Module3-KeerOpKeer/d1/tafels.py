while True:
    try:
        x = int (input("Welk getal wilt u de tafels van? "))
        break
    except:
        print("voer een heel getal in.")

for i in range (1,11):
    print(i * x)