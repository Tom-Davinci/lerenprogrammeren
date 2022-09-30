# name of student: Tom 
# number of student: 99066335
# purpose of program: Wisselgeld berekenen

toPay = int(float(input('Amount to pay: '))* 100) # Maakt wisselgeld naar een heel getal
paid = int(float(input('Paid amount: ')) * 100) # Doet het zelfde als boven
change = paid - toPay # maakt de variabele "change" het aantal te veel betaald

if change > 0: # Zorgt ervoor, dat er alleen wat gebeurt als er daadwerkelijk geld gewisseld moet worden.
  coinValue = 200 # zorgt voor de initele grootte van kleingeld terug gegeven, dus 50 cent
  
  while change > 0 or coinValue > 0: # doet alleen wat als er nog wisselgeld is te geven, en er nog munten zijn om in te vullen
    nrCoins = change // coinValue # berekent het aantal coins nodig, als het er niet inpast veranderd het, t aantal coins
    nrCoinsReturned = 0

    if nrCoins > 0: # Doet alleen wat als er coins gegeven kunnen worden
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # Laat de gebruiker zien hoeveel coins er maximaal ge returned kunnen worden
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #Vraagt de gebruiker hoeveel coins er gereturned zijn
      change -= nrCoinsReturned * coinValue #Haalt het aantal coins gereturned van change af

# comment on code below: Zorgt ervoor dat het kleingeld gevraagd steeds kleiner word
    if coinValue == 200:
      nr2eurReturned = nrCoinsReturned
      coinValue = 50
    elif coinValue == 50:
      nr50Returned = nrCoinsReturned
      coinValue = 20
    elif coinValue == 20:
      nr20Returned = nrCoinsReturned
      coinValue = 10
    elif coinValue == 10:
      nr10Returned = nrCoinsReturned
      coinValue = 5
    elif coinValue == 5:
      nr5Returned = nrCoinsReturned
      coinValue = 3
    elif coinValue == 3:
      nr3Returned = nrCoinsReturned
      coinValue = 2
    elif coinValue == 2:
      nr2Returned = nrCoinsReturned
      coinValue = 1
    else:
      nr1Returned = nrCoinsReturned
      coinValue = 0

coinarr = [200,50,20,10,5,3,2,1]
returnarr = [nr2eurReturned, nr50Returned, nr20Returned, nr10Returned, nr5Returned, nr3Returned, nr2Returned, nr1Returned]
for index in range(0, len(returnarr)):
  if returnarr[index] > 0:
    print(f"Amount of {coinarr[index]} coins returned: {returnarr[index]}")

if change > 0: # Als er nog change over is print het dat.
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')