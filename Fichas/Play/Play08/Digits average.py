import math

def average(n):
    return math.ceil((n//10 + n%10) / 2)

def ave(n):
    if n < 100:
        return average(n)
    return ave(n//10)*10 + ave(n%100)

def digits_average(n):
    if n < 10:
        return n
    
    return digits_average(ave(n))

print(digits_average(158))