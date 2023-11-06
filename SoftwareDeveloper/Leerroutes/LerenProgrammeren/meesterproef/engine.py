

#genereert het deck van 108 kaarten
def generateDeck() -> list:
    deck = []
    colours = ["yellow", "red", "blue", "green"]
    
    for colour in colours:
        deck.append({"num" : 0, "colour" : colour})
        for x in range(1, 10):
            deck.append({"num" : x, "colour" : colour})
            deck.append({"num" : x, "colour" : colour})
        
        for x in range(0, 2):
            deck.append({"num" : "skip", "colour" : colour})
            deck.append({"num" : "+2", "colour" : colour})
            deck.append({"num" : "turn", "colour" : colour})
        
    for x in range(0, 4):
        deck.append({"num" : "colPick", "colour" : "black"})
        deck.append({"num" : "+4", "colour" : "black"})
    return deck