def comprehensions(i, j):
    import math
    
    lista = [x for x in range(i, j + 1) if x % 10 in (3, 8)]
    # [48, 53]
    
    dict = {k: chr(k) for k in range(i, j + 1)}
    
    a_tupla = tuple([round(math.sqrt(num), 2) for num in range(i, j + 1)])
    
    return (lista, a_tupla, dict)
    
print(comprehensions(48, 57))