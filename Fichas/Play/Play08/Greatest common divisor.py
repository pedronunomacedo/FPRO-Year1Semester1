n1 = 18
n2 = 30

def gcd_rec(n1, n2):
    r = n1 % n2
    if r == 0:
        return n2
    else:
        return gcd_rec(n2, r)

    
print(gcd_rec(n1, n2))
        