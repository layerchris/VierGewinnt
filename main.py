from core.player import Player
from core.game import Game
from core.board import Board

if __name__ == '__main__':
    player1 = Player("Player 1", "G", True)
    player2 = Player("Player 2", "R", True)
    board = Board()

    while True:
        print("Geben Sie einen Befehl ein: ")
        i = input("> ")
        if i == 'quit':
            break
        elif i == 'help':
            print("Es gibt folgende Befehle: quit, modus, start")
        elif i == 'modus':
            print("Gegen Spieler oder Computergegner? [spieler/computer]")
            gegner = input("> ")
            if gegner == 'computer':
                player2.isPlayer = False
        elif i == 'start':
            print("Spiel gestartet...")
