LINE = "-----------------------------------------------"
TITLE = "##############################################"


class ReportView:
    def prompt_for_reports(self, menu, message):
        self.cls()
        print(menu.title)
        for choice in menu.choices:
            print(choice)
        print(LINE)
        print(message)
        print(LINE)
        entry = input("Entrez votre choix: ")
        if entry in menu.responses:
            ret = menu.responses[entry]
        else:
            ret = "Mes"
            message = "Entrée incorrecte."

        return (ret, message)

    def prompt_for_players_report(self, menu, players, sort, message):
        self.cls()
        print(menu.title)
        if not sort:
            for choice in menu.choices:
                print(choice)
            print(LINE)
            print(message)
            print(LINE)
            entry = input("Entrez votre choix: ")
            if entry in menu.responses:
                ret = menu.responses[entry]
            else:
                ret = "Mes"
                message = "Entrée incorrecte."
        else:
            print(message)
            print(LINE)
            print('{0:<10} {1:<10} {2:<10} {3:<5} {4:<4}'.format(
                "Nom", "Prénom", "Naissance", "Sexe", "Classement"))
            print(LINE)
            for player in players:
                print('{0:<10} {1:<10} {2:<10} {3:<5} {4:<4}'.format(player.last_name, player.for_name,
                      player.birthday, player.gender, player.ranking))
            ret = ''
            print(LINE)
            input("Appuyer sur une touche pour continuer...")

        return (ret, message)

    def prompt_for_tournament_players_report(self, menu, tournaments, tournament, players, sort, message):
        self.cls()
        print(menu.title)
        if tournament == '':
            for t in tournaments:
                index = tournaments.index(t)
                print(str(index) + ": " + str(t))
            print(LINE)
            print(message)
            print(LINE)
            entry = input("Entrez votre choix: ")
            lst = [format(x, 'd') for x in range(len(tournaments))]
            if entry in menu.responses:
                ret = menu.responses[entry]
            elif entry in lst:
                ret = "Sel"
                tournament = tournaments[int(entry)]
            else:
                ret = "Mes"
                message = "Entrée incorrecte."
            return (ret, tournament, message)
        else:
            print(tournament.name)
            print(LINE)
            if not sort:
                for choice in menu.choices:
                    print(choice)
                print(LINE)
                print(message)
                print(LINE)
                entry = input("Entrez votre choix: ")
                if entry in menu.responses:
                    ret = menu.responses[entry]
                else:
                    ret = "Mes"
                    message = "Entrée incorrecte."
                return (ret, tournament, message)
            else:
                print(message)
                print(LINE)
                print('{0:<10} {1:<10} {2:<10} {3:<5} {4:<10} {5:<5}'.format(
                    "Nom", "Prénom", "Naissance", "Sexe", "Classement", "Score"))
                print(LINE)
                for player in players:
                    print('{0:<10} {1:<10} {2:<10} {3:<5} {4:<10} {5:<5}'.format(player[0].last_name, player[0].for_name,
                          player[0].birthday, player[0].gender, player[0].ranking, player[1]))
                ret = ''
                print(LINE)
                input("Appuyer sur une touche pour continuer...")

    def prompt_for_tournaments_report(self, menu, tournaments):
        self.cls()
        print(menu.title)
        for tournament in tournaments:
            print('{0:<10} {1:<20} {2:<20} {3:<15} {4:<8} {5:<8} {6:<50}'.format(
                "Nom", "Description", "Date", "Localisation", "Nb Tour", "Temps", "Joueurs"))
            print(LINE * 4)
            print('{0:<10} {1:<20} {2:<20} {3:<15} {4:<8} {5:<8}'.format(tournament.name, tournament.description, tournament.date,
                  tournament.location, tournament.round_number, tournament.time_controler), tournament.players)
            print(LINE * 4)
        input("Appuyer sur une touche pour continuer...")

    def prompt_for_tournament_rounds_report(self, menu, tournaments, tournament, message):
        self.cls()
        print(menu.title)
        if tournament == '':
            for t in tournaments:
                index = tournaments.index(t)
                print(str(index) + ": " + str(t))
            print(LINE)
            print(message)
            print(LINE)
            entry = input("Entrez votre choix: ")
            lst = [format(x, 'd') for x in range(len(tournaments))]
            if entry in menu.responses:
                ret = menu.responses[entry]
            elif entry in lst:
                ret = "Sel"
                tournament = tournaments[int(entry)]
            else:
                ret = "Mes"
                message = "Entrée incorrecte."
            return (ret, tournament, message)
        else:
            print(tournament.name)
            print(LINE)
            print('{0:<4} {1:<20} {2:<20}'.format(
                "Num", "Date Début", "Date Fin"))
            print(LINE)
            for round in tournament.rounds:
                print('{0:<4} {1:<20} {2:<20}'.format(
                    round.number, round.start_date, round.end_date))
            input("Appuyer sur une touche pour continuer...")

    def prompt_for_tournament_matchs_report(self, menu, tournaments, tournament, message):
        self.cls()
        print(menu.title)
        if tournament == '':
            for t in tournaments:
                index = tournaments.index(t)
                print(str(index) + ": " + str(t))
            print(LINE)
            print(message)
            print(LINE)
            entry = input("Entrez votre choix: ")
            lst = [format(x, 'd') for x in range(len(tournaments))]
            if entry in menu.responses:
                ret = menu.responses[entry]
            elif entry in lst:
                ret = "Sel"
                tournament = tournaments[int(entry)]
            else:
                ret = "Mes"
                message = "Entrée incorrecte."
            return (ret, tournament, message)
        else:
            print(tournament.name)
            print(LINE * 2)
            print('{0:<25} {1:<5} {2:<5} {3:5} {4:<25} {5:<5} {6:<5}'.format(
                "Joueur1", "Total", "Score", "vs", "Joueur2", "Total", "Score"))
            print(LINE * 2)
            for round in tournament.rounds:
                for match in round.matchs:
                    print('{0:<25} {1:<5} {2:<5} {3:5} {4:<25} {5:<5} {6:<5}'.format(
                        str(match.player1[0]), match.player1[1], match.player1[2], "vs", str(match.player2[0]), match.player2[1], match.player2[2]))
                print(LINE * 2)
            input("Appuyer sur une touche pour continuer...")
