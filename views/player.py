import re
LINE = "-----------------------------------------------"
TITLE = "##############################################"


class PlayerView:
    def prompt_for_player(self, menu, players, message):
        self.cls()
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
        '''Create index list'''
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
        self.cls()
        print(menu.title)
        print(message)
        print(LINE)
        last_name = input("Entrez le nom du joueur: ")
        for_name = input("Entrez le prénom du joueur: ")
        birthday = input(
            "Entrez la date de naissance du joueur (JJ/MM/YYYY): ")
        gender = input("Entrez le sexe du joueur (M/F): ")
        ranking = input("Entrez le classement du joueur: ")
        print(LINE)
        for choice in menu.choices:
            print(choice)
        print(LINE)
        entry = input("Entrez votre choix: ")
        '''Check input'''
        error = ''
        regex = re.compile(r'^[0-9]{2}/[0-9]{2}/[0-9]{4}$')
        if gender not in ('M', 'F'):
            error = "Le sexe doit être M ou F."
        elif not ranking.isdigit() or int(ranking) <= 0:
            error = "Le classement doit être un entier supérieur à 0."
        elif not re.findall(regex, birthday):
            error = "Le format de l'anniversaire doit être JJ/MM/YYYY."
        if entry in menu.responses:
            if error == '':
                ret = menu.responses[entry]
                player = (last_name, for_name, birthday, gender, ranking)
            else:
                player = ''
                ret = "Mes"
                message = error
        else:
            player = ''
            ret = "Mes"
            message = "Entrée incorrecte."

        return (ret, player, message)

    def prompt_for_modify_player(self, menu, player, message):
        self.cls()
        print(menu.title)
        print(player)
        for select in menu.select:
            print(select + ": " + str(player.ranking))
        print(LINE)
        for choice in menu.choices:
            print(choice)
        print(LINE)
        print(message)
        print(LINE)
        entry = input("Entrez votre choix: ")
        if entry in menu.responses:
            ret = menu.responses[entry]
            if ret == "Mod":
                val = input("Entrez la nouvelle valeur: ")
                if not val.isdigit() or int(val) <= 0:
                    ret = "Mes"
                    message = "Le classement doit être un entier supérieur à 0."
                else:
                    message = ''
                    ret = "Mod"
                    val = int(val)
            else:
                val = ''
                message = ''
        else:
            val = ''
            ret = "Mes"
            message = "Entrée incorrecte."
        print(LINE)

        return (ret, val, message)
