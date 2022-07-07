def unique_values(alist):
    res = set()
    for dic in alist:
        for value in dict.values(dic):
            res.add(value)
    
    return res

print(unique_values([]))
            