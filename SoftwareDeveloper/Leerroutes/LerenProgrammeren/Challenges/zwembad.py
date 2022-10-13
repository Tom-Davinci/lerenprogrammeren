kuub = 8 * 3 * 1.5
afstand = 60

kosten_uitgraven = round( kuub * 25, 2)
kosten_afvoeren = round( kuub * 32.50, 2)
kosten_totaal = kosten_uitgraven + kosten_afvoeren
if afstand < 50:
    if kuub < 20:
        kosten_voorrij = 100 + afstand * 1.25
    else:
        kosten_voorrij = 250 + afstand * 2.15
else:
    if kuub < 20:
        kosten_voorrij = 100 + afstand * 1.15
    else:
        kosten_voorrij = 250 + afstand * 2.05

print(f"Kosten voor een zwembad van 8 bij 3 bij 1,5 meter (inhoud: xx m3)")
print(f"Uitgraven: {kosten_uitgraven} eur")
print(f"Afvoeren grond: {kosten_afvoeren} eur")
print(f"Voorrij kosten: {kosten_voorrij} eur")
print(f"Totaal: {kosten_totaal} eur")