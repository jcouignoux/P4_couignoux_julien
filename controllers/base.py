from views.menu import Menus
from .player import PlayerController as pc
from .tournament import TournamentController as tc
from .report import ReportController as rc


class Controller:

    def __init__(self, view, db):
        self.view = view
        self.db = db
        self.tc = tc
        self.pc = pc
        self.rc = rc
        self.menu = Menus()
        self.tournaments = tc.get_all_tournaments(self)
        self.players = pc.get_all_players(self)
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
                for tournament in self.tournaments:
                    tournament.update()
            elif res[0] == "1":
                message = ''
                self.tc.get_tournament(self, self.tournaments, message)
            elif res[0] == "2":
                message = ''
                self.pc.get_players(self, self.players, message)
            elif res[0] == "3":
                message = ''
                self.rc.get_reports(self, self.players,
                                    self.tournaments, message)
            elif res[0] == "Mes":
                message = res[1]
