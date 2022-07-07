s1 = {2, 3, 4, 5}
s2 = {2, 3, 4, 5, 6}

def lost_element(s1,s2):
    
    list_s1 = list(s1)
    list_s2 = list(s2)
    
    for i_1 in list_s1:
        if i_1 not in list_s2:
            return i_1
    
    for i_2 in list_s2:
        if i_2 not in list_s1:
            return i_2
    

print(lost_element(s1, s2))