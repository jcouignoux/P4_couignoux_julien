from typing import List
from datetime import datetime
import json

from models.tournament import Tournament, Round, Match
from .player import *


def get_tournament(self):
    res = self.view.prompt_for_tournament(
        self.tournaments, self.menu.tournament_menu())
    if res[0] == "New":
        get_new_tournament(self)
    elif res[0] == "Ret":
        self.run()
    elif res[0] == "View":
        self.tournament = res[1]
        get_tournament_detail(self)


def get_tournament_detail(self):
    res = self.view.prompt_for_tournament_detail(
        self.menu.tournament_detail_menu(), self.tournament)
    if res[0] == "Ret":
        get_tournament(self)
    elif res[0] == "Mod":
        match = res[1]
        get_match_detail(self, match)
    elif res[0] == "Val":
        add_round(self)


def get_new_tournament(self):
    date = datetime.now().strftime("%d/%m/%Y")
    res_t = self.view.prompt_for_new_tournament(
        self.menu.create_tournament_menu())
    if res_t[0] == "Abort":
        get_tournament(self)
    elif res_t[0] == "Create":
        self.tournament = Tournament(
            res_t[1][0], res_t[1][1], res_t[1][2], date, res_t[1][3], res_t[1][4])
        while True:
            res_p = add_players(self)


def add_players(self):
    res = self.view.prompt_for_add_player(
        self.menu.add_player_menu(), self.players)
    if res[0] == "Stop":
        get_tournament(self)
    elif res[0] == "Add":
        self.tournament.players.append(res[1])


def add_round(self):
    start_date = datetime.now().strftime("%d/%m/%Y-%H:%M")
    if len(self.tournament.roundst) == 0:
        round_number = 1
        self.tournament.rounds.append(round_number, start_date, '')
        players_list_sorted = sorted(
            self.tournament.players, key=lambda k: k.ranking)
        for i in range(len(players_list_sorted) // 2):
            player1 = (players_list_sorted[i], 0, 0)
            player2 = (players_list_sorted[i] +
                       (len(players_list_sorted) // 2), 0, 0)
            match = Match(player1, player2)
            self.tournament.rounds.matchs.append(match)
            match_json = ([json.loads(players_list_sorted[i].__dict__), 0, 0],
                          [json.loads(players_list_sorted[i + (len(players_list_sorted) // 2)].__dict__), 0, 0])
            # matchs_json.append(match_json)
    else:
        round_number = len(self.tournament.rounds) + 1
        player_list_temp = []
        for match in self.tournament.rounds.matchs:
            for player in match:
                player_list_temp.append([player[0], player[1] + player[2], 0])

        players_list_sorted = sorted(
            player_list_temp, key=lambda k: (k[1], k[0].ranking))

    round = Round(round_number, start_date, '')
    round_json = {'round_number': round_number,
                  'start_date': start_date}
    self.tournament.rounds.append(round)
    # tournament_json['rounds_list'].append(round_json)
    # for round in tournament.rounds_list:
    #     rounds_list_json.append(json.dumps(round.__dict__))
    # print(tournament_json['rounds_list'])
    # table.update({'rounds_list': tournament_json['rounds_list']},
    #  where('name') == tournament.name)

    return self


def get_match_detail(self, match):
    res = self.view.prompt_for_match_detail(
        self.menu.match_detail_menu(), match)
    if res[0] == "Mod":
        match.player1 = (match.player1[0], match.player1[1], res[1][0])
        match.player2 = (match.player2[0], match.player2[1], res[1][1])
        # self.db.update_match(self.tournament, match)
        get_tournament_detail(self)
    if res[0] == "Ret":
        get_tournament_detail(self)
