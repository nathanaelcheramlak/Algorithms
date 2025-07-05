# Minimax Algorithm 
import random

class TicTacToe:
    def __init__(self):
        self.board = [["." for j in range(3)] for i in range(3)]
        self.home = 'X'
        self.away = 'O'
        self.turn = self.home

    def get_available_space(self, board):
        space = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.':
                    space.append((i, j))
        return space

    def is_space_available(self, board):
        return self.get_available_space(board) != []
    
    def get_random_move(self):
        available_spaces = self.get_available_space(self.board)
        return random.choice(available_spaces)

    def check_winner(self, board):
        """Retruns 1 if home wins, -1 if away wins and 0 else"""
        # Row Check
        for row in board:
            if len(set(row)) == 1 and row[0] == self.home:
                return 1 
            if len(set(row)) == 1 and row[0] == self.away:
                return -1

        # Col Check 
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col]:
                if board[0][col] == self.home:
                    return 1
                if board[0][col] == self.away:
                    return -1
        
        # Diagonal Check
        if (board[0][0] == board[1][1] == board[2][2]) or (board[2][0] == board[1][1] == board[0][2]):
            if board[1][1] == self.home:
                return 1
            if board[1][1] == self.away:
                return -1
        
        return 0
    
    def minimax(self, board, is_home_turn, depth):
        winner = self.check_winner(board)
        if winner > 0:
            return winner
        if winner < 0:
            return winner
        
        if not self.is_space_available(board):
            return 0
        
        available_spaces = self.get_available_space(board)
        if is_home_turn:
            best_move_score = float('-inf')
            for i, j in available_spaces:
                board[i][j] = self.home
                best_move_score = max(best_move_score, self.minimax(board, False, depth + 1))
                board[i][j] = '.'
            return best_move_score 
        else:
            best_move_score = float('inf')
            for i, j in available_spaces:
                board[i][j] = self.away
                best_move_score = min(best_move_score, self.minimax(board, True, depth + 1))
                board[i][j] = '.'
            return best_move_score 

    def find_best_move(self, board, is_home_turn):
        available_spaces = self.get_available_space(board)

        best_move = None
        best_move_score = 0
        for i, j in available_spaces:
            board[i][j] = self.home if is_home_turn else self.away
            score = self.minimax(board, not is_home_turn, 0) 
            board[i][j] = '.'
            
            if is_home_turn:
                if score >= best_move_score:
                    best_move = (i, j)
                    best_move_score = score
            else:
                if score <= best_move_score:
                    best_move = (i, j)
                    best_move_score = score

        return best_move if best_move != None else self.get_random_move()
    
    def make_move(self, i, j):
        if self.board[i][j] != '.':
            return False
        self.board[i][j] = self.turn
        self.turn = self.home if self.turn == self.away else self.away
        return False
    
    def run(self):
        print("Instructions: Enter your move as row,col (for example: 1,2). Type 'help' to get the best move suggestion.")
        print("Current board:")
        print(*self.board, sep='\n')

        while self.is_space_available(self.board):
            response = input(f"\n{self.turn}'s turn. Enter move or 'help': ").strip().lower()

            if response == 'help':
                move = self.find_best_move(self.board, self.turn == self.home)
                print(f"Suggested move: {move[0]}, {move[1]}")
                continue

            try:
                i, j = map(int, response.split(','))
            except ValueError:
                print("Invalid input. Please enter your move in the format row,col (e.g. 0,2).")
                continue

            if not (0 <= i < 3 and 0 <= j < 3):
                print("Invalid move. Row and column must be between 0 and 2.")
                continue

            if self.board[i][j] != '.':
                print("That space is already taken. Choose another move.")
                continue

            self.make_move(i, j)
            print("\nCurrent board:")
            print(*self.board, sep='\n')

            winner = self.check_winner(self.board)
            if winner != 0:
                print(f"\n{self.home if winner == 1 else self.away} wins!")
                return

        print("\nIt's a draw!")


if __name__ == "__main__":
    game = TicTacToe()
    game.run()