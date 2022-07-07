def multiples_of7(n):
    
    i = 0
    
    while i < n:
        j = i
        i = i + 1
        
        if j % 7 == 0:
            yield j


alist = []
for i in multiples_of7(21):
    alist.append(i)
    
print(alist)