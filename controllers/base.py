# from typing import List

from views.menu import Menus
from .player import get_all_players, get_players
from .tournament import get_all_tournaments, get_tournament
from .report import get_reports


class Controller:

    def __init__(self, view):
        self.view = view
        self.menu = Menus()
        self.tournaments = get_all_tournaments()
        self.players = get_all_players()
        self.running = True

    def run(self):
        message = ''
        while self.running:
            res = self.view.prompt_for_main(self.menu.main_menu(), message)
            if res[0] == "Quit":
                self.running = False
            elif res[0] == "Bkup":
                for player in self.players:
                    player.update()
                    # self.db.save_player(player)
                for tournament in self.tournaments:
                    tournament.update()
                    # self.db.update_tournament(tournament)
            elif res[0] == "1":
                message = ''
                get_tournament(self, self.tournaments, message)
            elif res[0] == "2":
                message = ''
                get_players(self, self.players, message)
            elif res[0] == "3":
                message = ''
                get_reports(self, self.players, self.tournaments, message)
            elif res[0] == "Mes":
                message = res[1]
