def to_celsius(t):
    return [round((x-32)/1.8 , 1) for x in t]

print(to_celsius([84.56, 79.7, 81.14, 82.4, 82.04]))