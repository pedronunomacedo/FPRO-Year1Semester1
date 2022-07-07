path = ['LEFT', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'UP', 'LEFT']

def min_path(path):
    r = [""]
    for i in path:
        if i == "UP" and r[-1]=="DOWN":
            r.pop()
        elif i == "DOWN" and r[-1]=="UP":
            r.pop()
        elif i == "RIGHT" and r[-1]=="LEFT":
            r.pop()
        elif i == "LEFT" and r[-1]=="RIGHT":
            r.pop()
        else:
            r.append(i)
    return r[1:]

print(min_path(path))

