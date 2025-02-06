from core.player import Player

class Game:
    def __init__(self, p1, p2, b):
        self.player1 = p1
        self.player2 = p2
        self.board = b
        self.num_rows, self.num_columns = self.board.board.shape

    def check_win(self, player_symbol):
        return (
                self.check_horizontal(player_symbol) or
                self.check_vertical(player_symbol) or
                self.check_diagonal(player_symbol)
        )

    def check_horizontal(self, player_symbol):
        for row in range(self.num_rows):
            for col in range(self.num_columns - 3):
                if (
                        self.board.board[row, col] == player_symbol and
                        self.board.board[row, col + 1] == player_symbol and
                        self.board.board[row, col + 2] == player_symbol and
                        self.board.board[row, col + 3] == player_symbol
                ):
                    return True
        return False

    def check_vertical(self, player_symbol : Player):
        for col in range(self.num_columns):
            for row in range(self.num_rows - 3):
                if (
                        self.board.board[row, col] == player_symbol and
                        self.board.board[row + 1, col] == player_symbol and
                        self.board.board[row + 2, col] == player_symbol and
                        self.board.board[row + 3, col] == player_symbol
                ):
                    return True
        return False

    def check_diagonal(self, player_symbol : Player):

        for row in range(self.num_rows - 3):
            for col in range(self.num_columns - 3):
                if (
                        self.board.board[row, col] == player_symbol and
                        self.board.board[row + 1, col + 1] == player_symbol and
                        self.board.board[row + 2, col + 2] == player_symbol and
                        self.board.board[row + 3, col + 3] == player_symbol
                ):
                    return True

        for row in range(3, self.num_rows):
            for col in range(self.num_columns - 3):
                if (
                        self.board.board[row, col] == player_symbol and
                        self.board.board[row - 1, col + 1] == player_symbol and
                        self.board.board[row - 2, col + 2] == player_symbol and
                        self.board.board[row - 3, col + 3] == player_symbol
                ):
                    return True

        return False

    def spielen(self):

        self.board.print_board()

        current_player = self.player1
        while True:
            i = input(f"{current_player.player_name} ist am zug: ")

            if i != "quit" and i != "exit":

                ret = self.board.insert(i, current_player.player_color)
                self.board.print_board()
                if self.check_win(current_player.player_color):
                    print(f"{current_player.player_name} hat gewonnen!")
                    break

                if current_player == self.player1 and ret == 0:
                    current_player = self.player2
                elif current_player == self.player2 and ret == 0:
                    current_player = self.player1
            else:
                break
