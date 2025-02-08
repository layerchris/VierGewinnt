class Player:
    def __init__(self, name:str, color:str, p:bool):
        """Eine Klasse zur Darstellung eines Spielers.

            Attribute
            ----------
            player_name : str
                Der Name des Spielers.
            player_color : str
                Das Symbol oder die Farbe des Spielers auf dem Spielfeld.
            is_player : bool
                Gibt an, ob es sich um einen menschlichen Spieler handelt (True) oder um eine KI (False).
            """
        self.player_name = name
        self.player_color = color
        self.is_player = p
