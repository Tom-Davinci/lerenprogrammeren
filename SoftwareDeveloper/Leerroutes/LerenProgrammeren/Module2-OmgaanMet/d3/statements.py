a = int( input("Wat is a?") )
b = int( input("Wat is b?") )

if a > b:
    max = a
    print("a is grootste getal!", max)

elif a < b:
    min = a
    print("a is het kleinste getal", min)

else:
    print("a en b zijn even groot!")