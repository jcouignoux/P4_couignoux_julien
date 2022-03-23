from datetime import datetime

from models.tournament import Tournament, Round, Match
from .player import *
from datas.tinydb import all_tournaments


def get_all_tournaments():
    tournaments = []
    for tournament_dict in all_tournaments():
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


def get_tournament(self, tournaments, message):
    res = self.view.prompt_for_tournament(
        self.menu.tournament_menu(), tournaments, message)
    if res[0] == "New":
        message = ''
        adding_player = True
        get_new_tournament(self, adding_player, message)
    elif res[0] == "Ret":
        message = ''
        self.run()
    elif res[0] == "View":
        message = ''
        self.tournament = tournaments[res[1]]
        get_tournament_detail(self, self.tournament, message)
    elif res[0] == "Mes":
        message = res[2]
        get_tournament(self, tournaments, message)


def get_tournament_detail(self, tournament, message):
    res = self.view.prompt_for_tournament_detail(
        self.menu.tournament_detail_menu(), tournament, message)
    if res[0] == "Ret":
        message = ''
        get_tournament(self, self.tournaments, message)
    elif res[0] == "Mod":
        match_index = res[2]
        get_match_detail(self, tournament, match_index, message)
    elif res[0] == "Val":
        message = ''
        end_date = datetime.now().strftime("%d/%m/%Y-%H:%M")
        tournament.rounds[-1].end_date = end_date
        add_round(tournament)
        get_tournament_detail(self, tournament, message)
    elif res[0] == "New":
        message = ''
        add_round(tournament)
        get_tournament_detail(self, tournament, message)
    elif res[0] == "Mes":
        message = res[3]
        get_tournament_detail(self, tournament, message)
    elif res[0] == "Del":
        message = ''
        tournament.delete
    elif res[0] == "Close":
        message = ''
        pass
        # self.db.update_tournament


def get_new_tournament(self, adding_player, message):
    if adding_player == True:
        date = datetime.now().strftime("%d/%m/%Y")
        res = self.view.prompt_for_new_tournament(
            self.menu.create_tournament_menu(), message)
        if res[0] == "Abort":
            message = ''
            get_tournament(self, self.tournaments, message)
        elif res[0] == "Create":
            try:
                tournament = Tournament(
                    res[1][0], res[1][1], date, res[1][2], res[1][3], res[1][4])
                message = ''
            except Exception as e:
                message = e
                get_new_tournament(self, adding_player, message)
            while adding_player == True:
                add_players(self, tournament, message)
        if res[0] == "Mes":
            message = res[2]
            get_new_tournament(self, adding_player, message)
    else:
        add_round(tournament)
        self.tournaments.append(tournament)
        self.tournament = tournament
        self.db.save_tournament(self.tournament)
        get_tournament_detail(self, tournament, message)


def add_players(self, tournament, message):
    res = self.view.prompt_for_add_player(
        self.menu.add_player_menu(), tournament, self.players, message)
    if res[0] == "Stop":
        adding_player = False
        get_new_tournament(self, adding_player, message)
    elif res[0] == "Add":
        message = ''
        player = res[1]
        tournament.add_player(player)
    elif res[0] == "Create":
        player = create_player(self, message)
        tournament.add_player(player)
        # tournament = self.tournament
    elif res[0] == "Mes":
        message = res[2]
        add_players(self, tournament, message)


def add_round(tournament):
    start_date = datetime.now().strftime("%d/%m/%Y-%H:%M")
    round_number = len(tournament.rounds) + 1
    round = Round(round_number, start_date, '')
    if len(tournament.rounds) == 0:
        players_list_sorted = sorted(
            tournament.players, key=lambda k: k.ranking)
        for i in range(len(players_list_sorted) // 2):
            player1 = players_list_sorted[i], 0, 0
            player2 = players_list_sorted[i +
                                          (len(players_list_sorted) // 2)], 0, 0
            match = Match()
            match.player1 = player1
            match.player2 = player2
            round.add_match(match)
    else:
        player_list_temp = []
        for match in tournament.rounds[-1].matchs:
            player_list_temp.append(
                [match.player1[0], match.player1[1] + match.player1[2], 0])
            player_list_temp.append(
                [match.player2[0], match.player2[1] + match.player2[2], 0])
        players_list_sorted = sorted(
            player_list_temp, key=lambda k: (-k[1], k[0].ranking))
        # ref list
        player_list_pop = list(tournament.players)
        # first player index
        i1 = 0
        # second player index
        i2 = 1
        for item in range(len(players_list_sorted) // 2):
            # Initialize number of matchs
            for n in range(len(player_list_pop) - 1):
                player1 = [players_list_sorted[i1][0],
                           players_list_sorted[i1][1], 0]
                # Test if first ans second players in ref list
                if players_list_sorted[i1][0] in player_list_pop:
                    if players_list_sorted[i2][0] in player_list_pop:
                        # Check if match already played
                        couple = (
                            players_list_sorted[i1][0].last_name,
                            players_list_sorted[i2][0].last_name
                        )
                        if not tournament.is_already_played(couple):
                            if players_list_sorted[i2][0] in player_list_pop:
                                player2 = [players_list_sorted[i2][0],
                                           players_list_sorted[i2][1], 0]
                                # remove player from ref list
                                player_list_pop.remove(
                                    players_list_sorted[i1][0])
                                player_list_pop.remove(
                                    players_list_sorted[i2][0])
                                match = Match()
                                match.player1 = player1
                                match.player2 = player2
                                round.add_match(match)
                                i1 += 1
                                i2 = i1 + 1
                        else:
                            print(str(players_list_sorted[i1][0].last_name) + " et " +
                                  str(players_list_sorted[i2][0].last_name) + str(" ont déjà joué ensemble."))
                            input('')
                            i2 += 1
                    else:
                        # print("p2 pas dans player_pop")
                        i2 += 1
                else:
                    # print("p1 pas dans player_pop")
                    i1 += 1
                    i2 = i1 + 1
        # input('fin')
    tournament.add_round(round)


def get_match_detail(self, tournament, match_index, message):
    res = self.view.prompt_for_match_detail(
        self.menu.match_detail_menu(), tournament, match_index, message)
    if res[0] == "Mod":
        message = ''
        match = tournament.rounds[-1].matchs[match_index]
        match.player1 = (match.player1[0], match.player1[1], res[1][0])
        match.player2 = (match.player2[0], match.player2[1], res[1][1])
        get_tournament_detail(self, tournament, message)
    elif res[0] == "Ret":
        message = ''
        get_tournament_detail(self, tournament, message)
    elif res[0] == "Mes":
        message = res[2]
        get_match_detail(self, tournament, match_index, message)
