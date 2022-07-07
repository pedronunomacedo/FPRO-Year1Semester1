intlist = [(1,1), (3,5), (10,15)]

def generator(intlist):
    r = []
    for i in intlist:
        for j in range(i[0], i[1]+1):
            r.append(j)
    for i in r:
        yield i

print(generator(intlist))