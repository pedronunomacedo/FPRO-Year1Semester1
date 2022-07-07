# def evaluate(a,x):
#     soma = 0
#     for i in range(len(a)):
#         soma += calculate(a,i,x)
    
#     return soma

# def calculate(a,i,x):
#     return a[i] * (x ** i)


def evaluate(a, x):
    return sum([a[i] * (x**i) for i in range(len(a))])



print(evaluate([1, 2, 4, 6, 8], 2))