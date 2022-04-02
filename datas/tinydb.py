from tinydb import TinyDB, where


class DataBase:
    db = TinyDB('datas/db.json')
    players_table = db.table('_players')
    tournaments_table = db.table('_tournaments')

    def all_players(self):
        '''Get players from db'''
        serialized_players = self.players_table.all()

        return serialized_players

    @classmethod
    def save_player(cls, player):
        '''Insert player to db'''
        cls.players_table.insert(cls.serialize_player(cls, player))

    @classmethod
    def delete_player(cls, player):
        doc = cls.players_table.all()
        for d in doc:
            print(d.doc_id)
            if d['last_name'] == player.last_name:
                print(player.last_name)
                cls.players_table.remove(doc_ids=[d.doc_id])

    @classmethod
    def update_player(cls, player):
        cls.players_table.update({'ranking': player.ranking},
                                 where('last_name') == player.last_name)

    def all_tournaments(self):
        '''Get tournaments from db'''
        serialized_tournaments = self.tournaments_table.all()

        return serialized_tournaments

    @classmethod
    def save_tournament(cls, tournament):
        cls.tournaments_table.insert(cls.serialize_tournament(cls, tournament))

    @classmethod
    def delete_tournament(cls, tournament):
        doc = cls.tournaments_table.all()
        for d in doc:
            print(d.doc_id)
            if d['name'] == tournament.name:
                print(tournament.name)
                cls.tournaments_table.remove(doc_ids=[d.doc_id])

    @classmethod
    def update_tournament(cls, tournament):
        serialized_tournament = cls.serialize_tournament(cls, tournament)
        doc = cls.tournaments_table.all()
        for d in doc:
            if d['name'] == tournament.name:
                cls.tournaments_table.update(
                    serialized_tournament, doc_ids=[d.doc_id])

    # def update_round(self, tournament):
    #     round = tournament.rounds[-1]
    #     serialized_matchs = []
    #     for match in round:
    #         serialized_matchs.append(self.serialize_match(match))
    #     print(serialized_matchs)
    #     self.tournaments_table.update({'matchs': serialized_matchs},
    #                                   where('rounds') ==
    #                                   where('name') == tournament.name)

    # def update_match(self, tournament, r):
    #     matchs = tournament.rounds[-1].matchs
    #     serialized_matchs = []
    #     for match in matchs:
    #         serialized_matchs.append(self.serialize_match(match))
    #     print(serialized_matchs)
    #     self.tournaments_table.update({'matchs': serialized_matchs},
    #                                   where('rounds') ==
    #                                   where('name') == tournament.name)

    def serialize_player(self, player):
        serialized_player = player.__dict__
        # serialized_player = {
        #     'last_name': player.last_name,
        #     'for_name': player.for_name,
        #     'birthday': player.birthday,
        #     'gender': player.gender,
        #     'ranking': player.ranking
        # }
        return serialized_player

    def serialize_match(self, match):
        serialized_matchs = list()
        serialized_match = [
            self.serialize_player(self, match.player1[0]),
            match.player1[1],
            match.player1[2]
        ], [
            self.serialize_player(self, match.player2[0]),
            match.player2[1],
            match.player2[2]
        ]
        serialized_matchs.append(serialized_match)
        return serialized_match

    def serialize_round(self, round):
        matchs = []
        for match in round.matchs:
            matchs.append(self.serialize_match(self, match))
        serialized_round = {
            'number': round.number,
            'start_date': round.start_date,
            'end_date': round.end_date,
            'matchs': matchs
        }
        return serialized_round

    def serialize_result(self, result):
        serialized_result = [
            self.serialize_player(self, result[0]),
            result[1]
        ]
        return serialized_result

    def serialize_tournament(self, tournament):
        rounds = []
        for round in tournament.rounds:
            rounds.append(self.serialize_round(self, round))
        players = []
        for player in tournament.players:
            players.append(self.serialize_player(self, player))
        result = []
        for res in tournament.result:
            result.append(self.serialize_result(self, res))
        serialized_tournament = {
            'name': tournament.name,
            'description': tournament.description,
            'date': tournament.date,
            'location': tournament.location,
            'round_number': tournament.round_number,
            'rounds': rounds,
            'players': players,
            'time_controler': tournament.time_controler,
            'status': tournament.status,
            'result': result
        }
        return serialized_tournament
