def solve_sudoku(board):
    numeros=[1,2,3,4,5,6,7,8,9]
    for i in range(len(board)):
        for j in range(len(board[1])):
            if board[i][j] == 0:
                vertical = [board[a][j] for a in range(len(board))]
                horizontal = [board[i][b] for b in range(len(board[i]))]
                falta_v= [x for x in numeros if x not in vertical]
                falta_h = [x for x in numeros if x not in horizontal]
                number_to_print = [k for k in falta_v if k in falta_h]
                for n in range(1,300):
                    if n in number_to_print :
                        number_to_print = n
                        break
                board[i][j] = number_to_print
    return board

print(solve_sudoku([[5, 8, 0, 9, 2, 4, 7, 0, 3], [1, 9, 4, 3, 8, 7, 6, 5, 2], [2, 7, 3, 6, 1, 5, 4, 9, 8], [7, 5, 8, 1, 4, 3, 9, 2, 6], [6, 3, 1, 2, 9, 8, 5, 7, 4], [4, 2, 9, 7, 5, 6, 0, 3, 1], [3, 1, 5, 4, 6, 9, 2, 8, 7], [9, 6, 2, 8, 7, 0, 3, 4, 5], [8, 4, 7, 5, 3, 2, 1, 6, 9]]))