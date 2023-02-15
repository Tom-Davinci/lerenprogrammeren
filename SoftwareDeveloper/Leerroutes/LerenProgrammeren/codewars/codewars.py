def points(games):
    total = 0
    for game in games:
        if game[0] > game[2]:
            total += 3
        elif game[0] == game[2]:
            total += 1
    return total

print(points(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4']))