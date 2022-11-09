amount = int( input("Hoe veel nummers van de fibonacci rij wilt u?\n"))

def fibonacci(amount: int):
    num1 = 0
    num2 = 1
    end = [0, 1]
    for x in range(amount - 2):
        next_fibo = num1 + num2
        num1 = num2
        num2 = next_fibo
        end.append(next_fibo)
    return end

x = fibonacci(amount)
length = len(x)
print(f"De fibonacci reeks is: {x}")
print("De gulden snede is:")
print(f"{x[length - 1]} / {x[length - 2]}")
print(x[length - 1] / x[length - 2])