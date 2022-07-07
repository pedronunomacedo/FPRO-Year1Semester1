l1 = [('c', 'd'), ('c', 'e'), ('a', 'b'), ('a', 'd')]
l2 = [('a', 'c'), ('b', 'd')]

def l(nada):
    return nada[0]


def override(l1,l2):
    lets = list(map(lambda a: a[0],l2))
    in_or_not = list(filter(lambda b: b[0] not in lets,l1))
    
    output = in_or_not + l2
    
    
    output.sort(key = l, reverse = False)
    
    return output

print(override(l1,l2))




# def sort_function(atuple):
#     return atuple[0]

# def override(l1, l2):
#     #list of letters with the first elements of each tuple of l2
#     letters = list(map(lambda x: x[0], l2))
    
#     #l1 elemets where their first element is not in letters
#     temp = list(filter(lambda x: x[0] not in letters, l1))
    
#     result = temp + l2
#     result.sort(key = sort_function, reverse = False)
                
#     return result

# print(override(l1,l2))