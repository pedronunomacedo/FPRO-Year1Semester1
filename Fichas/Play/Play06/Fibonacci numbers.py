lnum = [42, 234, 135, 21, 232, 12312, -2343]
n = 2

def nth_lowest(lnum,n):
    lnum = sorted(lnum)
    return lnum[n-1]

print(nth_lowest(lnum,n))