def permutations(atuple):
    res = set()
    if len(atuple) == 1:
        return {atuple}
    if len(atuple) == 2:
        atuple_rev = reversed(atuple)
        return {atuple, atuple[::-1]}
    else:
        for i in range(len(atuple)):
            for j in permutations(atuple[:i] + atuple[i+1:]):
                res.add(((atuple[i], ) + j))
        return res
                
        

print(permutations(('A', 'B', 'C')))