import random, time

debug = False
UNIVERSAL_TIME_CONTROL = 1

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
def generatePlayers(playerCount : int) -> list:
    players = []

    for player in range(1, playerCount + 1):
        players.append({"playerNr" : player, "hand" : [], "extraDraw" : 0})
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
    skip = False
    turn = 0
    while True:
        print(f"turn: player {turn + 1}")
        time.sleep(UNIVERSAL_TIME_CONTROL)
        player = players[turn]
        player, cardsInplay, deck, reverse, skip = playTurn(player, cardsInplay, deck, players, turn, reverse, skip)
        turn, skip = calcNextturn(players, reverse, turn, skip)

#berekent wie de volgende turn neemt
def calcNextturn(players : list, reverse : bool, turn : int, skip : bool) -> int:
    playerCount = len(players)
    if not skip:
        if not reverse:
            turn += 1
            if turn >= playerCount:
                turn = 0
        else:
            turn -= 1
            if turn <= 0:
                turn = playerCount - 1
        return turn, skip
    
    else:
        if not reverse:
            turn += 2
            if turn == playerCount + 1:
                turn = 1
            elif turn == playerCount:
                turn = 0
        else:
            turn -= 2
            if turn == -1:
                turn = 2
            elif turn == 0:
                turn = 3
        
        skip = False
        return turn, skip        

#pakt kaart uit deck
def drawCard(deck : list, player : dict):
    random.shuffle(deck)
    player["hand"].append(deck[0])
    deck.pop(0)
    print(f"player {player['playerNr']} draws a card")
    time.sleep(UNIVERSAL_TIME_CONTROL)
    return deck, player

#speelt beurt van de speler af
def playTurn(player : dict, cardsInplay : list, deck : list, players : list, turn : int, reverse : bool, skip : bool):
    topCard = findTopCard(cardsInplay)
    playableCards = findPlayableCards(player["hand"], topCard)
    if playableCards == [] or len(playableCards) == 0:
        drawCard(deck, player)
        if player["extraDraw"] > 0:
            for x in range(0, player["extraDraw"]-1):
                drawCard(deck, player)
            player["extraDraw"] = 0
    else:
        optimalCard = findOptimalCard(playableCards, player)
        players, reverse, skip = playCard(player, cardsInplay, optimalCard, players, turn, reverse, deck, skip)
    
    if player["hand"] == []:
        print(f"{player['playerNr']} has won!")
        quit()
    else:
        return player, cardsInplay, deck, reverse, skip

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
def findOptimalCard(playableCards : list, player : dict) -> dict:
    #vind of er pest kaarten of niet zijn
    bullyCards, playableCards = cardSort(playableCards, "bully", "type")
    if debug:
        print(type(bullyCards))

    if player["extraDraw"] > 0:
        sortedCards, bullyCards = cardSort(bullyCards, "+2", "num")
        if len(sortedCards) > 0:
            return sortedCards[0]
        sortedCards, bullyCards = cardSort(bullyCards, "+4", "num")
        if len(sortedCards) > 0:
            return sortedCards[0]

    #kiest willekeurige pestkaart als die er zijn
    if len(bullyCards) > 0:
        return bullyCards[0]
    
    #sorteerd kaarten met kleur en welke grootte ze zijn
    else:
        yellowCards, playableCards = cardSort(playableCards, "yellow", "colour")
        redCards, playableCards = cardSort(playableCards, "red", "colour")
        blueCards, playableCards = cardSort(playableCards, "blue", "colour")
        greenCards, playableCards = cardSort(playableCards, "green", "colour")
        colours = [yellowCards, redCards, blueCards, greenCards]

        playableColours = []
        for colour in colours:
            if len(colour) > 0:
                playableColours.append(len(colour))
        playableColours.sort(reverse=True)

        if len(yellowCards) == playableColours[0]:
            yellowCards.sort(key=lambda x: x['num'], reverse=True)
            return yellowCards[0]
        elif len(redCards) == playableColours[0]:
            redCards.sort(key=lambda x: x['num'], reverse=True)
            return redCards[0]
        elif len(blueCards) == playableColours[0]:
            blueCards.sort(key=lambda x: x['num'], reverse=True)
            return blueCards[0]
        elif len(greenCards) == playableColours[0]:
            greenCards.sort(key=lambda x: x['num'], reverse=True)
            return greenCards[0] 

#sorteert kaarten
def cardSort(cards : list, type : str, sortBy : str) -> list:
    sortedCards = []
    for card in cards:
        if card[sortBy] == type:
            sortedCards.append(card)
            cards.remove(card)
    return list(sortedCards), cards

#speelt optimale kaart
def playCard(player : dict, cardsInplay : list, optimalCard : dict, players : list, turn : int, reverse : bool, deck : list, skip : bool) -> list:
    if optimalCard["colour"] == "black":
        optimalCard = blackPlayer(optimalCard)

    if optimalCard["num"] == "turn":
        if reverse == True:
            reverse = False
        elif reverse == False:
            reverse = True

    if optimalCard["num"] == "skip":
        skip = True

    if optimalCard["num"] == "+2" or optimalCard["num"] == "+4":
        players, player = plusPlayer(optimalCard, players, turn, reverse, player)
    elif optimalCard["num"] != "+2" or optimalCard["num"] != "+4" and player["extraDraw"] > 0:
        for x in range(0, player["extraDraw"]):
            drawCard(deck, player)
        player["extraDraw"] = 0

    cardsInplay.append(optimalCard)
    print(f"player '{player['playerNr']}' plays {optimalCard['colour']} {optimalCard['num']}")
    time.sleep(UNIVERSAL_TIME_CONTROL)
    print(f"player '{player['playerNr']}' has {len(player['hand']) - 1} cards remaining")
    time.sleep(UNIVERSAL_TIME_CONTROL)
    topCard = cardsInplay[len(cardsInplay)-1]
    print(f"top card: {topCard['colour']} {topCard['num']}")
    time.sleep(UNIVERSAL_TIME_CONTROL)
    player["hand"].remove(optimalCard)

    return players, reverse, skip

#kiest kleur wanneer zwarte kaarten gespeeld worden
def blackPlayer(optimalCard : dict) -> dict:
    colours = ["yellow", "red", "blue", "green"]
    random.shuffle(colours)
    optimalCard["colour"] = colours[0]
    return optimalCard

#zorgt dat +2 en +4 iets doen
def plusPlayer(optimalCard : dict, players : list, turn : int, reverse : bool, player : dict) -> list:
    extraExtraDraw = 0 #lol
    if player["extraDraw"] > 0:
        extraExtraDraw = player["extraDraw"]
        player["extraDraw"] = 0
    
    nextPlayer = playerFinder(players, reverse, player)

    if optimalCard["num"] == "+2":
        players[nextPlayer["playerNr"]-1]["extraDraw"] = players[nextPlayer["playerNr"]-1]["extraDraw"] + 2 + extraExtraDraw
    else:
        players[nextPlayer["playerNr"]-1]["extraDraw"] = players[nextPlayer["playerNr"]-1]["extraDraw"] + 4 + extraExtraDraw
    return players, player

#vind speler
def playerFinder(players : list, reverse : bool, player : dict) -> dict:
    num = player["playerNr"]
    if reverse == False:
        nextPlayerNr = num + 1
        if num + 1 == 5:
            nextPlayerNr = 1
    else:
        nextPlayerNr = num - 1
        if num - 1 == 0:
            nextPlayerNr = 4

    for x in players:
        if x["playerNr"] == nextPlayerNr:
            return x

#lijst van kaarten in het spel
#elke beurt 1 kaart genereren

#4 spelers kunnen de turn hebben
#de order is 1, 2, 3, 4 (reverse = False) of 4, 3, 2, 1 (reverse = True)
#elke turn word er 1 kaart gespeelt of 1 kaart gepakt
#als de gespeelde kaart een "bully" kaart is doet het iets speciaals

#altijd pestkaart
#anders hoogste van kleur met meeste