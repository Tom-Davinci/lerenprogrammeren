import random
import config

def attack():
    minroll = 1 + config.playerlevel
    maxroll = 10 + config.playerlevel
    damage = random.randint(minroll, maxroll)
    return damage

def heal():
    minroll = 10 + (config.playerlevel)
    maxroll = 25 + (config.playerlevel)
    healing = random.randint(minroll, maxroll)
    return healing

def enemyattack():
    minroll = 1 + config.enemylevel
    maxroll = 5 + config.enemylevel
    damage = random.randint(minroll, maxroll)
    return damage

def enemyheal():
    minroll = 1 + (config.enemylevel)
    maxroll = 5 + (config.enemylevel)
    healing = random.randint(minroll, maxroll)
    return healing

def playerxp():
    if config.playerxp >= 25 + (config.playerlevel * config.playerxp):
        config.playerlevel += 1
        return print(f"You levelled up to level: {config.playerlevel}!")

def continuestory():
    while True:
        x = input("Do you want to continue: ")
        if x in ["yes", "y"]:
            config.storyline += 1
            break
        else:
            print("Please enter a valid response")