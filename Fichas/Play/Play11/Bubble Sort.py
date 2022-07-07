def bubble_sort(alist):
    flag = 1
    while flag != 0:
        flag = 0
        for i in range(len(alist)-1):
            if alist[i] > alist[i + 1]:
                 p = alist[i]  # 5
                 alist[i] = alist[i + 1]  # 1
                 alist[i + 1] = p  # 5
                 flag += 1
    return alist

print(bubble_sort([5, 1, 2, 8, 2.5]))