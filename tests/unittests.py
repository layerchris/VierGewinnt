import unittest
import numpy as np

from core.player import Player
from core.board import Board
from core.game import Game

class TestWin(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Spieler 1", "G", True)
        self.player2 = Player("Spieler 2", "R", True)
        self.board = Board()

    @staticmethod
    def board_draw():
        return np.array([
        ["R", "R", "G", "R", "G", "G", "R"],
        ["G", "G", "R", "G", "R", "R", "G"],
        ["R", "R", "R", "G", "G", "G", "R"],
        ["G", "G", "R", "G", "G", "R", "G"],
        ["R", "R", "G", "R", "R", "R", "G"],
        ["G", "R", "R", "G", "G", "R", "G"]
    ])

    @staticmethod
    def board_win_vertical():
        return np.array([
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            ["G", " ", " ", " ", " ", " ", " "],
            ["G", " ", " ", " ", " ", " ", " "],
            ["G", " ", " ", " ", " ", " ", " "],
            ["G", " ", " ", " ", " ", " ", " "]
        ])

    @staticmethod
    def board_win_horizontal():
        return np.array([
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            ["R", "R", "R", "R", " ", " ", " "]
        ])

    @staticmethod
    def board_win_diagonal_negativ():
        return np.array([
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", "G", " ", " ", " "],
            [" ", " ", "G", " ", " ", " ", " "],
            [" ", "G", " ", " ", " ", " ", " "],
            ["G", " ", " ", " ", " ", " ", " "]
        ])

    @staticmethod
    def board_win_diagonal_positiv():
        return np.array([
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            ["R", " ", " ", " ", " ", " ", " "],
            [" ", "R", " ", " ", " ", " ", " "],
            [" ", " ", "R", " ", " ", " ", " "],
            [" ", " ", " ", "R", " ", " ", " "]
        ])

    @staticmethod
    def board_insert_full_column():
        return np.array([
            ["G", " ", " ", " ", " ", " ", " "],
            ["R", " ", " ", " ", " ", " ", " "],
            ["R", " ", " ", " ", " ", " ", " "],
            ["G", "R", " ", " ", " ", " ", " "],
            ["G", " ", "R", " ", " ", " ", " "],
            ["R", " ", " ", "R", " ", " ", " "]
        ])


    def test_win_vertical(self):
        self.board.board = self.board_win_vertical()
        g = Game(self.player1, self.player2, self.board)
        self.assertTrue(g.check_win(self.player1.player_color) == True)

    def test_win_horizontal(self):
        self.board.board = self.board_win_horizontal()
        g = Game(self.player1, self.player2, self.board)
        self.assertTrue(g.check_win(self.player2.player_color) == True)

    def test_win_diagonal_negativ(self):
        self.board.board = self.board_win_diagonal_negativ()
        g = Game(self.player1, self.player2, self.board)
        self.assertTrue(g.check_win(self.player1.player_color) == True)

    def test_win_diagonal_positiv(self):
        self.board.board = self.board_win_diagonal_positiv()
        g = Game(self.player1, self.player2, self.board)
        self.assertTrue(g.check_win(self.player2.player_color) == True)

    def test_draw(self):
        self.board.board = self.board_draw()
        g = Game(self.player1, self.player2, self.board)
        self.assertTrue(g.check_draw() == True)

    def test_insert_full_col(self):
        self.board.board = self.board_insert_full_column()
        g = Game(self.player1, self.player2, self.board)
        self.assertTrue(self.board.insert(1, self.player1.player_color) == 2)

    def test_insert_out_of_range(self):
        self.board.board = self.board_insert_full_column()
        g = Game(self.player1, self.player2, self.board)
        self.assertTrue(self.board.insert(9, self.player1.player_color) == 1)

    def test_correct_insert(self):
        self.board.board = self.board_insert_full_column()
        g = Game(self.player1, self.player2, self.board)
        self.assertTrue(self.board.insert(3, self.player1.player_color) == 0)
