def rearrange(l):
    return [x for x in l if x <= 0] + [y for y in l if y > 0]

print(rearrange([12, 11, -13, -5, 6, -7, 5, -3, -6, 0]))