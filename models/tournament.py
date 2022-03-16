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


class Matchs(list):

    def append(self, object):
        if not isinstance(object, Match):
            return ValueError("Vous ne pouvez ajouter que des matchs !")
        return super().append(object)


class Round:

    def __init__(self, number, start_date, end_date):
        self.number = number
        self.start_date = start_date
        self.end_date = end_date
        self.matchs: List[Match] = Matchs()

    # def match(self):
    #     matchs_list = []
    #     for match in self.matchs_list:
    #         p1_j = json.loads(match[0][0])
    #         player1 = Player(p1_j['last_name'], p1_j['for_name'],
    #                          p1_j['birthday'], p1_j['gender'], p1_j['ranking'])
    #         total1 = int(match[0][1])
    #         score1 = int(match[0][2])
    #         p2_j = json.loads(match[1][0])
    #         player2 = Player(p2_j['last_name'], p2_j['for_name'],
    #                          p2_j['birthday'], p2_j['gender'], p2_j['ranking'])
    #         total2 = int(match[1][1])
    #         score2 = int(match[1][2])
    #         matchs_list.append(
    #             Match(player1, total1, score1, player2, total2, score2))

    #     return matchs_list


class Rounds(list):

    def append(self, object):
        if not isinstance(object, Round):
            return ValueError("Vous ne pouvez ajouter que des tours !")
        return super().append(object)

    def list(self, object):
        if not isinstance(object, Round):
            return ValueError("Vous ne po")
        return super()


class Players(list):

    def append(self, object):
        if not isinstance(object, Player):
            return ValueError("Vous ne pouvez ajouter que des joueurs !")
        return super().append(object)


class Tournament:

    def __init__(self, name, description, date, location, round_number, time_controler):
        self.name = name
        self.description = description
        self.date = date
        self.location = location
        self.round_number = int(round_number)
        self.rounds: List[Round] = Rounds()
        self.players: List[Player] = Players()
        self.time_controler = time_controler

    def serialized_tournament(self):
        self.tournament = table.all()

    def add_tournament(self):
        pass

    def __str__(self):
        """Used in print."""
        return f"({self.name}, {self.location})"

    def __repr__(self):
        """Used in print."""
        return str(self)
    # def get_players(self):
    #     players_list = []
    #     for player_json in self.players_list:
    #         p_j = json.loads(player_json)
    #         player = Player(p_j['last_name'], p_j['for_name'],
    #                         p_j['birthday'], p_j['gender'], p_j['ranking'])
    #         players_list.append(player)

    #     return players_list

    # def get_rounds(self):
    #     rounds_list = []
    #     for round_json in self.rounds_list:
    #         r_j = round_json
    #         round = Round(r_j['number'], r_j['start_date'], r_j['end_date'],
    #                       r_j['matchs_list'])
    #         rounds_list.append(round)

    #     return rounds_list
