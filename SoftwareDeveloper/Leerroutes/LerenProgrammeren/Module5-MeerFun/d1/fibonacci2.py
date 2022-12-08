amount = int( input("Hoe veel nummers van de fibonacci rij wilt u?\n"))

def fibonacci(n1, n2, amount):
    if amount > 0:
        n1 = n2
        n2 = n1 + n2
        return fibonacci(n1, n2, amount - 1)
    else:
        return "done"

print( fibonacci(0, 1, amount))