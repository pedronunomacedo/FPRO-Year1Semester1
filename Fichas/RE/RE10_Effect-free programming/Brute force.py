def brute_force(f, l):
    return [(str(p) + str(s) + str(t)) for p in l for s in l for t in l if f(str(p) + str(s) + str(t))]
    
    
print(brute_force(lambda x: x in ('abc', 'bac', 'cab', 'cba'), ['a', 'b', 'c', 'd', 'e']))