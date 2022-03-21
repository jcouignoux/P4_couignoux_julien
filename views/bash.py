import os
LINE = "-----------------------------------------------"
TITLE = "##############################################"


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class BashView():

    def prompt_for_main(self, menu):
        cls()
        print(menu.title)
        for choice in menu.choices:
            print(choice)
        print(LINE)
        entry = input("Que souhaitez-vous faire: ")
        if entry in menu.responses:
            res = menu.responses[entry]
        else:
            print("Entrée incorrecte,\nappuyer sur une touche pour réessayer.")
            input("")
            self.prompt_for_main(menu)

        return res

    def prompt_for_player(self, menu, players):
        """Prompt for a name."""
        cls()
        print(menu.title)
        for player in players:
            index = players.index(player)
            print(str(index) + ": " + str(player) +
                  " (" + str(player.birthday) + ", " + str(player.gender) +
                  ", " + str(player.ranking) + ")")
        print(LINE)
        for choice in menu.choices:
            print(choice)
        print(LINE)
        entry = input("Entrez votre choix: ")
        lst = [format(x, 'd') for x in range(len(players))]
        if entry in lst:
            player = players[int(entry)]
            ret = "Mod"
        elif entry in menu.responses:
            player = ""
            ret = menu.responses[entry]
        else:
            print("Entrée incorrecte,\nappuyer sur une touche pour réessayer.")
            input("")
            self.prompt_for_player(menu, players)

        return ret, player

    def prompt_for_add_player(self, menu, tournament, players, message):
        cls()
        ret = ''
        print(menu.title)
        for player in players:
            index = players.index(player)
            print(str(index) + ": " + str(player))
        print(LINE)
        print(tournament.players)
        print(LINE)
        for choice in menu.choices:
            print(choice)
        print(LINE)
        print(message)
        entry = input("Entrez votre choix: ")
        lst = [format(x, 'd') for x in range(len(players))]
        print(LINE)
        # print('---' + entry + '---' + str(lst) + '---')
        if entry in lst:
            player = players[int(entry)]
            if player not in tournament.players:
                # print('test')
                ret = "Add"
                # print(ret)
            else:
                message = "Joueur déjà sélectionné."
                self.prompt_for_add_player(menu, tournament, players, message)
        elif entry in menu.responses:
            player = ""
            ret = menu.responses[entry]
        else:
            message = "Entrée incorrecte,\nappuyer sur une touche pour réessayer."
            self.prompt_for_add_player(menu, tournament, players, message)

        return ret, player

    def prompt_for_create_player(self, menu):
        cls()
        print(menu.title)
        last_name = input("Entrez le nom du joueur: ")
        for_name = input("Entrez le prénom du joueur: ")
        birthday = input(
            "Entrez la date de naissance du joueur (JJ/MM/YY): ")
        gender = input("Entrez le sexe du joueur (M/F): ")
        ranking = input("Entrez le classement du joueur: ")
        print(LINE)
        for choice in menu.choices:
            print(choice)
        print(LINE)
        entry = input("Entrez votre choix: ")
        if entry in menu.responses:
            ret = menu.responses[entry]
            player = (last_name, for_name, birthday, gender, ranking)
        else:
            print("Entrée incorrecte,\nappuyer sur une touche pour réessayer.")
            input("")
            self.prompt_for_add_player(menu)

        return ret, player

    def prompt_for_modify_player(self, menu, player):
        cls()
        print(menu.title)
        print(player)
        for select in menu.select:
            print(select + ": " + str(player.ranking))
        print(LINE)
        # sel = int(input("Entrez l'id à modifier: "))
        # print(LINE)
        # if sel in range(len(menu.select) + 1):
        #     print("Modification")
        val = input("Entrez la nouvelle valeur: ")
        for choice in menu.choices:
            print(choice)
        entry = input("Valider ou Abandonner: ")
        if entry in menu.responses:
            ret = menu.responses[entry]
        else:
            print("Entrée incorrecte,\nappuyer sur une touche pour réessayer.")
            input("")
            self.prompt_for_modify_player(menu, player)
        print(LINE)

        return ret, val

    def prompt_for_tournament(self, menu, tournaments):
        """Prompt for tournament."""
        cls()
        print(menu.title)
        for tournament in tournaments:
            index = tournaments.index(tournament)
            print(str(index) + ": " + str(tournament))
        print(LINE)
        for choice in menu.choices:
            print(choice)
        print(LINE)
        entry = input("Entrez votre choix: ")
        lst = [format(x, 'd') for x in range(len(tournaments))]
        if entry in menu.responses:
            ret = menu.responses[entry]
            tournament = ''
        elif entry in lst:
            ret = "View"
            tournament = tournaments[int(entry)]
            tournament = int(entry)
        else:
            print("Entrée incorrecte,\nappuyer sur une touche pour réessayer.")
            input("")
            self.prompt_for_tournament(menu, tournaments)

        return ret, tournament

    def prompt_for_new_tournament(self, menu):
        cls()
        ret = ''
        print(menu.title)
        name = input("Nom: ")
        description = input("Description: ")
        location = input("Localisation: ")
        round_number = input("Nombre de tours: ")
        time_controler = input("Gestion du temps: ")
        print(LINE)
        for choice in menu.choices:
            print(choice)
        print(LINE)
        entry = input("Entrez votre choix: ")
        if entry in menu.responses:
            ret = menu.responses[entry]
            tournament_infos = (name, description, location,
                                round_number, time_controler)
        else:
            print("Entrée incorrecte,\nappuyer sur une touche pour réessayer.")
            input("")
            self.prompt_for_new_tournament(menu)

        return ret, tournament_infos

    def prompt_for_tournament_detail(self, menu, tournament):
        cls()
        ret = ''
        match_index = ''
        print(menu.title)
        print(
            "Nom: " + str(tournament.name) +
            " - " +
            "Description: " + str(tournament.description)
        )
        print(
            "Localisation: " + str(tournament.location) +
            " - " +
            "Date: " + str(tournament.date)
        )
        print(
            "Nombre de tours: " + str(tournament.round_number) +
            " - " +
            "Gestion du Temps: " + str(tournament.time_controler)
        )
        print(LINE)
        print("Classement des joueurs")
        print(LINE)
        players_list = []
        for match in tournament.rounds[-1].matchs:
            players_list.append(match.player1)
            players_list.append(match.player2)
        player_sorted = sorted(
            players_list, key=lambda k: (-k[1], k[0].ranking))
        for player in player_sorted:
            print("  " + str(player_sorted.index(player) + 1) +
                  " - " + str(player[0]) + " (" + str(player[0].ranking) + ")" +
                  ": " + str(player[1])
                  )
        print(LINE)
        if len(tournament.rounds) == 0:
            for choice in menu.choices:
                print(choice)
            entry = input("Entrez votre choix: ")
            if entry in menu.responses:
                ret = menu.responses[entry]
            else:
                print("Entrée incorrecte,\nappuyer sur une touche pour réessayer.")
                input("")
                self.prompt_for_tournament_detail(menu, tournament)
        else:
            if len(tournament.rounds) == int(tournament.round_number):
                menu.choices = [
                    "C: Clore le tournoi",
                    "R: Retour"
                ]
                menu.responses = {"T": "Close", "R": "Ret"}
            else:
                menu.choices = [
                    "Entrez l'id du match à valider",
                    # "Nouveau tour",
                    "V: Valider le tour",
                    "R: Retour"
                ]
                menu.responses = {"V": "Val", "R": "Ret"}
        print(LINE)
        for round in tournament.rounds:
            print(
                "Tour " + str(round.number) +
                " - " +
                "Début: " + str(round.start_date) +
                " - " +
                "Fin: " + str(round.end_date)
            )
            print(LINE)
            for match in round.matchs:
                print(str(round.matchs.index(match)) +
                      str(" - ") +
                      str(match.player1) + " vs " +
                      str(match.player2))
            print(LINE)

        for choice in menu.choices:
            print(choice)
        print(LINE)
        entry = input("Entrez votre choix: ")
        lst = [format(x, 'd') for x in range(len(round.matchs))]
        if entry in menu.responses:
            ret = menu.responses[entry]
        elif entry in lst:
            ret = "Mod"
            match = round.matchs[int(entry)]
            match_index = int(entry)
        else:
            print("Entrée incorrecte,\nappuyer sur une touche pour réessayer.")
            input("")
            self.prompt_for_tournament_detail(menu, tournament)

        return ret, tournament, match_index

    def prompt_for_match_detail(self, menu, tournament, match_index):
        cls()
        print(menu.title)
        print("N°   Joueur    Total     Score")
        print(LINE)
        match = tournament.rounds[-1].matchs[match_index]
        print("1 - " + str(match.player1[0]) +
              ": " + str(match.player1[1]) +
              " " + str(match.player1[2]))
        print("2 - " + str(match.player2[0]) +
              ": " + str(match.player2[1]) +
              " " + str(match.player2[2]))
        print(LINE)
        score1 = input("Entrez le score du joueur 1: ")
        score2 = input("Entrez le score du joueur 2: ")
        if score1 in ('0', '0.5', '1') and score2 in ('0', '0.5', '1'):
            scores = (float(score1), float(score2))
        else:
            print(
                "Le score doit être 0, 0.5 ou 1,\nappuyer sur une touche pour réessayer.")
            input("")
            self.prompt_for_match_detail(menu, tournament, match_index)
        print(LINE)
        for choice in menu.choices:
            print(choice)
        print(LINE)
        entry = input("Entrez votre choix: ")
        if entry in menu.responses:
            ret = menu.responses[entry]
        else:
            print("Entrée incorrecte,\nappuyer sur une touche pour réessayer.")
            input("")
            self.prompt_for_match_detail(menu, tournament, match_index)
        return ret, scores
