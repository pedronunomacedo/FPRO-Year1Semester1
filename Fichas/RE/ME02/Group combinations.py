astring = 'aghljcb'

def is_pattern(astring):
    substring = 0
    for i in range(len(astring)-1):
        if astring[i+1] > astring[i]:
            substring += 1
        if astring[i+1] < astring[i]:
            substring -= 1
    
    return (substring == 0)

def subpatterns(astring):
    counter = 0
    for step in range(2,len(astring)+1):
        for char_index in range(0,len(astring) - step + 1):
            sub_str = astring[char_index:char_index + step]
            if is_pattern(sub_str):
                counter += 1
                
    return ("The string '{0}' contains '{1}' substring patterns.".format(astring,counter))

print(subpatterns(astring))