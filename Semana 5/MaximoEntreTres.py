def maximo(a, b, c):
    if (a >= b >= c) or (a >= c >= b):
        return a
    elif (b >= a >= c) or (b >= c >= a):
        return b
    else:
        return c