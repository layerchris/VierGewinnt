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
        for row in self.board:
            print("|" + "|".join(row) + "|")


if __name__ == '__main__':
    import player
    print("class Board")

    player1 = player.Player("John", "G", True)
    player2 = player.Player("Horst", "R", True)
    board = Board()
    print(f"----------------------------------------------------------------")
    print(board.print_board())
    print(f"----------------------------------------------------------------")

    while True:

        i = input("Spieler 1 ist am zug: ")

        board.insert(i, player1.playerColor)
        print(board.print_board())
