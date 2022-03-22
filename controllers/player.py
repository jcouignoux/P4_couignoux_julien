from models.player import Player


def get_players(self, players, message):
    res = self.view.prompt_for_player(
        self.menu.player_menu(), players, message)
    if res[0] == "New":
        message = ''
        create_player(self, message)
    elif res[0] == "Ret":
        message = ''
        self.run()
    elif res[0] == "Mod":
        message = ''
        modify_player(self, res[1], message)
    elif res[0] == "Mes":
        message = res[2]
        get_players(self, players, message)


def create_player(self, message):
    res = self.view.prompt_for_create_player(
        self.menu.create_player_menu(), message)
    if res[0] == "Abort":
        get_players(self.players, message)
    elif res[0] == "Create":
        try:
            player = Player(res[1][0], res[1][1], res[1]
                            [2], res[1][3], res[1][4])
            self.players.append(player)
            # self.db.add_player(player)
        except Exception as e:
            message = e
            create_player(self, message)
    elif res[0] == "Add":
        player = Player(res[1][0], res[1][1], res[1]
                        [2], res[1][3], res[1][4])
        # self.tournament.players.append(player)
        # return player
    elif res[0] == "Mes":
        message = res[2]
        create_player(self, message)


def modify_player(self, player, message):
    res = self.view.prompt_for_modify_player(
        self.menu.modify_player_menu(), player, message)
    if res[0] == "Abort":
        get_players(self, self.players)
    elif res[0] == "Mod":
        player.ranking = int(res[1])
        self.db.update_player(player)
    elif res[0] == "Del":
        self.db.delete_player(player)
    elif res[0] == "Mes":
        message = res[2]
        modify_player(self, player, message)
