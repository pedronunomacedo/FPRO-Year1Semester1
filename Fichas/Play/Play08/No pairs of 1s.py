def no_consecutives1(k, n = 0, count = 0):
    if n > 2 ** k - 1:
        return count
    else:
        if '11' not in bin(n):
            count += 1
        n += 1
        return no_consecutives1(k, n, count)
    
print(no_consecutives1(7))