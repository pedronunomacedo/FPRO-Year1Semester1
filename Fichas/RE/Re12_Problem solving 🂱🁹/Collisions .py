objects = [{'x1': 11, 'y1': 192, 'x2': 59, 'y2': 280}, {'x1': 546, 'y1': 564, 'x2': 629, 'y2': 580}, {'x1': 368, 'y1': 418, 'x2': 455, 'y2': 432}, {'x1': 479, 'y1': 506, 'x2': 577, 'y2': 521}, {'x1': 113, 'y1': 315, 'x2': 156, 'y2': 415}, {'x1': 513, 'y1': 40, 'x2': 537, 'y2': 119}, {'x1': 521, 'y1': 488, 'x2': 549, 'y2': 522}, {'x1': 72, 'y1': 295, 'x2': 122, 'y2': 343}, {'x1': 87, 'y1': 160, 'x2': 135, 'y2': 213}, {'x1': 495, 'y1': 304, 'x2': 524, 'y2': 339}]

def collisions(a,b):
    if a['x2'] < b['x1'] or a['y2'] < b['y1']:
        return False
    if a['y1'] > b['y2'] or a['x1'] > b['x2']:
        return False
    
    return True

def number_of_collisions(objects):
    res = 0
    for obj1 in range(0,len(objects)):
        for obj2 in range(obj1 + 1, len(objects)):
            if collisions(objects[obj1],objects[obj2]):
                res += 1
            else:
                continue
    
    return res

    
    
    
print(number_of_collisions(objects))