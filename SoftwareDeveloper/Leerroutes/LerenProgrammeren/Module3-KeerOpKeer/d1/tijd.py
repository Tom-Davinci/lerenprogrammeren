pm = 0
uur = 1
for uurteller in range (1, 25):
    if uur == 13:
        uur = 1
        pm += 1
    if pm == 0:
        print(f"Het is {uur}AM")
    elif pm == 1:
        print(f"Het is {uur}PM")
    else:
        break
    uur += 1