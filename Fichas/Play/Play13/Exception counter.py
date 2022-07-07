def count_exceptions(f, n1, n2):
    c = 0
    for i in range(n1,n2+1):
        try:
            f(i)
        except:
            c += 1
    return c

print(count_exceptions(lambda x: 1/x, -5, 5))
print(count_exceptions(lambda x: 1/(abs(x)-2), -5, 5))
print(count_exceptions(lambda x: 1/0 if x > 10 else 0, 0, 50))