f = lambda x: (1-(x+0.2))*(x+0.2)
n = 10

import math
def bisect(f, n):
    lower = 0
    upper = 1
    
    while n > 0:
        midpoint = (lower + upper) / 2
        
        if (f(lower) > 0 and f(midpoint) > 0) or (f(lower) < 0 and f(midpoint) < 0):
            lower = midpoint
        elif (f(lower) > 0 and f(midpoint) < 0) or (f(lower) < 0 and f(midpoint) > 0):
            upper = midpoint
        
        n -= 1
    
    return round(midpoint, 5)

print(bisect(f, n))