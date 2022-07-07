f = lambda n: -1 if n > 31 else 1 if n < 31 else 0
limits = (0, 100)



def find_me(f, limits):
    guesses = 0
    while True:
        guesses += 1
        mid = ((limits[0] + limits[1]) // 2)
        probe = f(mid)
        if probe == 0:
            return guesses
        if probe == -1:  # SMALLER
            limits = (limits[0], mid)
        if probe == 1:
            limits = (mid, limits[1])
    
print(find_me(f, limits))