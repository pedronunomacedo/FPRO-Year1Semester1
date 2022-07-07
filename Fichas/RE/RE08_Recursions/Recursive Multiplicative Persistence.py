n = 39



def md(a):
    if a//10 == 0:
        return a
    return ((a%10)*md(a//10))

def rec_multiplicative_persistence(n):
    if len(str(n)) == 1:
        return 0
    n2 = md(n)
    return (rec_multiplicative_persistence(n2) + 1)

print(rec_multiplicative_persistence(n))