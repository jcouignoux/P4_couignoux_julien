# from typing import List

# from datas.base import DataBase
# from views.menu import Menus as menu
from models.player import Player


def get_players(self, menu):
    res = self.view.prompt_for_player(
        self.players, menu)
    if res[0] == "New":
        create_player(self, self.menu.create_player_menu())
    elif res[0] == "Ret":
        self.run()
    elif res[0] == "Mod":
        modify_player(self, res[1])
    else:
        self.tournament.players.append(res)


def create_player(self, menu):
    res = self.view.prompt_for_create_player(self.menu.create_player_menu())
    print(res)
    if res[0] == "Abort":
        get_players(menu)
    elif res[0] == "Create":
        player = Player(res[1][0], res[1][1], res[1]
                        [2], res[1][3], res[1][4])
        self.db.add_player(player)


def modify_player(self, player):
    res = self.view.prompt_for_modify_player(
        self.menu.modify_player_menu(), player)
    if res[0] == "Abort":
        get_players(self, self.menu.player_menu())
    elif res[0] == "Mod":
        player.ranking = int(res[2])
        self.db.update_player(player)
