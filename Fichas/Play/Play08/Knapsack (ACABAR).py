money = 1000
products = {'ps4': 350, 'smartphone': 400, 'jacket': 40, 'pc': 600, 'glasses': 75}
wishlist = {'ps4': 1, 'smartphone': 1, 'pc': 1}

def total(products, wishlist):
    total = 0
    for elem in wishlist:
        total += products[elem] * wishlist[elem]
        # total += preço_produto * quantidade_produto
    
    return total


def knapsack(money, products, wishlist):
    if total(products, wishlist) <= money:
        return wishlist
    
    temp = wishlist.copy()
    best = total(products, wishlist)
    for prod in temp:
        temp.pop(prod)   # {'smartphone': 1, 'pc': 1}
        if total(products, temp) > 

print(knapsack(money, products, wishlist))