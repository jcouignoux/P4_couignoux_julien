from typing import List

from views.menu import Menus
from models.player import Player
from models.tournament import Tournament
from .player import *
from .tournament import *
from views.menu import Menus


class Controller:

    def __init__(self, view, db):
        self.view = view
        self.db = db
        self.menu = Menus()
        self.tournaments: List[Tournament] = self.db.get_all_tournaments()
        self.players: List[Player] = self.db.get_all_players()

    def run(self):
        running = True
        message = ''
        while running:
            res = self.view.prompt_for_main(self.menu.main_menu(), message)
            if res[0] == "Quit":
                running = False
            elif res[0] == "Bkup":
                for tournament in self.tournaments:
                    self.db.update_tournament(tournament)
            elif res[0] == "1":
                while True:
                    message = ''
                    get_tournament(self, self.tournaments, message)
            elif res[0] == "2":
                while True:
                    message = ''
                    get_players(self, self.players, message)
            elif res[0] == "Mes":
                message = res[1]
