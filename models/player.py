from typing import NewType, TypeVar, cast
from datetime import datetime
# from tinydb import TinyDB, where
from datas.base import DataBase as db
# db = TinyDB('db/db.json')
# table = db.table('_players')

GENDER = ("F", "M")
# BDAY = NewType('BDAY', datetime)
# DatetimeLike = TypeVar("DatetimeLike", BDAY)


class Player:

    def __init__(self, last_name, for_name, birthday, gender, ranking):
        self.last_name = last_name
        self.for_name = for_name
        self.birthday = birthday
        self.gender = gender
        self.ranking = int(ranking)

    # def serialized_player(self):
    #     self = {
    #         'last_name': self.last_name,
    #         'for_name': self.for_name,
    #         'bithday': self.birthday,
    #         'gender': self.gender,
    #         'ranking': self.ranking
    #     }

    def add(self):
        db.add_player(self)

    # def update_player_ranking(self):
    #     table.update({'ranking': self.ranking},
    #                  where('last_name') == self.last_name)

    def __str__(self):
        """Used in print."""
        return f"{self.last_name}, {self.for_name}"

    def __repr__(self):
        """Used in print."""
        return str(self)
