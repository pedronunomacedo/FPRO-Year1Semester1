def odd_range(start, stop, step):
    if start % 2 != 0:
        start = start
    else:
        start += 1

    for i in range(start, stop, 2*step):
        yield i
        

print(list(odd_range(0, 20, 2)))