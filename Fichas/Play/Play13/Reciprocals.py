def reciprocals(alist):
    finallist = []
    for number in alist:
        try:
            finallist.append(1/number)
        except:
            continue
    return finallist

print(reciprocals([4, 2, 8, 1]))