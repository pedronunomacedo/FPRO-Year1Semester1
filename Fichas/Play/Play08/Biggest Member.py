atuple = ('abc', 'jkl', ('abc', 'z', 'def', ('123', 'jkl')))

def biggest_member(atuple):
    
    for elem in atuple:
        if type(elem) == tuple:
            
            i = biggest_member(elem)
            
            if len(i) > len(atuple):
                atuple = i
    
    return atuple

print(biggest_member(atuple))