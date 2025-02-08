from core.board import Board
from core.player import Player
import random
import numpy as np

class Game:
    """Eine Klasse zur Darstellung eines Vier-Gewinnt-Spiels.

        Attribute
        ----------
        player1 : Player
            Der erste Spieler des Spiels.
        player2 : Player
            Der zweite Spieler des Spiels.
        board : Board
            Das Spielfeld.
        num_rows : int
            Anzahl der Reihen im Spielfeld.
        num_columns : int
            Anzahl der Spalten im Spielfeld.
        """
    def __init__(self, p1, p2, b):
        self.player1 = p1
        self.player2 = p2
        self.board = b
        self.num_rows, self.num_columns = self.board.board.shape

    def check_draw(self):
        """Überprüft, ob das Spiel unentschieden ist.

        Returns
        -------
        bool
            True, wenn das Spielfeld vollständig gefüllt ist und kein Spieler gewonnen hat, sonst False.
        """
        if np.all(self.board.board != " "):
            return True

    def check_win(self, player_symbol):
        """Überprüft, ob der angegebene Spieler gewonnen hat.

        Parameter
        ----------
        player_symbol : str
            Das Symbol, das die Spielsteine des Spielers auf dem Spielfeld repräsentiert.

        Rückgabe
        -------
        bool
            True, wenn der Spieler gewonnen hat, sonst False.
        """
        return (
                self.check_horizontal(player_symbol) or
                self.check_vertical(player_symbol) or
                self.check_diagonal(player_symbol)
        )

    def check_horizontal(self, player_symbol):
        """Überprüft eine horizontale Gewinnbedingung.

        Parameter
        ----------
        player_symbol : str
            Das Symbol, das die Spielsteine des Spielers auf dem Spielfeld repräsentiert.

        Rückgabe
        -------
        bool
            True, wenn eine horizontale Gewinnbedingung gefunden wurde, sonst False.
        """
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
        """Überprüft eine vertikale Gewinnbedingung.

        Parameter
        ----------
        player_symbol : str
            Das Symbol, das die Spielsteine des Spielers auf dem Spielfeld repräsentiert.

        Rückgabe
        -------
        bool
            True, wenn eine vertikale Gewinnbedingung gefunden wurde, sonst False.
        """
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
        """Überprüft eine diagonale Gewinnbedingung.

        Parameter
        ----------
        player_symbol : str
            Das Symbol, das die Spielsteine des Spielers auf dem Spielfeld repräsentiert.

        Rückgabe
        -------
        bool
            True, wenn eine diagonale Gewinnbedingung gefunden wurde, sonst False.
        """

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

    def switch_player(self, current_player : Player, board_ret_value : bool) -> Player:
        """Wechselt den aktuellen Spieler, falls der vorherige Zug gültig war.

            Parameters
            ----------
            current_player : Player
                Der derzeitige Spieler.
            board_ret_value : bool
                Rückgabewert des Spielbretts, der angibt, ob der Zug gültig war (0 = gültig).

            Returns
            -------
            Player
                Der neue Spieler, falls der Zug gültig war, ansonsten bleibt der aktuelle Spieler.
            """
        if current_player == self.player1 and board_ret_value == 0:
            return self.player2
        elif current_player == self.player2 and board_ret_value == 0:
            return self.player1
        else:
            return current_player


    def spielen(self):
        """Startet eine Spielsitzung, in der zwei menschliche Spieler abwechselnd spielen."""
        self.board.print_board()

        current_player = self.player1
        while True:
            i = input(f"{current_player.player_name} ist am zug: ")

            if i != "quit" and i != "exit":

                ret = self.board.insert(i, current_player.player_color)
                self.board.print_board()
                if self.check_draw():
                    print(f"Unentschieden!")
                    break
                elif self.check_win(current_player.player_color):
                    print(f"{current_player.player_name} hat gewonnen!")
                    break

                current_player = self.switch_player(current_player, ret)

            else:
                break

    def spielen_computergegner(self):
        """Startet eine Spielsitzung, in der ein Mensch gegen einen Computergegner spielt."""
        self.board.print_board()

        current_player = self.player1
        while True:
            if current_player.is_player:
                i = input(f"{current_player.player_name} ist am zug: ")

                if i != "quit" and i != "exit":
                    ret = self.board.insert(i, current_player.player_color)
                else:
                    break
            else:
                ret = self.board.insert(random.randint(1,7), current_player.player_color)
                while ret != 0:
                    ret = self.board.insert(random.randint(1, 7), current_player.player_color)

            self.board.print_board()

            if self.check_draw():
                print(f"Unentschieden!")
                break
            elif self.check_win(current_player.player_color):
                print(f"{current_player.player_name} hat gewonnen!")
                break

            current_player = self.switch_player(current_player, ret)
