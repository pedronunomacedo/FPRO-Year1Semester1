l1 = ['not found', 'pattern here', 'skip', 'next... or not?']
l2 = ['pattern here indeed', 'i want to be chosen', 'not my day', 'sneakypatternbutitisthere']
p = 'pattern'


def pattern_hunting(l1,l2,p):
    result = []
 
    for i_string_1 in range(len(l1)):
        if p in l1[i_string_1]:
            result.append(l2[i_string_1])
    
    for i_string_2 in range(len(l2)):
        if p in l2[i_string_2]:
            result.append(l1[i_string_2])
            
    return sorted(result, reverse = True)

print(pattern_hunting(l1,l2,p))