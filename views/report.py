LINE = "-----------------------------------------------"
TITLE = "##############################################"


class ReportView:
    def prompt_for_reports(self, menu, message):
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
            print("Nom Prénom Naissance Sexe Classement")
            print(LINE)
            for player in players:
                print(player.last_name, player.for_name,
                      player.birthday, player.gender, player.ranking)
            ret = ''
            print(LINE)
            input("Appuyer sur une touche pour continuer...")

        return (ret, message)

    def prompt_for_tournament_players_report(self, menu, tournaments, tournament, players, sort, message):
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
                print("Nom Prénom Naissance Sexe Classement Score")
                print(LINE)
                for player in players:
                    print(player[0].last_name, player[0].for_name,
                          player[0].birthday, player[0].gender, player[0].ranking, player[1])
                ret = ''
                print(LINE)
                input("Appuyer sur une touche pour continuer...")

    def prompt_for_tournaments_report(self, menu, tournaments):
        print(menu.title)
        for tournament in tournaments:
            print("Nom Description Date Localisation Nb Tour Temps Joueurs")
            print(LINE)
            print(tournament.name, tournament.description, tournament.date,
                  tournament.location, tournament.round_number, tournament.time_controler,
                  tournament.players)
            print(LINE)
        input("Appuyer sur une touche pour continuer...")

    def prompt_for_tournament_rounds_report(self, menu, tournaments, tournament, message):
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
            print("Num Date Début Date Fin")
            print(LINE)
            for round in tournament.rounds:
                print(round.number, round.start_date, round.end_date)
            input("Appuyer sur une touche pour continuer...")

    def prompt_for_tournament_matchs_report(self, menu, tournaments, tournament, message):
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
            print("Joueur1 Joueur2")
            print(LINE)
            for round in tournament.rounds:
                for match in round.matchs:
                    print(match.player1, match.player2)
            input("Appuyer sur une touche pour continuer...")
