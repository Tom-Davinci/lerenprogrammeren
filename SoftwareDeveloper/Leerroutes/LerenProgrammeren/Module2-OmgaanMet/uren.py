#vraaft huidige tijd
#uren dan minuten
#het duurt nog x uur en y minuten tot de dag eindigt

uren = int( input("Hoeveel uren ") )
minuten = int( input("Hoeveel minuten ") )

einduren = 23 - uren
eindminuten = 60 - minuten

print("Nog",einduren, "uren voor dat de dag voorbij is")
print("Nog",eindminuten, "minuten voor dat de dag voorbij is")