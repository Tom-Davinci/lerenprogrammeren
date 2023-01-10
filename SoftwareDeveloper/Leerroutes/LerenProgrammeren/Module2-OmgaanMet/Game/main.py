import moveset
import random
import config

name = input("Please enter your name: ")
if name == "GerLard":
    raise NameError("Thats the great evil dumbass")
elif name == "debug":
    config.playerhealth = 99999999
    config.playerlevel = 99999999
story = True
encounter = False

while True:
    while encounter == True:
        print(f"{enemy} encounter!")
        turn = 0
        if enemy == "Goblin":
            config.enemyhealth = 25
            config.enemyhealthcap = 25
            config.enemylevel = 0
            config.enemyxp = 25
        
        if enemy == "Doom Tree":
            config.enemyhealth = 50
            config.enemyhealthcap = 50
            config.enemylevel = 3
            config.enemyxp = 40
        
        if enemy == "Doomier Tree":
            config.enemyhealth = 40
            config.enemyhealthcap = 40
            config.enemylevel = 5
            config.enemyxp = 50
        
        if enemy == "GerLard minion":
            config.enemyhealth = 30
            config.enemyhealthcap = 30
            config.enemylevel = 6
            config.enemyxp = 100
        
        if enemy == "Skeleton":
            config.enemyhealth = 40
            config.enemyhealthcap = 40
            config.enemylevel = 3
            config.enemyxp = 50
        
        if enemy == "Dancing Zombie":
            config.enemyhealth = 50
            config.enemyhealthcap = 50
            config.enemylevel = 6
            config.enemyxp = 100
        
        if enemy == "Annoying ass Spider":
            config.enemyhealth = 10
            config.enemyhealthcap = 10
            config.enemylevel = 10
            config.enemyxp = 10
        
        if enemy == "GerLard the Tyrant!":
            config.enemyhealth = 1000
            config.enemyhealthcap = 1000
            config.enemylevel = 1000
            config.enemyxp = 1000000
            config.playerhealth = 9999
            config.playerlevel = 9999

        while True:
            if config.enemyhealth <= 0:
                print(f"You kill the {enemy} for {config.enemyxp} xp!")
                config.playerxp += config.enemyxp
                moveset.playerxp()
                encounter = False
                story = True
                config.storyline += 1
                break
            if config.playerhealth <= 0:
                print("You died start over!")
                quit()
            print(f"{enemy} health: {config.enemyhealth}")
            print(f"Player health: {config.playerhealth}")

            while turn == 0:
                move = input("What do you do? [ATTACK, HEAL]").lower()
                if move in ["a","attack","hit"]:
                    damage = moveset.attack()
                    print(f"You damage the {enemy} for: {damage}")
                    config.enemyhealth -= damage
                    turn += 1
                elif move in ["h","heal","restore"]:
                    healing = moveset.heal()
                    print(f"You heal yourself for {healing}")
                    config.playerhealth += healing
                    if config.playerhealth >= config.maxplayerhealth:
                        config.playerhealth = config.maxplayerhealth
                    turn += 1
                elif move == "quit":
                    quit()
                else:
                    print("Please input a valid move!")

            while turn == 1:
                enemyrng = random.randint(0, 100)
                if enemyrng <= 90:
                    damage = moveset.enemyattack()
                    print(f"The {enemy} hits you for: {damage}")
                    print("----------------------------------")
                    config.playerhealth -= damage
                    turn -= 1
                elif enemyrng > 90:
                    healing = moveset.enemyheal()
                    print(f"The enemy heals itself for {healing}")
                    print("----------------------------------")
                    config.enemyhealth += healing
                    if config.enemyhealth >= config.enemyhealthcap:
                        config.enemyhealth = config.enemyhealthcap
                    turn -= 1
    while story == True:
        if config.storyblock == 0:
            if config.storyline == 0:
                print("In the kingdom of the evil tyrant")
                print(f"Lives a hero called {name}")
                print("The evil tyrant reigned with an iron fist, but our hero seeks to stop his tyranny")
                print("Will our great hero survive his/her first encounter? A small goblin!")
                moveset.continuestory()
            elif config.storyline == 1:
                story = False
                encounter = True
                enemy = "Goblin"
            elif config.storyline == 2:
                print("Congratulations on defeating your first enemy!")
                i = 0
                while i == 0:
                    choice1 = input("Does our hero go right, into the sussy forest of DOOM or left, in to the DEATH plains? ").lower()
                    if choice1 in ["right", "r"]:
                        config.storyblock = 1
                        config.storyline = 0
                        i = 1
                    elif choice1 in ["left", "l"]:
                        config.storyblock = 2
                        config.storyline = 0
                        i = 1
                    else:
                        print("Please enter a valid input.")
        if config.storyblock == 1:
            if config.storyline == 0:
                print("Our great hero turns right, into the forest of DOOM")
                print("Scared and afraid of the DOOM around him, our hero surrounded by what looks like living trees!")
                print("Ambush!")
                moveset.continuestory()
            if config.storyline == 1:
                story = False
                encounter = True
                enemy = "Doom Tree"
            if config.storyline == 2:
                print("With the DOOM tree slain, our hero continues")
                print("Our hero gets a whisper in his ear, the name of the great tyrant, the key to defeating him")
                print(f"GerLard, is the tyrants name {name}, slay him!")
                print("A DOOMIER Tree ambuhes our hero")
                moveset.continuestory()
            if config.storyline == 3:
                story = False
                encounter = True
                enemy = "Doomier Tree"
            if config.storyline == 4:
                print("Our brave hero made it out of the deadly forest of DOOM")
                print("It seems GerLard has noticed our heros prescence!")
                print("He sends a minion to deal with you!")
                moveset.continuestory()
            if config.storyline == 5:
                story = False
                encounter = True
                enemy = "GerLard minion"
            if config.storyline == 6:
                print("That was close!")
                print("Our hero heals himself to great effect!")
                print(f"{name} heals himself for 100")
                config.playerhealth = 100
                print(f"GerLard is quite suspicious {name} thinks to himself")
                print("Our player dies because of sus behavior")
                quit()
        if config.storyblock == 2:
            if config.storyline == 0:
                print("Our great hero ventures into the plains of DEATH")
                print(f"Ooooh shiver me timbers {name} thinks to himself")
                print("Scared and 'alone' our hero continues")
                print("The ground shakes beneath our hero a Skeleton pops out of the ground!")
                moveset.continuestory()
            if config.storyline == 1:
                story = False
                encounter = True
                enemy = "Skeleton"
            if config.storyline == 2:
                x = 0
                while x == 0:
                    choice1 = input(f"{name} finds a rare plant, old tales call it the 'devils lettuce' does he take it ?").lower()
                    if choice1 in ["yes", "y"]:
                        config.storyblock = 3
                        config.storyline = 0
                        x += 1
                    if choice1 in ["no", "n"]:
                        config.storyline += 1
                        x += 1
                    else:
                        print("Please input a valid response!")
            if config.storyline == 3:
                print("Our hero decides not to touch the rare plant")
                print("Looking back probably a wise move")
                print("The ground shakes again, a zombie!")
                print("Suddenly thriller by the late MJ starts playing!")
                moveset.continuestory()
            if config.storyline == 4:
                story = False
                encounter = True
                enemy = "Dancing Zombie"
            if config.storyline == 5:
                print("SUUUUUUUUUUUUUUI our hero defeated the Dancing Zombie")
                print("The ground shakes, a trapdoor leading to the basement opens up infront of our hero")
                print("Hero jumps in without fear")
                print("No is that an 'annoying ass spider'")
                print("Ambush!")
                moveset.continuestory()
            if config.storyline == 6:
                story = False
                encounter = True
                enemy = "Annoying ass Spider"
            if config.storyline == 7:
                x = 0
                while x == 0:
                    choice1 = input("Our hero sees a door going to an angel, and a door going to the devil, where does he go? ").lower()
                    if choice1 in ["angel", "a"]:
                        config.storyblock = 4
                        config.storyline = 0
                        x += 1
                    if choice1 in ["devil", "d"]:
                        config.storyline += 1
                        x += 1
                    else:
                        print("Please input a valid response!")
            if config.storyline == 8:
                print("The devil offer you the power of brimstone!")
                print("Our hero cannot resist, but instead of recieving unlimited power")
                print("He died a horrific death and his soul is now suffering endless torment in hell")
                quit()
        if config.storyblock == 3:
            if config.storyline == 0:
                print("Your caracther picks up the devils lettuce")
                print("Immediately rolls it up into a so called blunt")
                print(f"Damn this zaza strong {name} thinks to himself")
                print(f"{name} immediatley gets disctracted from his quest and just spends the rest of his life smoking")
                print("The end!")
                quit()
        if config.storyblock == 4:
            if config.storyline == 0:
                print("Our brave hero goes towards the angel")
                print("But is was a trick there was no angel!")
                print(f"But GerLard the evil tyrant apperead infront of {name}")
                moveset.continuestory()
            if config.storyline == 1:
                encounter = True
                story = False
                enemy = "GerLard the Tyrant!"
            if config.storyline == 2:
                print("Our great hero suddenly very mighty defeats the evil Tyrant!")
                print("Thanks for playing!")
                print("Game end")
                print("-------------------------------------------------------")
    while True:
        end = input("Play again?\n").lower()
        if end in ["y", "yes", "ye"]:
            config.storyblock = 0
            config.storyline = 0
            break
        elif end in ["n", "no",]:
            quit()
        else:
            print("Give a correct input [Y/N]")