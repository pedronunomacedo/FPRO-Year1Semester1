money = 7.71

def change(money):
    dict = {2.0: 0, 1.0: 0, 0.5: 0, 0.2: 0, 0.1: 0, 0.05: 0, 0.02: 0, 0.01: 0}
    for coin in dict.keys():
        contador = 0
        while money >= coin:
            contador += 1
            money = round(money - coin, 2)
        dict[coin] = contador
        
    return dict

print(change(money))