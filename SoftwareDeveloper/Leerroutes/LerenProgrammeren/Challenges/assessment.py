def aantalPoten(giraffen:int, struisvogels:int, zebras:int) -> int:
    poten = (giraffen * 4) + (struisvogels * 2) + (zebras * 4)
    return poten

print(aantalPoten(1, 2, 3))