def scenario_get(scenarios : list,name : str) -> int:
    for x in range( len(scenarios)):
        if scenarios[x]["name"] == name:
            return x

def ways_chooser(ways : list) -> str:
    awnser_check = []
    for way in ways:
        print(f"{way[0]}. {way}")
        awnser_check.append(way[0])
    while True:
        x = input("Choose a way:\n").lower()
        if x in awnser_check:
            for way in ways:
                if way[0] == x:
                    return way

def wincon(ways : list):
    if ways == "death":
        print("you die")
        return False
    elif ways == "win":
        print("you win!")
        return False
    else:
        return True

def desc_getter(scenarios : list,scenario : int) -> str:
    return scenarios[scenario]["desc"]

def game(scenarios : list, name : str):
    endcon = True
    while endcon:
        scenario = scenario_get(scenarios, name)
        desc = desc_getter(scenarios, scenario)
        print(desc)
        endcon = wincon(scenarios[scenario]["ways"])
        if endcon:
            name = ways_chooser(scenarios[scenario]["ways"])
    print("thanks for playing")