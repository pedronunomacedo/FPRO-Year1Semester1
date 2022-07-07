clues = {(-1, 1): (0, 0), (0, 0): (1, 0), (1, 0): (-1, 1)}

def treasure(clues):
    start = (0,0)
    while start in clues:
        value = start
        start = clues[value]
        del clues[value]
    return start

print(treasure(clues))