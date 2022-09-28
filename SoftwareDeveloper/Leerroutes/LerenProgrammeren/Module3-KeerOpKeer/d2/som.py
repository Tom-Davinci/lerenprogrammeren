nummer = 50
totaal = 0
output = " "
while totaal < 1000:
    totaal += nummer
    nummer += 1
    output += f" + {nummer}"
    print(f"{output} = {totaal}")