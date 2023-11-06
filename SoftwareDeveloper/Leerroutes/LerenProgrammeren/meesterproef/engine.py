import random, time

#genereert het deck van 108 kaarten
def generateDeck() -> list:
    deck = []
    colours = ["yellow", "red", "blue", "green"]
    
    for colour in colours:
        deck.append({"num" : 0, "colour" : colour, "type" : "normal"})
        for x in range(1, 10):
            deck.append({"num" : x, "colour" : colour, "type" : "normal"})
            deck.append({"num" : x, "colour" : colour, "type" : "normal"})
        
        for x in range(0, 2):
            deck.append({"num" : "skip", "colour" : colour, "type" : "bully"})
            deck.append({"num" : "+2", "colour" : colour, "type" : "bully"})
            deck.append({"num" : "turn", "colour" : colour, "type" : "bully"})
        
    for x in range(0, 4):
        deck.append({"num" : "colPick", "colour" : "black", "type" : "bully"})
        deck.append({"num" : "+4", "colour" : "black", "type" : "bully"})
    return deck

#genereert de spelers die in het spel zitten
def generatePlayers(playerCount) -> list:
    players = []

    for player in range(1, playerCount + 1):
        players.append({"playerNr" : player, "hand" : []})
    return players

#genereert de startende handen van de spelers
def generateHands(deck : list, players: list) -> list:
    random.shuffle(deck)

    for player in players:
        for x in range(0, 7):
            player["hand"].append(deck[0])
            deck.pop(0)
    return deck, players

#voor simpele integer inputs (waar nodig)
def intInput(max) -> int:
    while True:
        try:
            playerCount = int( input(f"Input amount of players (max {max} players):\n"))
            if playerCount > max:
                print("Too many players")
            else:
                return playerCount
        except:
            print("Only whole numbers")

#genereert de eerste kaart
def generateFirstTopCard(deck) -> list:
    cardsInplay = []
    while deck[0]["type"] == "bully":
        random.shuffle(deck)
    cardsInplay.append( deck[0])
    deck.pop(0)
    return cardsInplay

#opbouw van het spel
def game():
    playerCount = 4 #intInput(4)
    deck = generateDeck()
    players = generatePlayers(playerCount)
    generateHands(deck, players)
    cardsInplay = generateFirstTopCard(deck)
    gameLoop(deck, players, cardsInplay)

   
#main loop van het spel 
def gameLoop(deck : list, players : list, cardsInplay : list):
    reverse = False
    turn = 1
    while True:
        player = players[turn]
        playTurn(player, cardsInplay, deck)
        turn = calcNextturn(players, reverse, turn)
        quit()
    pass

#berekent wie de volgende turn neemt
def calcNextturn(players : list, reverse : bool, turn : int) -> int:
    playerCount = len(players)
    if not reverse:
        turn += 1
        if turn > playerCount:
            turn = 1
    else:
        turn -= 1
        if turn <= 0:
            turn = playerCount
    return turn

#pakt kaart uit deck
def drawCard(deck : list, player : dict):
    random.shuffle(deck)
    player["cards"].append(deck[0])
    deck.pop(0)
    return deck, player

#speelt beurt van de speler af
def playTurn(player : dict, cardsInplay : list, deck : list):
    topCard = findTopCard(cardsInplay)
    playableCards = findPlayableCards(player["hand"], topCard)

    if playableCards == []:
        drawCard(deck, player)
    else:
        optimalCard = findOptimalCard(playableCards)
        print(optimalCard)
        playCard(player, cardsInplay, optimalCard)
    
    if player["hand"] == []:
        playerNr = player["playerNr"]
        print(f"{player} has won!")
        quit()
    else:
        return player, cardsInplay, deck



#vind boventste kaart
def findTopCard(cardsInplay : list) -> dict:
    x = len(cardsInplay) - 1
    topCard = cardsInplay[x]
    return topCard

#vind alle speelbare kaarten in spelers hand
def findPlayableCards(hand : list, topCard : dict) -> list:
    playableCards = []
    for card in hand:
        if card["colour"] == topCard["colour"] or card["num"] == topCard["num"] or card["colour"] == "black":
            playableCards.append(card)
    return playableCards

#vind de beste kaart om te spelen volgens de regels uitgezet
def findOptimalCard(playableCards : list) -> dict:

    #vind of er pest kaarten of niet zijn
    bullyCards = cardSort(playableCards, "bully", "type")

    #kiest willekeurige pestkaart als die er zijn
    if len(bullyCards) > -1:
        return bullyCards[0]
    
    #sorteerd kaarten met kleur en welke grootte ze zijn
    else:
        yellowCards = cardSort(playableCards, "yellow", "colour")
        redCards = cardSort(playableCards, "red", "colour")
        blueCards = cardSort(playableCards, "blue", "colour")
        greenCards = cardSort(playableCards, "green", "colour")
        colours = [len(yellowCards), len(redCards), len(blueCards), len(greenCards)]
        colours.sort()

        if len(yellowCards) == colours[0]:
            yellowCards.sort(key="num", reverse=True)
            return yellowCards[0]
        elif len(redCards) == colours[0]:
            redCards.sort(key="num",reverse=True)
            return redCards[0]
        elif len(blueCards) == colours[0]:
            blueCards.sort(key="num",reverse=True)
            return blueCards[0]
        elif len(greenCards) == colours[0]:
            greenCards.sort(key="num",reverse=True)
            return greenCards[0] 
        

#sorteert kaarten
def cardSort(cards : list, type : str, sortBy : str) -> list:
    sortedCards = []

    for card in cards:
        if card[sortBy] == type:
            sortedCards.append(card)
            cards.remove(card)
    return sortedCards, cards

#speelt optimale kaart
def playCard(player : dict, cardsInplay : list, optimalCard : dict) -> list:
    cardsInplay.append(optimalCard)
    print(player["hand"])
    index = player["hand"].index(optimalCard) #??????????????
    player["hand"].pop(index)
    return player, cardsInplay


#lijst van kaarten in het spel
#elke beurt 1 kaart genereren

#4 spelers kunnen de turn hebben
#de order is 1, 2, 3, 4 (reverse = False) of 4, 3, 2, 1 (reverse = True)
#elke turn word er 1 kaart gespeelt of 1 kaart gepakt
#als de gespeelde kaart een "bully" kaart is doet het iets speciaals

#altijd pestkaart
#anders hoogste van kleur met meeste