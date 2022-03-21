from typing import List
import json
from .player import Player
from tinydb import TinyDB, where

db = TinyDB('db/db.json')
table = db.table('_tournaments')


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


class Tournament:

    def __init__(self, name, description, date, location, round_number, time_controler):  # , rounds, players
        self.name = name
        self.description = description
        self.date = date
        self.location = location
        self.round_number = int(round_number)
        self.rounds = []
        self.players = []
        self.time_controler = time_controler

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
        # return True

    def __str__(self):
        """Used in print."""
        return f"({self.name}, {self.location})"

    def __repr__(self):
        """Used in print."""
        return str(self)
