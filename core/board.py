import numpy as np

class Board:
    def __init__(self):
        self.board = np.full((6, 7), ' ', dtype=str)
