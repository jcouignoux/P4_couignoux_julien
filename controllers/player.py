from models.player import Player


class PlayerController():

    def get_all_players(self):
        '''Get serialized all players'''
        players = []
        for serialized_player in self.db.all_players():
            player = Player(
                last_name=serialized_player['last_name'],
                for_name=serialized_player['for_name'],
                birthday=serialized_player['birthday'],
                gender=serialized_player['gender'],
                ranking=int(serialized_player['ranking']),
            )
            players.append(player)
        return players

    def get_players(self, players, message):
        '''View players list'''
        res = self.view.pv.prompt_for_player(
            self.view, self.menu.player_menu(), players, message)
        if res[0] == "New":
            message = ''
            self.pc.create_player(self, message)
            self.pc.get_players(self, players, message)
        elif res[0] == "Ret":
            message = ''
            self.run()
        elif res[0] == "Mod":
            message = ''
            self.pc.modify_player(self, res[1], message)
            self.pc.get_players(self, players, message)
        elif res[0] == "Mes":
            message = res[2]
            self.pc.get_players(self, players, message)

    def create_player(self, message):
        '''Create player and add to players list'''
        res = self.view.pv.prompt_for_create_player(
            self.view, self.menu.create_player_menu(), message)
        if res[0] == "Abort":
            message = ''
            self.pc.get_players(self, self.players, message)
        elif res[0] == "Create":
            try:
                self.player = Player(
                    res[1][0], res[1][1], res[1][2], res[1][3], res[1][4]
                )
                self.players.append(self.player)
                self.player.save()
            except Exception as e:
                message = e
                self.pc.create_player(self, message)
        elif res[0] == "Add":
            self.player = Player(res[1][0], res[1][1],
                                 res[1][2], res[1][3], res[1][4]
                                 )
            return self.player
        elif res[0] == "Mes":
            message = res[2]
            self.pc.create_player(self, message)

    def modify_player(self, player, message):
        '''Modify rank player'''
        res = self.view.pv.prompt_for_modify_player(
            self.view, self.menu.modify_player_menu(), player, message)
        if res[0] == "Abort":
            message = ''
            self.pc.get_players(self, self.players, message)
        elif res[0] == "Mod":
            try:
                player.ranking = int(res[1])
                player.update
                player.save
            except Exception as e:
                message = e
                self.pc.modify_player(self, player, message)
        elif res[0] == "Del":
            self.players.remove(player)
            player.delete()
        elif res[0] == "Mes":
            message = res[2]
            self.pc.modify_player(self, player, message)
