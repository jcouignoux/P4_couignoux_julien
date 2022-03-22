
class DataBase:

    # def __init__(self, active_db, dbs):
    def __init__(self, active_db):
        self.active_db = active_db
        # self.dbs = dbs

    def get_all_players(self):
        return self.active_db.get_all_players()

    def save_player(self, player):
        return self.active_db.save_player(player)

    def update_player(self, player):
        return self.active_db.update_player(player)

    def delete_player(self, player):
        return self.active_db.delete_player(player)

    def get_all_tournaments(self):
        return self.active_db.get_all_tournaments()

    def save_tournament(self, tournament):
        return self.active_db.save_tournament(tournament)

    def update_match(self, tournament, match):
        return self.active_db.update_match(tournament, match)

    def update_tournament(self, tournament):
        return self.active_db.update_tournament(tournament)
