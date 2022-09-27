tijd = 1
ampm = 0

while tijd < 13:
    if ampm == 0:
        print(f"Het is: {tijd}AM")
    elif ampm == 1:
        print(f"Het is: {tijd}PM")
    if tijd == 12 and ampm == 0:
        tijd = 0
        ampm = 1
    tijd += 1