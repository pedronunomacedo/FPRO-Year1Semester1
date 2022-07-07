def multiples_of7(n):
    for i in range(0,n):
        if i % 7 == 0:
            yield i

        
# def divisible_by7(i):
#     if i % 7 == 0:
#         return True
#     return False

print(list(multiples_of7(21)))