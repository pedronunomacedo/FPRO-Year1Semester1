alist = [-1, 111, 1, 11, -1, 11, 1, 111]


def remove_repetidos(alist):

    lista_numeros_unicos = []
    
    for numero in range(len(alist)):
        if(alist[numero] in lista_numeros_unicos): #Verifica se o atual elemento existe na lista original
            pass
        else:
            lista_numeros_unicos.append(alist[numero]) #Se não existir, adiciona com o comando append() o numero na lista

    return lista_numeros_unicos


def most_frequent(alist):
    lista = remove_repetidos(alist)   # [-1, 2, 5, 3, 4]
    
    for num in range(len(lista)):
        
        quantidade = alist.count(lista[num])
        
        if num == 0:
            maior_quant = lista[0]
        elif quantidade > alist.count(maior_quant):
            maior_quant = lista[num]
        elif quantidade == alist.count(maior_quant):
            for i in range(1,len(alist)+1,-1):
                if alist[i] == lista[num]:
                    # indice = i
                    # break
                    
                else:
                    if alist[i] == maior_quant:
                        # indice = i
                        # break
                    
                    
    # return alist[i]

print(most_frequent(alist))                 