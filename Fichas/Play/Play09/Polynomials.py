a = [1, 2, 4]
x = 5

def evaluate(a, x):
    return sum(map(lambda n: n * x ** a.index(n), a))

print(evaluate(a, x))