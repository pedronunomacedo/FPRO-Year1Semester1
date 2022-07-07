n = 14


# def list_of_divisors(n):    # [2, 4, 6]
#     i = 1
#     n_divisors = 0
    
#     list_divisors = [1]
#     while i <= n:
#         if i % 2 == 0:
#             n_divisors += 1
#             list_divisors.append(i)
#         i += 1
    
#     return list_divisors

def ugly(n):
    if n == 1:
        return True
    while (n%2 == 0):
        n /= 2
    while (n%3 == 0):
        n /= 3
    while (n%5 == 0):
        n /= 5
    if (n == 1):
        return True
    else:
        return False
    
print(ugly(n))