dict1 = {1: 3, 7: 1}
dict2 = {1: 3, 7: 1}

def sparse_dot_product(dict1,dict2):
    set_f = set(dict1.keys()) & set(dict2.keys())
    sum = 0
    
    for i in set_f:
        sum += dict1[i] * dict2[i]
    
    return sum

print(sparse_dot_product(dict1,dict2))