acroi = int( input("Hoeveel croissantjes wilt u?") )
astok = int( input("Hoeveel stokbroden wilt u?") )
akort = int( input("Hoeveel kortings bonnen heeft u?"))

croi = acroi * 0.39
stok = astok * 2.78
kort = akort * 0.5
kost = croi + stok - kort

print("De feestlunch kost je bij de bakker", round(kost, 3), "euro voor de", acroi, "croissantjes en de", astok, "stokbroden als de", akort, "kortingsbonnen nog geldig zijn!")