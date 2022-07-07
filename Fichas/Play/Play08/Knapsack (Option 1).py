money = 1500
products = {'xbox': 250, 'smartphone': 500, 'jeans': 50, 'pc': 600, 'glasses': 100}
wishlist = {'glasses': 3, 'jeans': 2, 'pc': 1, 'xbox': 1}

from itertools import combinations

def knapsack(money, products, wishlist):
    final = []
    
    
    new_list = []
    for item in wishlist:
        for i in range(wishlist[item]):
            new_list.append(item)
    # ['glasses', 'glasses', 'glasses', 'jeans', 'jeans', 'pc', 'xbox']
    
    
    aux = []
    for i in range(1, len(new_list)):
        aux.append(list(combinations(new_list, i)))
    # Lista de todas as combinações possíveis dos elementos da lista
    # new_list
    
    
    for element in aux:
        for sub_elem in element:
            new_wish_list = {}
            money_spent = 0
            for item in sub_elem:
                if item not in new_wish_list.keys():
                    new_wish_list[item] = 1
                else:
                    new_wish_list[item] += 1
                money_spent += products[item]
            final.append([new_wish_list, money_spent])
    final.sort(key = lambda x: x[1], reverse = True)
    decisive_final = list(filter(lambda x: x[1] <= money, final))
    
    
    
    return decisive_final[0][0] 
            
print(knapsack(money, products, wishlist))