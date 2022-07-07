def count_zeros(f):
    alist = f()
    return alist.count(0)

print(count_zeros(lambda: [1]*800000 + [0]*56000000))