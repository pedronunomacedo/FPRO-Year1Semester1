def maximum_depth(alist):
    if alist == []:
        return 1
    max = 1
    for x in alist:
        aux = maximum_depth(x) + 1
        if aux > max:
            max = aux
    return max

print(maximum_depth([[], [[]], [], [[]]]))