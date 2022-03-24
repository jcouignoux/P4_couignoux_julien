from datas.tinydb import delete_player, save_player, update_player

GENDER = ("F", "M")
# BDAY = NewType('BDAY', datetime)
# DatetimeLike = TypeVar("DatetimeLike", BDAY)


class Player:

    def __init__(self, last_name, for_name, birthday, gender, ranking):
        self.last_name = str(last_name)
        self.for_name = str(for_name)
        self.birthday = birthday
        self.gender = gender
        self.ranking = int(ranking)

    def save(self):
        save_player(self)

    def update(self):
        update_player(self)

    def delete(self):
        delete_player(self)

    def __str__(self):
        """Used in print."""
        return f"{self.last_name}, {self.for_name}"

    def __repr__(self):
        """Used in print."""
        return str(self)
