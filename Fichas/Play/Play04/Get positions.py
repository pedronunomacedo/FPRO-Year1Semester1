from math import factorial

n = 5

def pascal(n):
    output = ""
    # x = 0
    for i in range(n):
        # x = x + 1
        elem = i + 1
        for j in range(elem):
            output += str(int(factorial(i)/(factorial(j) * factorial(i-j))))
            if (j < i):
                output += " "
            
        output += "\n"
    
    return output

print(pascal(n))