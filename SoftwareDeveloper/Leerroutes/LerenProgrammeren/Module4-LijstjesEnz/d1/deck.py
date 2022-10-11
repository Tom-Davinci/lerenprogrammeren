import random
deck = []
kleuren = ("harten", "klaveren", "schoppen", "ruiten")
nummers = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "heer", "aas")

kleur_index = 0
index = 0
while index <= 12 and kleur_index <= 3:
    if index >= 12 and kleur_index < 3:
        kleur_index += 1
        index = -1
    deck.append(kleuren[kleur_index] + " " + nummers[index])
    index += 1

deck.append("joker")
deck.append("joker")
random.shuffle(deck)

for index in range(1, 8):
    print(f"kaart {index}: ", deck[index])
    deck.remove(deck[index])
print("Deck (",len(deck), "kaarten): ", deck)