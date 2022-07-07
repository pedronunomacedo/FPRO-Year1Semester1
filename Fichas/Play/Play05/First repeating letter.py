names = ('ana', 'bernando', 'carlos')
numbers = (938421028, 916381961, 939090082)
emails = ('ana.serra@gmail.com', 'b1999@hotmail.com', 'up201945321@fe.up.pt')




def iterate_rev(names,numbers,emails):
    output = ''
    
    tuple_list_n=[]
    for n in range(len(names)):
        tuple_list_n.append(names[n])   # ['ana', 'bernando', 'carlos']
    tuple_list_n.reverse() # ['carlos', 'ana', 'bernando']
    
    tuple_list_num = []
    for num in range(len(numbers)):
        tuple_list_num.append(numbers[num])
    tuple_list_num.reverse() 
        
    tuple_list_e = []
    for e in range(len(emails)):
        tuple_list_e.append(emails[e])
    tuple_list_e.reverse()   # ['up201945321@fe.up.pt', 'ana.serra@gmail.com', 'b1999@hotmail.com']
    
    for i in range(len(names)):
        output += str(tuple_list_n[i]) + " - " + str(tuple_list_num[i]) + " - " + str(tuple_list_e[i]) + "\n" 
        
    return output

print(iterate_rev(names,numbers,emails))