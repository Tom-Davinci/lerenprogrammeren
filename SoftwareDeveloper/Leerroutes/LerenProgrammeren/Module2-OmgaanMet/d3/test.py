a = int( input("Wat is a?") )
b = int( input("Wat is b?") )

if a > b:
    max = a
    min = b
    print("het minimum is:", b)
    print("het maximum is:", a)

elif a < b:
    min = a
    max = b
    print("het minimum is:", min)
    print("het maximum is:", max)

else:
    print("a en b zijn even groot!")