def juggler(n, p):
    import math
    
    if p == 0:
        return n
    if juggler(n, p -1) % 2 == 0:
        return int(math.floor((juggler(n, p - 1)) ** (1/2)))
    else:
        return int(math.floor((juggler(n, p - 1)) ** (3/2)))
    
print(juggler(3, 1))