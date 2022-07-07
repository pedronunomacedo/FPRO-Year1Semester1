t = [84.56, 79.7, 81.14, 82.4, 82.04]

def to_celsius(t):
    return list(map(lambda x: round((x - 32) * (5/9) , 2), t))

print(to_celsius(t))