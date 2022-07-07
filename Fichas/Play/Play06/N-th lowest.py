l = [1, 2, 3, 4, 5, 6, 7, 8]
def rotate_list(l):
    new_list = []
    if len(l) >= 3:
        for i in range(len(l)):
            new_list.append(l[i+(-len(l)+3)])
        return new_list
    else:
        return l

print(rotate_list(l))