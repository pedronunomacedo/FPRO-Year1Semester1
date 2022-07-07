n = 1
boards = [60, 70, 10, 20, 40, 50, 10, 40]

def paint(n, boards):
    if n == 1:
        return sum(boards) # Soma de todos os elementos da lista
    
print(paint(n, boards))