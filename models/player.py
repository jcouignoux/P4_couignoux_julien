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

    def add(self):
        db.add_player(self)

    def __str__(self):
        """Used in print."""
        return f"{self.last_name}, {self.for_name}"

    def __repr__(self):
        """Used in print."""
        return str(self)
