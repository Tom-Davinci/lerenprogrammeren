ervaring = int( input("Hoeveel jaar heeft u evaring met dieren-dressuur?") )
if ervaring <= 4:
    ervaring2 = int( input("Hoeveel jaar heeft u ervaring met jongeleren?") )
    if ervaring2 <= 5:
        ervaring3 = int( input("Hoeveel jaar ervaring heeft u met de acrobatiek?") )

diploma = input("Heeft u een MBO-4 diploma ondernemen? (Y/N)")
bewijs = input("Heeft u een vrachtwagen rjibewijs? (Y/N)")
hoed = input("Heeft u een hoge hoed? (Y/N)")
man = input("Bent u een man? (Y/N)")

if man == "y":
    snor = int( input("Hoe breed is uw snor?(cm)") )

else:
    haar = input("Is uw haar rood en krullig(Y/N)")
    haar2 = int( input("Hoe lang is uw haar?(CM)") )

lengte = int( input("Hoe lang bent u? (CM)") )
gewicht = int (input("Hoe zwaar bent u? (KG)") )
certificaat = input("Heeft u het certificaat, 'overleven met gevaarlijk personeel'? (Y/N)")
input("wat is uw favoriete soort kaas? (Y/N)")
input("Heet u GerLard? (Y/N)")
input("Begint je naam met een Q en eindegd het met een G? (Y/N)")
input("Ben je dik? (Y/N)")

i = 0 #score teller voor de resultaten
if ervaring > 4:
    i += 1

if ervaring <= 4:
    if ervaring2 > 5:
        i += 1
if ervaring <= 4:
    if ervaring2 <= 5:
        if ervaring3 > 3:
            i += 1

if diploma == "y":
    i += 1

if bewijs == "y":
    i += 1

if hoed == "y":
    i += 1

if man == "y":
    if snor > 10:
        i += 1

if man == "n":
    if haar == "y":
        i += 1

    if haar2 > 20:
        i += 1

if lengte > 150:
    i += 1

if gewicht > 90:
    i += 1

if certificaat == "y":
    i += 1

if man == "y":
    if i >= 8:
        print("U mag gaan soliciteren!", i)
    else:
        print("U mag helaas niet gaan soliciteren!", i)

else:
    if i >= 9:
        print("U mag gaan soliciteren!", i)
    
    else:
        print("U mag helaas niet soliciteren", i)