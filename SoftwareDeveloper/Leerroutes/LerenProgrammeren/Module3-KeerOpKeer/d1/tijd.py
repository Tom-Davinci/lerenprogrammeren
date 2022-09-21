uur = 1
for uurteller in range (1, 25):
    if uur == 13:
        uur = 1
    if uurteller <= 12:
        print(f"Het is {uur}AM")
    elif uurteller >= 13:
        print(f"Het is {uur}PM")
    else:
        break
    uur += 1