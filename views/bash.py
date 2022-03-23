import os
LINE = "-----------------------------------------------"
TITLE = "##############################################"


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class BashView():

    def prompt_for_main(self, menu, message):
        cls()
        print(menu.title)
        for choice in menu.choices:
            print(choice)
        print(LINE)
        print(message)
        print(LINE)
        entry = input("Que souhaitez-vous faire: ")
        if entry in menu.responses:
            return (menu.responses[entry], message)
        else:
            message = "Entrée incorrecte."
            return ("Mes", message)

    def prompt_for_player(self, menu, players, message):
        cls()
        print(menu.title)
        for player in players:
            index = players.index(player)
            print(str(index) + ": " + str(player) +
                  " (" + str(player.birthday) + ", " + str(player.gender) +
                  ", " + str(player.ranking) + ")")
        print(LINE)
        print(message)
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
            ret = "Mes"
            message = "Entrée incorrecte."

        return (ret, player, message)

    def prompt_for_add_player(self, menu, tournament, players, message):
        cls()
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
        print(LINE)
        print(len(tournament.players))
        print(int(tournament.round_number))
        entry = input("Entrez votre choix: ")
        lst = [format(x, 'd') for x in range(len(players))]
        print(LINE)
        if entry in lst:
            player = players[int(entry)]
            if player not in tournament.players:
                ret = "Add"
            else:
                ret = 'Mes'
                pleyer = ''
                message = "Joueur déjà sélectionné."
        elif entry in menu.responses:
            if entry == "S":
                player = ''
                ret = menu.responses[entry]
                if len(tournament.players) <= int(tournament.round_number):
                    ret = "Mes"
                    message = "Il doit y avoir au moins un joueur de plus que de tour"
                if (len(tournament.players) % 2) == 0:
                    ret = "Mes"
                    message = "Il doit y avoir un nombre de joueurs paire"
                # else:
                #     ret = menu.responses[entry]
            else:
                player = ""
                ret = menu.responses[entry]
        else:
            player = ''
            ret = "Mes"
            message = "Entrée incorrecte."

        return (ret, player, message)

    def prompt_for_create_player(self, menu, message):
        cls()
        print(menu.title)
        print(message)
        print(LINE)
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
            ret = "Mes"
            message = "Entrée incorrecte."

        return (ret, player, message)

    def prompt_for_modify_player(self, menu, player, message):
        cls()
        print(menu.title)
        print(player)
        for select in menu.select:
            print(select + ": " + str(player.ranking))
        print(LINE)
        print(message)
        print(LINE)
        val = input("Entrez la nouvelle valeur: ")
        for choice in menu.choices:
            print(choice)
        entry = input("Valider ou Abandonner: ")
        if entry in menu.responses:
            ret = menu.responses[entry]
            message = ''
            if isinstance(val, int):
                ret = "Mod"
                val = int(val)
        else:
            ret = "Mes"
            message = "Entrée incorrecte."
        print(LINE)

        return (ret, val, message)

    def prompt_for_tournament(self, menu, tournaments, message):
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
        print(message)
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
            ret = "Mes"
            message = "Entrée incorrecte."

        return (ret, tournament, message)

    def prompt_for_new_tournament(self, menu, message):
        cls()
        print(menu.title)
        print(message)
        print(LINE)
        name = input("Nom: ")
        description = input("Description: ")
        location = input("Localisation: ")
        round_number = input("Nombre de tours (default 4): ") or 4
        time_controler = input("Gestion du temps: ")
        print(LINE)
        for choice in menu.choices:
            print(choice)
        print(LINE)
        entry = input("Entrez votre choix: ")
        if entry in menu.responses:
            message = ''
            ret = menu.responses[entry]
            tournament_infos = (name, description, location,
                                round_number, time_controler)
        else:
            tournament_infos = ''
            ret = "Mes"
            message = "Entrée incorrecte."

        return (ret, tournament_infos, message)

    def prompt_for_tournament_detail(self, menu, tournament, message):
        cls()
        # ret = ''
        match_index = ''
        print(message)
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
            print(message)
            print(LINE)
            entry = input("Entrez votre choix: ")
            if entry in menu.responses:
                ret = menu.responses[entry]
            else:
                ret = "Mes"
                message = "Entrée incorrecte."
        else:
            if len(tournament.rounds) == int(tournament.round_number):
                menu.choices = [
                    "C: Clore le tournoi",
                    "D: Supprimer le tournoi",
                    "R: Retour"
                ]
                menu.responses = {"T": "Close", "D": "Del", "R": "Ret"}
            else:
                menu.choices = [
                    "Entrez l'id du match à valider",
                    "V: Valider le tour",
                    "D: Supprimer le tournoi",
                    "R: Retour"
                ]
                menu.responses = {"V": "Val", "D": "Del", "R": "Ret"}
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
        print(message)
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
            ret = "Mes"
            message = "Entrée incorrecte."

        return (ret, tournament, match_index, message)

    def prompt_for_match_detail(self, menu, tournament, match_index, message):
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
        print(message)
        print(LINE)
        score1 = input("Entrez le score du joueur 1: ")
        score2 = input("Entrez le score du joueur 2: ")
        if score1 in ('0', '0.5', '1') and score2 in ('0', '0.5', '1'):
            scores = (float(score1), float(score2))
            message = ''
        else:
            scores = ''
            ret = "Mes"
            message = "Le score doit être 0, 0.5 ou 1."
            return (ret, scores, message)
        print(LINE)
        for choice in menu.choices:
            print(choice)
        print(LINE)
        print(message)
        print(LINE)
        entry = input("Entrez votre choix: ")
        if entry in menu.responses:
            ret = menu.responses[entry]
        else:
            scores = ''
            ret = "Mes"
            message = "Entrée incorrecte."
        return (ret, scores, message)
