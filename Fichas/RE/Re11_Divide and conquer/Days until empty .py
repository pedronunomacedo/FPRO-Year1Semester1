c = 5
l = 2

def days_until_empty(c, l):
    quant = c
    for i in range(1, c):
        quant -= i
        if quant <= 0:
            break
        elif quant + l > c:
            quant = c
        else:
            quant += l
    
    return i
    
print(days_until_empty(c, l))
            