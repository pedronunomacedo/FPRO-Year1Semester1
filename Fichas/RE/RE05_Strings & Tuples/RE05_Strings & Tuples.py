def rm_letter_rev(ch, a_string):
        a_string = a_string.replace((ch), "") [::-1]
        return(a_string)

print(rm_letter_rev('b', 'aabbbcc'))



def find_dtype(a_tuple, data_type):
    result = ()
    
    for t in a_tuple:
        if type(t) == data_type:
            result = result + (t, )

    return(result)

print(find_dtype((1, False, 'False', 2.0, 10, '3j'), int))



def palindrome(a_string):
    pal = 0
    for i in range(0,len(a_string)-1):
        for j in range(i+1, len(a_string)):
            c = a_string[i:j+1]
            if c == c[::-1]:
                pal += 1
    return ("The string '{}' contains {} palindrome substrings.").format(a_string,pal)

print(palindrome('mmymm'))



def triplet(atuple):
    empty = ()
    for x, a in enumerate(atuple):
        for y, b in enumerate(atuple):
            for z, c in enumerate(atuple):
                if a + b + c == 0 and x != y and x != z and y != z:
                    return((a, b, c))
    return empty

print(triplet(9, 9, 4, -8, -7, 1, 4, 4, -1, 1, 0))



def sort_rule(data):
    avg_grade = 100 - (float(sum(data[2]))) / (len(data[2]))
    return (avg_grade, data[0], data[1])

def sort_grades(records):
    return (tuple(sorted(records, key = sort_rule)))

print(sort_grades(('Tate', 'up2011111', (50, 60, 40, 30, 80, 100)), ('Jarred', 'up2012112', (60, 45, 29, 31, 42, 81)), ('Ayan', 'up2011112', (59, 61, 71, 52, 37, 0)), ('James', 'up2012111', (60, 60, 60, 70, 55)), ('Tatiana', 'up2013000', (61, 62, 63, 64, 65, 66)), ('Jasper', 'up2013010', (50, 100, 100, 90, 0, 15)), ('Jarrod', 'up2011110', (10, 30, 50, 70, 90, 100))))