# VierGewinnt
Vier gewinnt ist ein Strategiespiel für 2 Spieler, bei dem abwechselnd, Spielsteine in ein Gitter aus sieben Spalten und sechs Reihen geworfen werden.
Ziel ist es, als erster vier Steine seiner Farbe in eine Linie zu bringen. Dies kann horizontal, vertikal oder diagonal sein.

Starten, indem die main.py Datei gestartet wird. Das Spiel wird über die Konsole mit Input Befehlen gespielt.
Folgende Befehle sind möglich (case-sensitiv!):

* <code>quit, exit</code> - Zum beenden des Spiels
* <code>help</code> - Gibt eine Liste möglicher Befehle aus
* <code>modus</code> - Mit modus kann man den Spielmodus wählen, computer für "Spieler gegen KI" oder spieler für "Spieler gegen Spieler"
  * Anmerkung: Per Default ist immer Spieler gegen Spieler ausgewählt, daher braucht man das nicht extra auswählen.
* <code>start</code> - Startet das Spiel im ausgewählten Modus

Gespielt wird, indem der Spieler, der an der Reihe ist in die Konsole die Nummer der Spalte (1-7) eingiebt, in der sein nächster Spielstein eingeworfen werden soll. Danach kommt entweder die Eingabeaufforderung für den 2. Spieler oder der Computer macht seinen Zug und Spieler 1 muss wieder die Spalte wählen.

Nachdem ein Spieler gewonnen hat, kommt man wieder ins "Hauptmenü" und kann erneut mittels Befehle ein neues Spiel konfigurieren und starten.

Ein Abbruch des Spiels ist jederzeit mit <code>exit</code> oder <code>quit</code> möglich.

Das Spielfeld sieht wie folgt aus:

<code>
-----------------------------------------<br>
| | | | | | | |<br>
| | | | | | | |<br>
| | | | | | | |<br>
| | | | | | | |<br>
| | | | | | | |<br>
| | | | | | | |<br>
-----------------------------------------<br>
Spieler 1 ist am zug: 
</code>
<br><br>
Notwendige Packages: numpy
