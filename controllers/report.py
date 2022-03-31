
class ReportController:

    def get_reports(self, players, tournaments, message):
        res = self.view.rv.prompt_for_reports(
            self.view, self.menu.reports_menu(), message)
        if res[0] == "1":
            message = ''
            self.rc.players_report(self, players, message)
        elif res[0] == "2":
            message = ''
            self.rc.tournament_players_report(self, tournaments, message)
        elif res[0] == "3":
            message = ''
            self.rc.tournaments_report(self, tournaments,)
        elif res[0] == "4":
            message = ''
            self.rc.tournament_rounds_report(self, tournaments, message)
        elif res[0] == "5":
            message = ''
            self.rc.tournament_matchs_report(self, tournaments, message)
        elif res[0] == "Mes":
            message = res[1]
            self.rc.get_reports(self, players, tournaments, message)
        elif res[0] == "Ret":
            message = ''
            self.run()

    def players_report(self, players, message):
        sort = False
        res = self.view.rv.prompt_for_players_report(
            self.view, self.menu.players_report_menu(), players, sort, message)
        if res[0] == "1":
            message = 'Tri par ordre alphabétique'
            players_sorted = sorted(
                players, key=lambda k: (k.last_name))
            sort = True
            self.view.rv.prompt_for_players_report(
                self.view, self.menu.players_report_menu(), players_sorted, sort, message)
            self.rc.get_reports(self, self.players, self.tournaments, message)
        elif res[0] == "2":
            message = 'Tri par ordre de classement'
            players_sorted = sorted(
                players, key=lambda k: (k.ranking))
            sort = True
            self.view.rv.prompt_for_players_report(
                self.view, self.menu.players_report_menu(), players_sorted, sort, message)
            self.rc.get_reports(self, self.players, self.tournaments, message)
        elif res[0] == "Ret":
            message = ''
            sort = False
            self.rc.get_reports(self, players, self.tournaments, message)
        elif res[0] == "Mes":
            message = res[3]
            self.rc.players_report(self, players, message)

    def tournament_players_report(self, tournaments, message):
        tournament = ''
        players = ''
        sort = False
        res = self.view.rv.prompt_for_tournament_players_report(
            self.view, self.menu.players_report_menu(), tournaments, tournament, players, sort, message)
        if res[0] == "Sel":
            tournament = res[1]
            res2 = self.view.rv.prompt_for_tournament_players_report(
                self.view, self.menu.players_report_menu(), tournaments, tournament, players, sort, message)
            if res2[0] == "1":
                message = 'Tri par ordre alphabétique'
                matchs_list = tournament.rounds[-1].matchs
                players_list = []
                for match in matchs_list:
                    players_list.append(match.player1)
                    players_list.append(match.player2)
                players_sorted = sorted(
                    players_list, key=lambda k: (k[0].last_name))
                sort = True
                self.view.rv.prompt_for_tournament_players_report(
                    self.view, self.menu.players_report_menu(), tournaments, tournament, players_sorted, sort, message)
                self.rc.get_reports(self, players, self.tournaments, message)
            elif res2[0] == "2":
                message = 'Tri par ordre de classement'
                matchs_list = tournament.rounds[-1].matchs
                players_list = []
                for match in matchs_list:
                    players_list.append(match.player1)
                    players_list.append(match.player2)
                players_sorted = sorted(
                    players_list, key=lambda k: (-k[1], k[0].ranking))
                sort = True
                self.view.rv.prompt_for_tournament_players_report(
                    self.view, self.menu.players_report_menu(), tournaments, tournament, players_sorted, sort, message)
                self.rc.get_reports(self, players, self.tournaments, message)
            elif res2[0] == "Mes":
                message = res[3]
                self.rc.tournament_players_report(self, tournaments, message)
        elif res[0] == "Mes":
            message = res[2]
            self.rc.tournament_players_report(self, tournaments, message)
        elif res[0] == "Ret":
            message = ''
            sort = False
            self.rc.get_reports(self, players, self.tournaments, message)

    def tournaments_report(self, tournaments):
        self.view.rv.prompt_for_tournaments_report(
            self.view, self.menu.tournaments_report_menu(), tournaments)
        message = ''
        self.rc.get_reports(self, self.players, self.tournaments, message)

    def tournament_rounds_report(self, tournaments, message):
        tournament = ''
        res = self.view.rv.prompt_for_tournament_rounds_report(
            self.view, self.menu.tournament_rounds_menu(), tournaments, tournament, message)
        if res[0] == "Sel":
            tournament = res[1]
            res = self.view.rv.prompt_for_tournament_rounds_report(
                self.view, self.menu.tournament_rounds_menu(), tournaments, tournament, message)
        elif res[0] == "Mes":
            message = res[2]
            self.rc.tournament_rounds_report(self, tournaments, message)
        self.rc.get_reports(self, self.players, self.tournaments, message)

    def tournament_matchs_report(self, tournaments, message):
        tournament = ''
        res = self.view.rv.prompt_for_tournament_matchs_report(
            self.view, self.menu.tournament_matchs_menu(), tournaments, tournament, message)
        if res[0] == "Sel":
            tournament = res[1]
            res = self.view.rv.prompt_for_tournament_matchs_report(
                self.view, self.menu.tournament_matchs_menu(), tournaments, tournament, message)
        elif res[0] == "Mes":
            message = res[2]
            self.rc.tournament_matchs_report(self, tournaments, message)
        self.rc.get_reports(self, self.players, self.tournaments, message)
