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
