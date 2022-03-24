from tinydb import TinyDB, where

db = TinyDB('datas/db.json')


players_table = db.table('_players')
tournaments_table = db.table('_tournaments')


def all_players():
    serialized_players = players_table.all()

    return serialized_players


def save_player(player):
    # pass
    players_table.insert(serialize_player(player))


def delete_player(player):
    doc = players_table.all()
    for d in doc:
        print(d.doc_id)
        if d['last_name'] == player.last_name:
            print(player.last_name)
            players_table.remove(doc_ids=[d.doc_id])
    input('')


def update_player(player):
    players_table.update({'ranking': player.ranking},
                         where('last_name') == player.last_name)


def all_tournaments():
    serialized_tournaments = tournaments_table.all()

    return serialized_tournaments


def save_tournament(tournament):
    # pass
    tournaments_table.insert(serialize_tournament(tournament))


def delete_tournament(self, tournament):
    doc = self.tournament_table.all()
    for d in doc:
        print(d.doc_id)
        if d['name'] == tournament.name:
            print(tournament.name)
            self.tournaments_table.remove(doc_ids=[d.doc_id])
    input('')


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
        if d['name'] == tournament.name:
            self.tournaments_table.update(
                serialized_tournament, doc_ids=[d.doc_id])
    return 1


def serialize_player(player):
    serialized_player = {
        'last_name': player.last_name,
        'for_name': player.for_name,
        'birthday': player.birthday,
        'gender': player.gender,
        'ranking': player.ranking
    }
    return serialized_player


def serialize_match(match):
    serialized_matchs = list()
    serialized_match = [
        serialize_player(match.player1[0]),
        match.player1[1],
        match.player1[2]
    ], [
        serialize_player(match.player2[0]),
        match.player2[1],
        match.player2[2]
    ]
    serialized_matchs.append(serialized_match)
    return serialized_match


def serialize_round(round):
    matchs = []
    for match in round.matchs:
        matchs.append(serialize_match(match))
    serialized_round = {
        'number': round.number,
        'start_date': round.start_date,
        'end_date': round.end_date,
        'matchs': matchs
    }
    return serialized_round


def serialize_result(result):
    serialized_result = [
        serialize_player(result[0]),
        result[1]
    ]
    return serialized_result


def serialize_tournament(tournament):
    rounds = []
    for round in tournament.rounds:
        rounds.append(serialize_round(round))
    players = []
    for player in tournament.players:
        players.append(serialize_player(player))
    result = []
    for res in tournament.result:
        result.append(serialize_result(res))
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
