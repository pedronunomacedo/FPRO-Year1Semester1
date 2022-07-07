def four_in_line(board):
    for row_number, row in enumerate(board):
        for col in range(len(row)):
            # HORIZONTAIS
            if col < len(row) - 3:
                if row[col] != 0 and row[col] == row[col + 1] and row[col + 1] == row[col + 2] and row[col + 2] == row[col + 3]:
                    return set([(row_number, col), (row_number, col + 3)])
            # VERTICAIS
            if row_number < len(board) - 3:
                if board[row_number][col] != 0 and board[row_number][col] == board[row_number + 1][col] and board[row_number + 1][col] == board[row_number + 2][col] and board[row_number + 2][col] == board[row_number + 3][col]:
                    return set([(row_number, col), (row_number + 3, col)])
            # DIAGONAL 1
            if row_number < len(board) - 3 and col < len(row) - 3:
                if board[row_number][col] != 0 and board[row_number][col] == board[row_number + 1][col + 1] and board[row_number + 1][col + 1] == board[row_number + 2][col + 2] and board[row_number + 2][col + 2] == board[row_number + 3][col + 3]:
                    return set([(row_number, col), (row_number + 3, col + 3)])
            # DIAGONAL 2
            if row_number > 2 and col < len(row) - 3:
                if board[row_number][col] != 0 and board[row_number][col] == board[row_number - 1][col + 1] and board[row_number - 1][col + 1] == board[row_number - 2][col + 2] and board[row_number - 2][col + 2] == board[row_number - 3][col + 3]:
                    return set([(row_number, col), (row_number - 3, col + 3)])
    return set()

print(four_in_line([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 2, 0, 0], [0, 0, 2, 2, 0], [0, 1, 1, 1, 1], [0, 1, 1, 1, 2]]))