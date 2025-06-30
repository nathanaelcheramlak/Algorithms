def n_queens(n):
    possible_arrangements = []

    col_queens = set()
    forward_diagonal = set()
    backward_diagonal = set()
    def backtrack(row, col, board):
        if row == n:
            answer = list(''.join(row) for row in board)
            possible_arrangements.append(answer)
            return
        if col == n:
            return
        
        if col not in col_queens and row + col not in backward_diagonal and row - col not in forward_diagonal:
            board[row][col] = 'Q'

            col_queens.add(col)
            forward_diagonal.add(row - col)
            backward_diagonal.add(row + col)

            backtrack(row + 1, 0, board)

            col_queens.discard(col)
            forward_diagonal.discard(row - col)
            backward_diagonal.discard(row + col)

            board[row][col] = '.'

        backtrack(row, col + 1, board)

    board = [['.' for j in range(n)] for i in range(n)]
    backtrack(0, 0, board)
    return possible_arrangements

print(n_queens(4))