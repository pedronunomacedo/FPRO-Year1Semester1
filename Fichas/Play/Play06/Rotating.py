llists = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]

def fetch_middle(llists):
    output = []  
    for lista in llists:
        if len(lista) % 2 != 0:
            middle = lista[len(lista)//2]
            output.append(middle)
        else:
            middle1 = lista[len(lista)//2]
            middle2 = lista[int(len(lista)/2)-1]
            middle = (middle1 + middle2)/2
            output.append(middle)
    
    return output

print(fetch_middle(llists))