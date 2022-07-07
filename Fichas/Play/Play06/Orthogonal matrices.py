mx = [[-2, 3], [4, -1]]

def is_orthogonal(mx):
    seq = 0
    for linha in mx:
        for elem in linha:
            seq += elem ** 2
        if seq != 1:
            return False
        seq = 0
    return True

print(is_orthogonal(mx))