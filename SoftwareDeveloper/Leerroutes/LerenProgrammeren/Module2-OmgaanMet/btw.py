def btw(x, btw):
    y = x * btw
    x += y
    return x

print( btw(100, 0.09) )