from fruitmand import fruitmand

fruitmand.remove(fruitmand[4])

banned_kleuren, kleuren = [], []

for index in range(0, len(fruitmand)):
    if fruitmand[index].get("color") in kleuren:
        banned_kleuren.append( fruitmand[index].get("color")), kleuren.remove( fruitmand[index].get("color"))
    elif fruitmand[index].get("color") not in banned_kleuren:
        kleuren.append( fruitmand[index].get("color"))
print(kleuren)

# dit was eerst prachtig overzichtelijke code
# MAAR NEE het moest weer kleiner worden
# echt jammer dit weer