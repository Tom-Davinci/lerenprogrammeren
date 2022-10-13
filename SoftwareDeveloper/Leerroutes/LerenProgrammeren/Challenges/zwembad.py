kuub = 8 * 3 * 1.5

kosten_uitgraven = round( kuub * 25, 2)
kosten_afvoeren = round( kuub * 32.50, 2)
kosten_totaal = kosten_uitgraven + kosten_afvoeren

print(f"Kosten voor een zwembad van 8 bij 3 bij 1,5 meter (inhoud: xx m3)")
print(f"Uitgraven: {kosten_uitgraven} eur")
print(f"Afvoeren grond: {kosten_afvoeren} eur")
print(f"Totaal: {kosten_totaal} eur")
