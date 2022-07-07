pos = (8, 4)
steps = 'down-down-left-left-up-up'

def map(pos,steps):
    x = pos[0]
    y = pos[1]
    steps_2 = steps.split("-")
    for i in steps_2:
        if (i == "right"):
            x += 1
        if (i == "left"):
            x -= 1
        if (i == "up"):
            y += 1
        if (i == "down"):
            y-= 1
        
        output = (x,y)
        
    return output

print(map(pos,steps))