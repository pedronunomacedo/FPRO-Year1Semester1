s1 = {'abc', 'geeksforgeeks', 'abcdefgh', 'lmnopqrst'}
s2 = {'abcdefghijklmnopqrstuvwxyz', 'ijklmnopqrstuvwxyz', 'defghijklmnopqrstuvwxyz'}

def complete_pairs(s1, s2):
    res = set()
    for i in s1:
        for j in s2:
            a = set(i + j)
            if len(a) == 26:
                res.add(i+j)
    
    return res

print(complete_pairs(s1, s2))