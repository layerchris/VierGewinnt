# Klassen

- Spiel (Game)
  - Attribute
    - Player
    - Spielfeld
  - Methoden
    - check_draw()
    - check_win()
    - check_horizontal()
    - check_vertical()
    - check_diagonal()
    - switch_player()
    - spielen()
    - spielen_computergegner()

- Spielfeld (Board)
  - Attribute
    - Feld (Numpy Array 6x7)
  - Methoden
    - insert() – Wirft Spielstein in die Spalte ein (falls möglich)
    - print_board() – gibt das Spielfeld in der Konsole aus
        - optional: wir könnten auch mit matplotlib arbeiten und das Feld zeichnen lassen
    - reset_board() - Spielfeld wieder auf leer zurücksetzen

- Spieler (Player)
  - Attribute
    - player_name - Name
    - player_color - Farbe der Spielsteine
    - is_player - ob dieser Spieler ein Mensch oder KI ist


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


# Änderungen im Lauf des Projekts

Wir haben im Zuge des Projekts die Game-Klasse um einige Methoden erweitert (check_win), 
an die wir am Anfang nicht dachten. 

Die Spielfeld-Klasse (Board) wurde auch erweitert um reset funktion.

Spieler ist gleich geblieben.

In der main wurde die Schleife zum tatsächlichen Spielen in die Game-Klasse ausgelagert, 
somit macht man in der Main nur noch die Konfiguration des Spiels.