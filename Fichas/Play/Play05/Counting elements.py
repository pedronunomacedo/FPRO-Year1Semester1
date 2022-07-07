tup = (1, '2', 3, 4.0, 5j)

def count_until(tup):
    for i in range(len(tup)):
        if type(tup[i]) == tuple:
            return i
    
    return -1

print(count_until(tup))