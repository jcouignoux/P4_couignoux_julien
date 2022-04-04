from datetime import datetime

from models.tournament import Tournament
from models.round import Round, Match
from models.player import Player


class TournamentController:

    def get_all_tournaments(self):
        '''Get srialized all tournaments'''
        tournaments = []
        for tournament_dict in self.db.all_tournaments():
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
                tournament.add_round(round)
            tournaments.append(tournament)
        return tournaments

    def get_tournament(self, tournaments, message):
        '''View tournaments list'''
        res = self.view.tv.prompt_for_tournament(
            self.view, self.menu.tournament_menu(), tournaments, message)
        if res[0] == "New":
            message = ''
            self.adding_player = True
            self.tc.get_new_tournament(self, message)
        elif res[0] == "Ret":
            message = ''
            self.run()
        elif res[0] == "View":
            message = ''
            self.tournament = tournaments[res[1]]
            self.tc.get_tournament_detail(self, self.tournament, message)
        elif res[0] == "Mes":
            message = res[2]
            self.tc.get_tournament(self, tournaments, message)

    def get_tournament_detail(self, tournament, message):
        '''View tournament details to action'''
        res = self.view.tv.prompt_for_tournament_detail(
            self.view, self.menu.tournament_detail_menu(), tournament, message)
        if res[0] == "Ret":
            message = ''
            self.tc.get_tournament(self, self.tournaments, message)
        elif res[0] == "Mod":
            match_index = res[2]
            self.tc.get_match_detail(self, tournament, match_index, message)
        elif res[0] == "Val":
            message = ''
            end_date = datetime.now().strftime("%d/%m/%Y-%H:%M")
            tournament.rounds[-1].end_date = end_date
            try:
                self.tc.add_round(tournament)
            except Exception as e:
                message = e
            self.tc.get_tournament_detail(self, tournament, message)
        elif res[0] == "New":
            message = ''
            self.tc.add_round(tournament)
            self.tc.get_tournament_detail(self, tournament, message)
        elif res[0] == "Mes":
            message = res[3]
            self.tc.get_tournament_detail(self, tournament, message)
        elif res[0] == "Del":
            message = ''
            self.tournaments.remove(tournament)
            tournament.delete()
        elif res[0] == "Close":
            message = 'Tournoi Terminé'
            self.tc.close_tournament(tournament)
            self.tc.get_tournament_detail(self, tournament, message)

    def get_new_tournament(self, message):
        '''New tournament view'''
        if self.adding_player:
            date = datetime.now().strftime("%d/%m/%Y")
            res = self.view.tv.prompt_for_new_tournament(
                self.view, self.menu.create_tournament_menu(), message)
            if res[0] == "Abort":
                message = ''
                self.tc.get_tournament(self, self.tournaments, message)
            elif res[0] == "Create":
                try:
                    self.tournament = Tournament(
                        res[1][0], res[1][1], date, res[1][2], res[1][3], res[1][4])
                    message = ''
                except Exception as e:
                    message = e
                    self.tc.get_new_tournament(self, message)
                while self.adding_player:
                    self.tc.add_players(self, self.tournament, message)
            if res[0] == "Mes":
                message = res[2]
                self.tc.get_new_tournament(self, message)
        else:
            self.tc.first_round(self.tournament)
            self.tournaments.append(self.tournament)
            self.tournament.save()
            self.tc.get_tournament_detail(self, self.tournament, message)

    def add_players(self, tournament, message):
        '''Select or Create player and Add to tournament'''
        res = self.view.tv.prompt_for_add_player(
            self.view, self.menu.add_player_menu(), tournament, self.players, message)
        if res[0] == "Stop":
            self.adding_player = False
            self.tc.get_new_tournament(self, message)
        elif res[0] == "Add":
            message = ''
            player = res[1]
            tournament.add_player(player)
        elif res[0] == "Create":
            player = self.pc.create_player(self, message)
            tournament.add_player(player)
        elif res[0] == "Mes":
            message = res[2]
            self.tc.add_players(self, tournament, message)

    def first_round(tournament):
        start_date = datetime.now().strftime("%d/%m/%Y-%H:%M")
        round_number = 1
        round = Round(round_number, start_date, '')
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
        tournament.add_round(round)

    def add_round(tournament):
        start_date = datetime.now().strftime("%d/%m/%Y-%H:%M")
        round_number = len(tournament.rounds) + 1
        round = Round(round_number, start_date, '')
        player_list_temp = []
        for match in tournament.rounds[-1].matchs:
            player_list_temp.append(
                [match.player1[0], match.player1[1] + match.player1[2], 0])
            player_list_temp.append(
                [match.player2[0], match.player2[1] + match.player2[2], 0])
        players_list_sorted = sorted(
            player_list_temp, key=lambda k: (-k[1], k[0].ranking))
        player_list_pop = list(tournament.players)
        i1 = 0
        i2 = 1
        for item in range(len(players_list_sorted) // 2):
            for n in range(len(player_list_pop) - 1):
                player1 = [players_list_sorted[i1][0],
                           players_list_sorted[i1][1], 0]
                if players_list_sorted[i1][0] in player_list_pop:
                    if players_list_sorted[i2][0] in player_list_pop:
                        couple = (
                            players_list_sorted[i1][0].last_name,
                            players_list_sorted[i2][0].last_name
                        )
                        if not tournament.is_already_played(couple) or (len(player_list_pop)) == 2:
                            if players_list_sorted[i2][0] in player_list_pop:
                                player2 = [players_list_sorted[i2][0],
                                           players_list_sorted[i2][1], 0]
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
                                  str(players_list_sorted[i2][0].last_name) +
                                  str(" ont déjà joué ensemble."))
                            input('')
                            i2 += 1
                    else:
                        i2 += 1
                else:
                    i1 += 1
                    i2 = i1 + 1
        tournament.add_round(round)

    def get_match_detail(self, tournament, match_index, message):
        '''View to enter scores'''
        res = self.view.tv.prompt_for_match_detail(
            self.view, self.menu.match_detail_menu(), tournament, match_index, message)
        if res[0] == "Mod":
            message = ''
            match = tournament.rounds[-1].matchs[match_index]
            match.player1 = (match.player1[0], match.player1[1], res[1][0])
            match.player2 = (match.player2[0], match.player2[1], res[1][1])
            self.tc.get_tournament_detail(self, tournament, message)
        elif res[0] == "Ret":
            message = ''
            self.tc.get_tournament_detail(self, tournament, message)
        elif res[0] == "Mes":
            message = res[2]
            self.tc.get_match_detail(self, tournament, match_index, message)

    def close_tournament(tournament):
        '''Calculate ultimate rank and put status to False'''
        if tournament.status:
            date = datetime.now().strftime("%d/%m/%Y-%H:%M")
            round = tournament.rounds[-1]
            round.end_date = date
            tournament.rounds[-1] = round
            tournament.status = False
            player_list = []
            for match in tournament.rounds[-1].matchs:
                player_list.append(
                    [match.player1[0], match.player1[1] + match.player1[2]])
                player_list.append(
                    [match.player2[0], match.player2[1] + match.player2[2]])
                players_list_sorted = sorted(
                    player_list, key=lambda k: (-k[1], k[0].ranking))
            tournament.result = players_list_sorted
            tournament.save
        else:
            pass
