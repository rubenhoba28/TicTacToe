class Game:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def make_move(self, player, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = player
            if self.check_win(player):
                return f"{player} wins!"
            elif self.check_draw():
                return "It's a draw!"
            self.current_player = 'O' if player == 'X' else 'X'
            return "Next move"
        return "Invalid movee"

    def check_win(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
                    all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or \
                all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def check_draw(self):
        return all(cell != '' for row in self.board for cell in row)
