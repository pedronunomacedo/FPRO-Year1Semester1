t = [29.2, 26.5, 27.3, 28, 27.8]

def to_fahrenheit(t):
    return list(map(lambda x: round((9/5) * x + 32, 2), t))

print(to_fahrenheit(t))