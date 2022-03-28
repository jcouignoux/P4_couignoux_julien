# from datas.tinydb import save_tournament, update_tournament, delete_tournament
from datas.tinydb import DataBase as db
from .player import Player
from .round import Round


class Tournament:

    def __init__(self, name, description, date, location, round_number, time_controler):
        self.name = str(name)
        self.description = str(description)
        self.date = date
        self.location = str(location)
        self.round_number = int(round_number)
        self.rounds = []
        self.players = []
        self.time_controler = time_controler
        self.status = True
        self.result = []

    def add_player(self, player):
        if not isinstance(player, Player):
            return ValueError("Vous ne pouvez ajouter que des tours !")
        self.players.append(player)

    def add_round(self, round):
        if not isinstance(round, Round):
            return ValueError("Vous ne pouvez ajouter que des tours !")
        self.rounds.append(round)

    def is_already_played(self, couple):
        for round in self.rounds:
            if round.is_already_played_round(couple):
                return True

    def save(self):
        db.save_tournament(self)

    def update(self):
        db.update_tournament(self)

    def delete(self):
        db.delete_tournament(self)

    def __str__(self):
        """Used in print."""
        return f"({self.name}, {self.location})"

    def __repr__(self):
        """Used in print."""
        return str(self)
