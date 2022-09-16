def btw(x: float, btw: float)->float:
    x *= 1 + btw
    return round(x, 2)

print( btw(100, 0.09) )