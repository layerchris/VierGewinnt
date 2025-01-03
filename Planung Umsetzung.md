# Klassen

- Spiel (Game)
    - Player
    - Spielfeld
    - checkWin()
    - startGame()

- Spielfeld (Board)
    - Feld (Array 6x7)
    - insert() – Wirft Spielstein in die Spalte ein (falls möglich)
    - printField() – gibt das Spielfeld in der Konsole aus
        - optional: wir könnten auch mit matplotlib arbeiten und das Feld zeichnen lassen

- Spieler (Player)
    - Name
    - Farbe der Spielsteine
    - bool ob dieser Spieler ein Mensch oder KI ist (isPlayer)


# Allgemein
Game Klasse: 

Steuert Ablauf des Spiels, beinhält Regeln und Siegbedingungen


main:

Schleife mit möglichen eingaben 
- Auswahl des Gegners
- Spieler Gegen Spieler
- Spieler gegen Computer
- Spaltennummer als Eingabe für den nächsten Zug, wo soll der nächste Spielstein eingeworfen werden
- Exit – Programm 
