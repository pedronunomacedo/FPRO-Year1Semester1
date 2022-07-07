board = 'xo \n xo\no  '
player = 'x'

def tic_tac_toe(board,player):
    board = [list(board[x:x+3]) for x in range(0, len(board), 4)]
    # [['x', 'o', ' '], [' ', 'x', 'o'], ['o', ' ', ' ']]
    
    dic = {0:"A", 1:"B", 2:"C"}
    
    for x, line in enumerate(board):
        for y, val in enumerate(line): # Ponto(x,y), sendo que x corresponde ao nº da linha e y ao nº da coluna.
            if val != " ":
                continue
            col = [x[y] for x in board]
            diag1 = {(0,0): board[0][0], (1,1): board[1][1], (2,2): board[2][2]}
            diag2 = {(0,2): board[0][2], (1,1): board[1][1], (2,0): board[2][0]}
            # diag1 = {(0, 0): 'x', (1, 1): 'x', (2, 2): ' '}
            #diag2 = {(0, 2): ' ', (1, 1): 'x', (2, 0): 'o'}
            
            if line.count(player) == 2 or col.count(player) == 2:
                return dic[x] + str(y+1)
            elif ((x,y) in diag1 and (list(diag1.values()).count(player) == 2) or (x,y) in diag2 and (list(diag2.values()).count(player) == 2)):
                return dic[x] + str(y+1)
            
            
print(tic_tac_toe(board, player))