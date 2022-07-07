n = 1

def fib(n):
    output = []
    if n == 1:
        output.append(0)
    elif n > 1:
        output = [0,1]
        for i in range(2,n):
            soma = output[i-2] + output[i-1]
            output.append(soma)
    
    return output

print(fib(n))