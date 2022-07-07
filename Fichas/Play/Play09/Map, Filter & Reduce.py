lst = [1, 2, 3, 4, 5, 6, 7, 8]
f1 = lambda i: i % 2 == 0
f2 = lambda i: i**2
f3 = lambda a, b: a+b

from functools import reduce
def map_filter_reduce(lst, f1, f2, f3):
    return reduce(f3, map(f2, filter(f1, lst)))

print(map_filter_reduce(lst, f1, f2, f3))