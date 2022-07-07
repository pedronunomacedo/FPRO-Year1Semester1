num = 310909

def greatest(num):
    num_list = []
    n = num
    while n > 9:
        resto = n % 10
        num_list.append(resto)
        n = n // 10
    num_list.append(n)
    
    num_list = sorted(num_list,key=int,reverse=True)
    
    output = 0
    for i in range(len(num_list)):
        output += num_list[i] * (10 **(len(num_list)-1-i))
    
    return output

print(greatest(num))