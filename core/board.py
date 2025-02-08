import numpy as np

class Board:
    """Eine Klasse zur Darstellung des Spielbretts.

    Attribute
    ----------
    board : np.ndarray
        Ein 6x7-Array, das das Spielfeld darstellt.
    """
    def __init__(self):
        self.board = np.full((6, 7), ' ', dtype=str)

    @staticmethod

    def try_parse_int(zahl : int) -> int:
        """Versucht, eine Eingabe in eine Ganzzahl umzuwandeln.

        Parameters
        ----------
        zahl : int
            Der Eingabewert, der überprüft werden soll.

        Returns
        -------
        int
            Die umgewandelte Ganzzahl oder -1 bei Fehler.
        """
        try:
            int(zahl)
            return int(zahl)
        except ValueError:
            return -1

    def insert(self, col:int, color:str) -> int:
        """Fügt einen Spielstein in die angegebene Spalte ein.

              Parameters
              ----------
              col : int
                  Die Spalte, in die der Stein gesetzt werden soll (1-7).
              color : str
                  Die Farbe oder das Symbol des Spielers.

              Returns
              -------
              int
                  0, wenn der Zug erfolgreich war.
                  1, wenn die Spalte außerhalb des gültigen Bereichs liegt.
                  2, wenn die Spalte bereits voll ist.
              """
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
        """Gibt das Spielfeld in der Konsole aus."""
        print(f"-----------------------------------------")
        for row in self.board:
            print("|" + "|".join(row) + "|")
        print(f"-----------------------------------------")

    def reset_board(self):
        """Setzt das Spielfeld zurück, indem es mit leeren Zeichen gefüllt wird."""
        self.board = np.full((6, 7), ' ', dtype=str)