values = '1,2,3,4,5,6,7,8,9'

def square_odds(values):
    res = ','.join(str(int(x) ** 2) for x in values.split(',') if int(x) % 2 != 0)
    return res

print(square_odds(values))