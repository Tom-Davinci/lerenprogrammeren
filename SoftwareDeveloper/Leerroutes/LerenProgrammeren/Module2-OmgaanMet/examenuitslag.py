while True:
    try:
        scoreE = int( input("Wat is ScoreE?"))
        if scoreE >= 0 and scoreE < 7:
            break
        else:
            print("Score kan alleen van 0-6")
    except:
        print("Alleen score invoeren")
while True:
    try:
        scoreP = int( input("Wat is ScoreP?"))
        if scoreP >= 0 and scoreP < 9:
            break
        else:
            print("Score kan alleen van 0-8")
    except:
        print("Alleen score invoeren")
while True:
    try:
        scoreO = int( input("Wat is ScoreO?"))
        if scoreO >= 0 and scoreO < 6:
            break
        else:
            print("Score kan alleen van 0-5")
    except:
        print("Alleen score invoeren")
while True:
    try:
        scoreS = int( input("Wat is ScoreS?"))
        if scoreS >= 0 and scoreS < 3:
            break
        else:
            print("Score kan alleen van 0-2")
    except:
        print("Alleen score invoeren")

totalscore = scoreE + scoreP - scoreO - scoreS

if scoreP == 8 and scoreE > 4 and scoreO == 0 and scoreS == 0:
    print("De uitlsag is: Goed!")
elif scoreS == 0 and totalscore > 7 and totalscore < 13 or scoreS == 1 and totalscore > 9:
    print("De uitslag is Voldoende!")
else:
    print("De uitslag is Onvoldoende")