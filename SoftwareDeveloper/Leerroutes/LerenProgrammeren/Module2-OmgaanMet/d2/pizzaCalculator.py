#Tom de Boer, pizza calculator

# input, integer gemaakt want een halve pizza is niet mogelijk in dit restaurant
var = 0
while var == 0:
    try:
        small = int( input("Hoeveel small pizza's wilt u?") )
        var += 1
    except:
        print("Heel getal invoeren")

while var == 1:
    try:
        med = int( input("Hoeveel medium pizza's wilt u?") )
        var += 1
    except:
        print("Heel getal invoeren")

while var == 2:
    try:
        large = int( input("Hoeveel large pizza's wilt u?") )
        var += 1
    except:
        print("Heel getal invoeren")

# prijzen van een willekeurig plekje in Albequerque
# round toegevoegd om het te houden in euro
smallcost = round(small * 6.99, 3)
medcost = round(med * 11.99, 3)
largecost = round(large * 12.99, 3)
totalcost = smallcost + medcost + largecost

# output, gemaakt als een bonnetje
print("Pizzaplek Albequerque")
print("Kaaslaan 19, 3187FK")
print("---------------------")
print(small, "X small   ", smallcost)
print(med, "X medium   ", medcost)
print(large, "X large   ", largecost)
print("---------------------")
print("Totaal:", totalcost)