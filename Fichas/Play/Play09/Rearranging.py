l = [50, -30, 0, -10, 10]

def rearrange(l):
    neg = []
    pos = []
    return list(filter(lambda x: x <= 0, l)) + list(filter(lambda z: z > 0, l))

print(rearrange(l))