import json
from tinydb import TinyDB, where
from models.player import Player
from models.tournament import Tournament, Round, Match

db = TinyDB('datas/db.json')


class TinyDb():

    def __init__(self):
        self.players_table = db.table('_players')
        self.tournaments_table = db.table('_tournaments')

    def get_all_players(self):
        players = []
        for serialized_player in self.players_table.all():
            player = Player(
                last_name=serialized_player['last_name'],
                for_name=serialized_player['for_name'],
                birthday=serialized_player['birthday'],
                gender=serialized_player['gender'],
                ranking=int(serialized_player['ranking']),
            )
            players.append(player)

        return players

    def save_player(player):
        pass
        # self.players_table.insert(self.serialize_player(player))

    def delete_player(self, player):
        doc = self.players_table.all()
        for d in doc:
            print(d.doc_id)
            if d['last_name'] == player.last_name:
                print(player.last_name)
                self.tournaments_table.remove(doc_ids=[d.doc_id])
        input('')

    def update_player(self, player):
        self.players_table.update({'ranking': player.ranking},
                                  where('last_name') == player.last_name)

    def get_all_tournaments(self):
        tournaments = []
        for tournament_dict in self.tournaments_table.all():
            tournament = Tournament(
                name=tournament_dict['name'],
                description=tournament_dict['description'],
                date=tournament_dict['date'],
                location=tournament_dict['location'],
                round_number=int(tournament_dict['round_number']),
                time_controler=tournament_dict['time_controler']
            )
            for player_dict in tournament_dict['players']:
                player = Player(
                    last_name=player_dict['last_name'],
                    for_name=player_dict['for_name'],
                    birthday=player_dict['birthday'],
                    gender=player_dict['gender'],
                    ranking=int(player_dict['ranking'])
                )
                tournament.add_player(player)
            for round_list in tournament_dict['rounds']:
                round = Round(
                    number=round_list['number'],
                    start_date=round_list['start_date'],
                    end_date=round_list['end_date']
                )
                for match_list in round_list['matchs']:
                    f1 = match_list[0][0]['last_name']
                    p1 = filter(lambda x: f1 in x.last_name,
                                tournament.players)
                    f2 = match_list[1][0]['last_name']
                    p2 = filter(lambda x: f2 in x.last_name,
                                tournament.players)
                    match = Match()
                    match.player1 = (
                        list(p1)[0],
                        float(match_list[0][1]),
                        float(match_list[0][2])
                    )
                    match.player2 = (
                        list(p2)[0],
                        float(match_list[1][1]),
                        float(match_list[1][2])
                    )
                    round.add_match(match)
                    already_played_matchs = (
                        match.player1[0].last_name, match.player2[0].last_name
                    ), (
                        match.player2[0].last_name, match.player1[0].last_name
                    )
                tournament.add_round(round)
            tournaments.append(tournament)

        return tournaments

    def save_tournament(self, tournament):
        pass
        # self.tournaments_table.insert(self.serialize_tournament(tournament))

    def add_round(self, round):
        pass

    def add_match(self, match):
        pass

    def update_round(self, tournament):
        round = tournament.rounds[-1]
        serialized_matchs = []
        for match in round:
            serialized_matchs.append(self.serialize_match(match))
        print(serialized_matchs)
        self.tournaments_table.update({'matchs': serialized_matchs},
                                      where('rounds') ==
                                      where('name') == tournament.name)
        input('')

    def update_match(self, tournament, r):
        matchs = tournament.rounds[-1].matchs
        serialized_matchs = []
        for match in matchs:
            serialized_matchs.append(self.serialize_match(match))
        print(serialized_matchs)
        self.tournaments_table.update({'matchs': serialized_matchs},
                                      where('rounds') ==
                                      where('name') == tournament.name)
        input('')

    def update_tournament(self, tournament):
        serialized_tournament = self.serialize_tournament(tournament)
        print(serialized_tournament)
        doc = self.tournaments_table.all()
        for d in doc:
            print(d.doc_id)
            if d['name'] == tournament.name:
                self.tournaments_table.update(
                    serialized_tournament, doc_ids=[d.doc_id])
        input('')

        return 1

    def serialize_player(self, player):
        serialized_player = {
            'last_name': player.last_name,
            'for_name': player.for_name,
            'birthday': player.birthday,
            'gender': player.gender,
            'ranking': player.ranking
        }
        return serialized_player

    def serialize_match(self, match):
        serialized_matchs = list()
        serialized_match = [
            self.serialize_player(match.player1[0]),
            match.player1[1],
            match.player1[2]
        ], [
            self.serialize_player(match.player2[0]),
            match.player2[1],
            match.player2[2]
        ]
        serialized_matchs.append(serialized_match)
        return serialized_match

    def serialize_round(self, round):
        matchs = []
        for match in round.matchs:
            matchs.append(self.serialize_match(match))
        serialized_round = {
            'number': round.number,
            'start_date': round.start_date,
            'end_date': round.end_date,
            'matchs': matchs
        }
        return serialized_round

    def serialize_tournament(self, tournament):
        rounds = []
        for round in tournament.rounds:
            rounds.append(self.serialize_round(round))
        players = []
        for player in tournament.players:
            players.append(self.serialize_player(player))
        serialized_tournament = {
            'name': tournament.name,
            'description': tournament.description,
            'date': tournament.date,
            'location': tournament.location,
            'round_number': tournament.round_number,
            'rounds': rounds,
            'players': players,
            'time_controler': tournament.time_controler
        }
        return serialized_tournament
