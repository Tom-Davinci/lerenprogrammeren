import random
deck = []
kleuren = ("harten", "klaveren", "schoppen", "ruiten")
nummers = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "heer", "aas")

for index in range(0, 4):
    for i in range(0, 13):
        deck.append(kleuren[index] + " " + nummers[i])

deck.append("joker")
deck.append("joker")
random.shuffle(deck)

for index in range(1, 8):
    print(f"kaart {index}: ", deck[index])
    deck.pop(index)
print("Deck (",len(deck), "kaarten): ", deck)