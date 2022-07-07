alist = ['A', 'B', 'C']

def permuta(alist, step = 0):
    res = []
    if len(alist) == 1:
        return [alist]
    elif len(alist) == 2:
        return [alist, [alist[1], alist[0]]]
    else:
        for i in range(len(alist)):
            tmp = alist.copy()
            if i >= step:
                tmp[i], tmp[step] = tmp[step], tmp[i]
            res += ([[tmp[0]] + elem for elem in permuta(tmp[1:])])
        
        return res
    
    
    
print(permuta(alist))