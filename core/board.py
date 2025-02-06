import numpy as np

class Board:
    def __init__(self):
        self.board = np.full((6, 7), ' ', dtype=str)

    @staticmethod
    def try_parse_int(zahl : int) -> int:
        try:
            int(zahl)
            return int(zahl)
        except ValueError:
            return -1

    def insert(self, col:int, color:str) -> int:
        col = self.try_parse_int(col) - 1 # check, falls keine Zahl eingegeben wird
        if col < 0 or col > 6:
            print("Die Spalte muss zwischen 1 und 7 sein!")
            return 1
        elif self.board[0][col] != ' ':
            print("Die Spalte ist bereits Voll!")
            return 2
        else:
            # jede Zeile einer Spalte von unten nach oben durchgehen (also von Index 5 bis 0) und an der ersten Stelle
            # wo noch kein Spielstein ist, wird der aktuelle Stein eingefügt
            for i in range(6):
                if self.board[5-i][col] == ' ':
                    self.board[5-i][col] = color
                    break
            return 0

    def print_board(self):
        print(f"-----------------------------------------")
        for row in self.board:
            print("|" + "|".join(row) + "|")
        print(f"-----------------------------------------")


if __name__ == '__main__':
    import player
    print("class Board")

    player1 = player.Player("John", "G", True)
    player2 = player.Player("Horst", "R", True)
    board = Board()

    board.print_board()

    current_player = player1
    while True:
        i = input(f"{current_player.player_name} ist am zug: ")

        if i != "quit" and i != "exit":

            ret = board.insert(i, current_player.player_color)
            board.print_board()

            if current_player == player1 and ret == 0:
                current_player = player2
            elif current_player == player2 and ret == 0:
                current_player = player1
        else:
            break
