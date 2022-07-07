alist = [24, 42]

def collisions(alist):
    dic = {}
    for x in alist:
        num = soma(x)
        dic[num] = dic.get(num,0) + 1
    return dic


def soma(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    
    return (sum % 8)



print(collisions(alist))