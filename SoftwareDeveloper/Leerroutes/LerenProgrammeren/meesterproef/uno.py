from engine import *

deck = generateDeck()

for card in deck:
    print(card["colour"], card["num"])