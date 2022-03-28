from .player import Player


class Match:

    def __init__(self):
        self.player1: Player = Player, float(), float()
        self.player2: Player = Player, float(), float()

    def is_already_played(self, couple):
        test = [
            (self.player1[0].last_name, self.player2[0].last_name),
            (self.player2[0].last_name, self.player1[0].last_name)
        ]
        if couple in test:
            return True


class Round:

    def __init__(self, number, start_date, end_date):
        self.number = number
        self.start_date = start_date
        self.end_date = end_date
        self.matchs = []

    def add_match(self, match):
        if not isinstance(match, Match):
            return ValueError("Vous ne pouvez ajouter que des matchs !")
        self.matchs.append(match)

    def is_already_played_round(self, couple):
        for match in self.matchs:
            if match.is_already_played(couple):
                return True
