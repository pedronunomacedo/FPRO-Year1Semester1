pos = (8, 4)
steps = ['down', 'down', 'left', 'left', 'up', 'up']

def find_treasure(pos, steps):
    
    list_pos = []
    
    for cord in pos:
        list_pos.append(cord)  # [8, 4]
    
    
    
    x = list_pos[0]  # 8
    y = list_pos[1]  # 4
    
    for step in steps:
        if step == 'up':
            y += 1
        elif step == 'down':
            y -= 1
        elif step == 'right':
            x += 1
        else:
            x -= 1
    
    
    
    lista_final = []
    
    lista_final.append(x)
    lista_final.append(y)
    
    return tuple(lista_final)

print(find_treasure(pos, steps))