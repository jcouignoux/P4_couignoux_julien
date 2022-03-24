LINE = "-----------------------------------------------"
TITLE = "##############################################"


class PlayerView:
    def prompt_for_player(self, menu, players, message):
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

    def prompt_for_create_player(self, menu, message):
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
            player = ''
            ret = "Mes"
            message = "Entrée incorrecte."

        return (ret, player, message)

    def prompt_for_modify_player(self, menu, player, message):
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
