pm = 0
uur = 0
for i in range (1, 26):
    if uur == 13:
        uur = 1
        pm += 1
    if pm == 0:
        print(f"Het is {uur}AM")
    else:
        print(f"Het is {uur}PM")
    uur += 1
    i += 1