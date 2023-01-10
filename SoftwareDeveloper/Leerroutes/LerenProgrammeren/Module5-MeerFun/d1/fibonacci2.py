amount = int( input("Hoe veel nummers van de fibonacci rij wilt u: "))

def fibonacci(n1, n2, amount):
    if amount > 0:
        next_fibo = n1 + n2
        n1 = n2
        print(n1)
        return fibonacci(n1, next_fibo, amount - 1)
    else:
        return "done"

amount -= 1
print(0)
fibonacci(0, 1, amount)