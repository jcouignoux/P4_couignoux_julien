from models.player import Player


def get_players(self, players):
    res = self.view.prompt_for_player(
        self.menu.player_menu(), players)
    if res[0] == "New":
        create_player(self)
    elif res[0] == "Ret":
        self.run()
    elif res[0] == "Mod":
        modify_player(self, res[1])
    # else:
    #     self.tournament.players.append(res)


def create_player(self):
    res = self.view.prompt_for_create_player(self.menu.create_player_menu())
    if res[0] == "Abort":
        get_players(self.players)
    elif res[0] == "Create":
        player = Player(res[1][0], res[1][1], res[1]
                        [2], res[1][3], res[1][4])
        self.players.append(player)
        # self.db.add_player(player)
    elif res[0] == "Add":
        player = Player(res[1][0], res[1][1], res[1]
                        [2], res[1][3], res[1][4])
        # self.tournament.players.append(player)
    return player


def modify_player(self, player):
    res = self.view.prompt_for_modify_player(
        self.menu.modify_player_menu(), player)
    if res[0] == "Abort":
        get_players(self, self.players)
    elif res[0] == "Mod":
        player.ranking = int(res[1])
        self.db.update_player(player)
    elif res[0] == "Del":
        self.db.delete_player(player)
