import os

from .player import PlayerView as pv
from .tournament import TournamentView as tv
from .report import ReportView as rv


LINE = "-----------------------------------------------"
TITLE = "##############################################"


class Views:

    def __init__(self):
        self.pv = pv
        self.tv = tv
        self.rv = rv

    # def prompt_for_main(self, menu, message):
    #     return self.active_view.prompt_for_main(menu, message)
    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def prompt_for_main(self, menu, message):
        self.cls()
        print(menu.title)
        for choice in menu.choices:
            print(choice)
        print(LINE)
        print(message)
        print(LINE)
        entry = input("Que souhaitez-vous faire: ")
        if entry in menu.responses:
            return (menu.responses[entry], message)
        else:
            message = "Entrée incorrecte."
            return ("Mes", message)

    # def prompt_for_player(self, menu, players, message):
    #     self.cls()
    #     return self.player_view.prompt_for_player(menu, players, message)

    # def prompt_for_add_player(self, menu, tournament, players, message):
    #     self.cls()
    #     return self.tournament_view.prompt_for_add_player(menu, tournament, players, message)

    # def prompt_for_create_player(self, menu, message):
    #     self.cls()
    #     return self.player_view.prompt_for_create_player(menu, message)

    # def prompt_for_modify_player(self, menu, player, message):
    #     self.cls()
    #     return self.player_view.prompt_for_modify_player(menu, player, message)

    # def prompt_for_tournament(self, menu, tournaments, message):
    #     self.cls()
    #     return self.tournament_view.prompt_for_tournament(menu, tournaments, message)

    # def prompt_for_new_tournament(self, menu, message):
    #     self.cls()
    #     return self.tournament_view.prompt_for_new_tournament(menu, message)

    # def prompt_for_tournament_detail(self, menu, tournament, message):
    #     self.cls()
    #     return self.tournament_view.prompt_for_tournament_detail(menu, tournament, message)

    # def prompt_for_match_detail(self, menu, tournament, match_index, message):
    #     self.cls()
    #     return self.tournament_view.prompt_for_match_detail(menu, tournament, match_index, message)

    # def prompt_for_reports(self, menu, message):
    #     self.cls()
    #     return self.report_view.prompt_for_reports(menu, message)

    # def prompt_for_players_report(self, menu, players, sort, message):
    #     self.cls()
    #     return self.report_view.prompt_for_players_report(menu, players, sort, message)

    # def prompt_for_tournament_players_report(self, menu, tournaments, tournament, players, sort, message):
    #     self.cls()
    #     return self.report_view.prompt_for_tournament_players_report(menu, tournaments, tournament, players, sort, message)

    # def prompt_for_tournaments_report(self, menu, tournaments):
    #     self.cls()
    #     return self.report_view.prompt_for_tournaments_report(menu, tournaments)

    # def prompt_for_tournament_rounds_report(self, menu, tournaments, tournament, message):
    #     self.cls()
    #     return self.report_view.prompt_for_tournament_rounds_report(menu, tournaments, tournament, message)

    # def prompt_for_tournament_matchs_report(self, menu, tournaments, tournament, message):
    #     self.cls()
    #     return self.report_view.prompt_for_tournament_matchs_report(menu, tournaments, tournament, message)
