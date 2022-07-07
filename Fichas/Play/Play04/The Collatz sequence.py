n = 12

def collatz(n):
    output = str(n)
    while n > 1:
        if (n%2 == 0):   # n é par(even)
            n = n//2
            if (n == 1):
                output += "," + str(n)
                break
            output += "," + str(n)
        else:            # n é ímpar(odd)
            n = (n * 3) + 1
            output += "," + str(n)
    return output

print(collatz(n))