dict = {'Magenta': '#FF00FF', 'Red': '#FF0000', 'White': '#FFFFFF'}

def sort_by_value(dict):
    resultado = []
    
    values = list(dict.values())  # ['#FF00FF', '#FF0000', '#FFFFFF']
    values_ord = sorted(values)   # ['#FF0000', '#FF00FF', '#FFFFFF']
    
    
    
    lista_dict = []
    for key, value in dict.items():
    
        lista1 = []
        lista1.append(key)
        lista1.append(value)
    
        lista_dict.append(lista1)  # [['Magenta', '#FF00FF'], ['Red', '#FF0000'], ['White', '#FFFFFF']]
    



    for elem in range(len(values_ord)):
        for hexa in range(len(lista_dict)):
            if lista_dict [hexa][1] == values_ord[elem]:
                tupla = (lista_dict[hexa][0], values_ord[elem])
                resultado.append(tupla)
    
    return resultado

print(sort_by_value(dict))