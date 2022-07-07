matrix = (('X', 'A', 'B', 'N', 'T', 'O'), ('Y', 'T', 'N', 'R', 'I', 'T'), ('U', 'P', 'O', 'M', 'D', 'S'), ('I', 'O', 'H', 'U', 'O', 'O'), ('R', 'T', 'E', 'L', 'Q', 'X'), ('I', 'W', 'J', 'K', 'P', 'Z'))
word = 'PORTO'


def soup(matrix,word):
    # dicionário para introduzir as colunas
    dict = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F"}
    
    # procurar por recursive function
    def find (matrix,i,j,word):
        if matrix[i][j] == word[0]:
            if len(word) == 1:
                return True
            else:
                for (a,b) in [(i - 1, j -1), (i + 1, j + 1), (i - 1, j + 1), (i + 1, j - 1), (i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j)]:
                    if matrix[a][b] == word[1] and a >= 0 and b >= 0:
                        return True and find(matrix,a,b,word[1:])
                        
    
    # apanhar a letra
    for line in range(len(matrix)):
        for column in range(len(matrix)):
            if find(matrix,line,column,word) == True:
                return dict[line] + str(column + 1)
            

print(soup(matrix,word))