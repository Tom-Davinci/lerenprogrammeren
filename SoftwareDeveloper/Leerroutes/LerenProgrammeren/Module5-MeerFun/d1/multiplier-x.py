def multiplier(x : int):
    end = ""
    for i in range(1, 11):
        end += f"{i} x {x} = {x * i}\n"
    return end

amount = int( input("Van welk getal wilt u de tafel zien?\n"))

print(multiplier(amount))