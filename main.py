from core.player import Player
from core.game import Game
from core.board import Board

if __name__ == '__main__':
    player1 = Player("Spieler 1", "G", True)
    player2 = Player("Spieler 2", "R", True)
    board = Board()

    while True:
        print("Geben Sie einen Befehl ein: ")
        i = input("> ")
        if i == 'quit' or i == 'exit':
            break
        elif i == 'help':
            print("Es gibt folgende Befehle: quit, modus, start")
        elif i == 'modus':
            print("Gegen Spieler oder Computergegner? [spieler/computer]")
            gegner = input("> ")
            if gegner == 'computer':
                player2.is_player = False
                player2.player_name = "Computer"
        elif i == 'start' and player2.is_player:
            spiel = Game(player1, player2, board)
            spiel.spielen()
            board.reset_board()
        elif i == 'start' and not player2.is_player:
            spiel = Game(player1, player2, board)
            spiel.spielen_computergegner()
            board.reset_board()
            player2.is_player = True
            player2.player_name = "Spieler 2"