from typing import List

from views.menu import Menus
from models.player import Player
from models.tournament import Tournament
from .player import *
from .tournament import *
from views.menu import Menus as menu


class Controller:

    def __init__(self, view, db):
        self.view = view
        self.db = db
        self.menu = Menus()
        self.tournaments: List[Tournament] = self.db.get_all_tournaments()
        self.players: List[Player] = self.db.get_all_players()

    def run(self):
        running = True
        while running:
            res = self.view.prompt_for_main(menu.main_menu(self))
            if res == "Quit":
                running = False
            elif res == "Bkup":
                for tournament in self.tournaments:
                    self.db.update_tournament(tournament)
            elif res == "1":
                while True:
                    get_tournament(self, self.tournaments)
            elif res == "2":
                while True:
                    get_players(self, self.players)
            else:
                self.run()
