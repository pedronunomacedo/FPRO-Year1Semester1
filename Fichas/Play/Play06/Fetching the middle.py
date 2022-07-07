dict1 = {1: 3, 7: 1}
dict2 = {1: 3, 7: 1}

def sparse_dot_product(dict1,dict2):
    sum = 0
    for i in dict1:
        for j in dict2:
            if dict1[i] == dict2[j]:
                sum += (dict1[i] * dict2[j])
    
    return sum

print(sparse_dot_product(dict1,dict2))

def sparse_dot_products(dict1,dict2):
    acc = 0
    for k,v in dict.item():
        if k in dict2:
            acc += v * dict2[k]
            
    return acc

print(sparse_dot_product(dict1,dict2))