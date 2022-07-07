a_list = ['Andre', 'Rui', 'Silva', 'Madalena', 'Leonor', 'Francisco', 'Filomena']
step = 7

def last_man_standing(a_list, step):
    position = 0
    
    while (len(a_list) > 1):
        position = (position + step - 1) % len(a_list)
        a_list.pop(position)
    
    return a_list[0]

print(last_man_standing(a_list, step))