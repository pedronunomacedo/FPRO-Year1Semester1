alist = ['Hello', [2, [[], False]], [True]]

def flatten(alist):
    # base case
    if alist == []:
        return []
    
    #recursive calls
    if type(alist[0]) == list:
        return flatten(alist[0]) + flatten(alist[1:])
    else:
            return alist[:1] + flatten(alist[1:])
        

print(flatten(alist))