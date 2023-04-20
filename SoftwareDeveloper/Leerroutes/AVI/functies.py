EASY_TEXT = """Ik hou van programmeren. Programmeren is leuk. 
Ik kan veel dingen maken met programmeren. Ik kan een website maken. 
Ik kan een spel maken. Ik kan een chatbot maken. 
Programmeren is niet moeilijk. Ik moet alleen de juiste code schrijven. 
De code moet logisch zijn. De code moet foutloos zijn. Werkende code maakt mij blij. 
Niet-werkende code chagerijnig. Programmeren is een avontuur. Ik leer elke dag iets nieuws met programmeren."""

DIFFICULT_TEXT = """Programmeren is een geweldige activiteit, die je in staat stelt om je creativiteit, 
logica en probleemoplossend vermogen te gebruiken, om allerlei soorten applicaties te maken, 
die nuttig, vermakelijk of zelfs levensveranderend kunnen zijn, afhankelijk van je doel en publiek. 
Het is ook een uitdagende bezigheid, die je voortdurend leert om nieuwe talen, technieken en concepten te leren, 
die je helpen om je code efficiënter, eleganter en robuuster te maken, zonder dat je je ooit hoeft te vervelen of te herhalen. 
Bovendien is het een leuke hobby, die je veel voldoening en plezier kan geven, als je ziet hoe je ideeën tot leven komen op het scherm, als je de interactie met je gebruikers ziet of 
als je de reacties van je vrienden en familie ziet, als je ze verrast met je eigen creaties.
"""

ALLOWED_IN_WORD = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"

# depending on the type of text you wish you get an easy, difficult or text from file.
def getText(choice: str) -> str:
    if choice == 'easy':
        return EASY_TEXT
    elif choice == 'difficult':
        return DIFFICULT_TEXT
    else:
        return getFileContentAsString(choice)

def getFileContentAsString(textFile: str) -> str:
    with open(textFile, 'r') as file:
        content = file.read()
    return content

# opdracht 1
def getNumberOfCharacters(text: str) -> int:
    chars = 0
    for letter in text:
        letter = letter.lower()
        if letter in ALLOWED_IN_WORD:
            chars += 1
    return chars

# opdracht 2
def getNumberOfSentences(text: str) -> int:
    sentences = 0
    for letter in text:
        if letter in ".!?":
            sentences += 1
    return sentences

# opdracht 3
def getNumberOfWords(text: str) -> int:
#    voor het geval dat "u" geen woord is
#    count = 0
#    words = text.split()
#    for word in words:
#        if len(word) > 1:
#            count += 1
#    return count
    return len(text.split())

# AVI score
def getAVIscore(text: str) -> float:
    gem = getNumberOfWords(text) / getNumberOfSentences(text)
    if gem <= 7: # vast een betere manier van dit doen, maar het zal wel
        score = 5
    elif gem > 7 and gem < 8:
        score = 6
    elif gem > 8 and gem < 9:
        score = 7
    elif gem > 10 and gem < 11:
        score = 8
    elif gem == 11:
        score = 11
    elif gem > 11:
        score = 12
    return score