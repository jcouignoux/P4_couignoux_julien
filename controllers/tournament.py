from typing import List
from datetime import datetime

from models.tournament import Tournament, Round, Match
from .player import *


def get_tournament(self, tournaments):
    res = self.view.prompt_for_tournament(
        self.menu.tournament_menu(), tournaments)
    if res[0] == "New":
        adding_player = True
        get_new_tournament(self, adding_player)
    elif res[0] == "Ret":
        self.run()
    elif res[0] == "View":
        self.tournament = tournaments[res[1]]
        get_tournament_detail(self, self.tournament)


def get_tournament_detail(self, tournament):
    res = self.view.prompt_for_tournament_detail(
        self.menu.tournament_detail_menu(), tournament)
    if res[0] == "Ret":
        get_tournament(self, self.tournaments)
    elif res[0] == "Mod":
        match_index = res[2]
        get_match_detail(self, tournament, match_index)
    elif res[0] == "Val":
        end_date = datetime.now().strftime("%d/%m/%Y-%H:%M")
        tournament.rounds[-1].end_date = end_date
        add_round(tournament)
        get_tournament_detail(self, tournament)
    elif res[0] == "New":
        add_round(tournament)
        get_tournament_detail(self, tournament)
    elif res[0] == "Close":
        pass
        # self.db.update_tournament


def get_new_tournament(self, adding_player):
    if adding_player == True:
        date = datetime.now().strftime("%d/%m/%Y")
        message = ''
        res_t = self.view.prompt_for_new_tournament(
            self.menu.create_tournament_menu())
        if res_t[0] == "Abort":
            get_tournament(self)
        elif res_t[0] == "Create":
            self.tournament = Tournament(
                res_t[1][0], res_t[1][1], date, res_t[1][2], res_t[1][3], res_t[1][4])
            while adding_player == True:
                add_players(self, self.tournament, message)
    else:
        add_round(self.tournament)
        self.tournaments.append(self.tournament)
        get_tournament_detail(self, self.tournament)


def add_players(self, tournament, message):
    res = self.view.prompt_for_add_player(
        self.menu.add_player_menu(), tournament, self.players, message)
    if res[0] == "Stop":
        if (len(tournament.players) % 2) == 0:
            adding_player = False
            get_new_tournament(self, adding_player)
        else:
            message = "Il doit y avoir un nombre de joueurs paire"
    elif res[0] == "Add":
        player = res[1]
        tournament.add_player(player)
    elif res[0] == "Create":
        player = create_player(self)
        # print(player)
        # input('')
        tournament.players.append(player)


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
            round.matchs.append(match)
    else:
        # créer une liste : à faire en méthode
        matchs_played_list = []
        for r in tournament.rounds:
            for m in r.matchs:
                p = m.player1[0].last_name, m.player2[0].last_name
                p_inv = m.player2[0].last_name, m.player1[0].last_name
                matchs_played_list.append(p)
                matchs_played_list.append(p_inv)
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
                    print("p1 pas dans player_pop")
                    i1 += 1
                    i2 = i1 + 1
        # input('fin')
    # tournament.rounds.append(round)
    tournament.add_round(round)


def get_match_detail(self, tournament, match_index):
    res = self.view.prompt_for_match_detail(
        self.menu.match_detail_menu(), tournament, match_index)
    if res[0] == "Mod":
        match = tournament.rounds[-1].matchs[match_index]
        match.player1 = (match.player1[0], match.player1[1], res[1][0])
        match.player2 = (match.player2[0], match.player2[1], res[1][1])
        get_tournament_detail(self, tournament)
    if res[0] == "Ret":
        get_tournament_detail(self, tournament)
