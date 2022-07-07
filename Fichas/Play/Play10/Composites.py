def get_composites(n):
    for i in range(4, n+1):
        if not prime(i):
            yield(i)
            
def prime(i):
    for j in range(2,i):
        if i % j == 0:
            return False
    return True


print(list(get_composites(6)))