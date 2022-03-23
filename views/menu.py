LINE = "-----------------------------------------------"
TITLE = "##############################################"


class Menus:

    def main_menu(self):
        self.title = TITLE + "\n ACCUEIL \n" + TITLE
        self.choices = [
            "1: Gestion Tournois",
            "2: Gestion Joueurs",
            "3: Reports",
            "B: Sauvegarder tout",
            "Q: Quitter"
        ]
        self.responses = {
            "1": "1",
            "2": "2",
            "3": "3",
            "B": "Bkup",
            "Q": "Quit"
        }

        return self

    def tournament_menu(self):
        self.title = TITLE + "\n GESTION DES TOURNOIS \n" + TITLE
        self.choices = [
            "Entrez l'id du tournoi à charger",
            "N: Nouveau tournoi",
            "R: Retourner à l'accueil"
        ]
        self.responses = {
            "N": "New",
            "R": "Ret"
        }

        return self

    def create_tournament_menu(self):
        self.title = TITLE + "\n CREATION D'UN TOURNOI \n" + TITLE
        self.choices = [
            "C: Créer tournoi",
            "A: Abandonner"
        ]
        self.responses = {
            "C": "Create",
            "A": "Abort"
        }

        return self

    def tournament_detail_menu(self):
        self.title = TITLE + "\n INFORMATION TOURNOI \n" + TITLE
        self.choices = [
            "S: Lancer le tournoi",
            "D: Supprimer le tournoi",
            "R: Retour"
        ]
        self.responses = {
            "S": "Start",
            "D": "Del",
            "R": "Ret"
        }

        return self

    def match_detail_menu(self):
        self.title = TITLE + "\n INFORMATION MATCH \n" + TITLE
        self.choices = [
            "M: Modifier les résultats",
            "R: Retour"
        ]
        self.responses = {
            "M": "Mod",
            "R": "Ret"
        }

        return self

    def add_player_menu(self):
        self.title = TITLE + "\n AJOUT D'UN JOUEUR \n" + TITLE
        self.choices = [
            "Entrez l'id du joueur à ajouter",
            "C: Ajouter Nouveau joueur",
            "S: Stop"
        ]
        self.responses = {
            "C": "Create",
            "S": "Stop"
        }

        return self

    def player_menu(self):
        self.title = TITLE + "\n GESTION DES JOUEURS \n" + TITLE
        self.choices = [
            "Entrez l'id du joueur pour le modifier",
            "N: Nouveau joueur",
            "R: Retourner à l'accueil"
        ]
        self.responses = {
            "N": "New",
            "R": "Ret"
        }

        return self

    def create_player_menu(self):
        self.title = TITLE + "\n CREATION D'UN JOUEUR \n" + TITLE
        self.choices = [
            "C: Créer joueur",
            "A: Abandonner"
        ]
        self.responses = {
            "C": "Create",
            "A": "Abort"
        }

        return self

    def modify_player_menu(self):
        self.title = TITLE + "\n MODIFCATION D'UN JOUEUR \n" + TITLE
        self.select = [
            # "1: Nom",
            # "2: Prénom",
            # "3: Naissance",
            # "4: Sexe",
            "Classement"
        ]
        self.choices = [
            "M: Modifier",
            "S: Supprimer",
            "A: Abandonner"
        ]
        self.responses = {
            "M": "Mod",
            "S": "Del",
            "A": "Abort"
        }

        return self

    def is_checked(self, menu):
        pass

    def reports_menu(self):
        self.title = TITLE + "\n GESTION DES RAPPORT \n" + TITLE
        self.choices = [
            "1: Tous les joueurs",
            "2: Tous les joueurs d'un tournoi",
            "3: Tous les tournois",
            "4: Tous les tours d'un tournoi",
            "5: Tous les matchss d'un tournoi",
            "R: Retourner à l'accueil"
        ]
        self.responses = {
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "R": "Ret"
        }

        return self

    def players_report_menu(self):
        self.title = TITLE + "\n RAPPORT JOUEURS\n" + TITLE
        self.choices = [
            "1: Ordre alphabétique",
            "2: Par classement",
            "R: Retour"
        ]
        self.responses = {
            "1": "1",
            "2": "2",
            "R": "Ret"
        }

        return self

    def tournament_players_report_menu(self):
        self.title = TITLE + "\n RAPPORT JOUEURS PAR TOURNOI\n" + TITLE
        self.choices = [
            "1: Ordre alphabétique",
            "2: Par classement",
            "R: Retour"
        ]
        self.responses = {
            "1": "1",
            "2": "2",
            "R": "Ret"
        }

        return self

    def tournaments_report_menu(self):
        self.title = TITLE + "\n RAPPORT TOURNOI\n" + TITLE

        return self

    def tournament_rounds_menu(self):
        self.title = TITLE + "\n RAPPORT ROUNDS PAR TOURNOI\n" + TITLE

        return self

    def tournament_matchs_menu(self):
        self.title = TITLE + "\n RAPPORT MATCHS PAR TOURNOI\n" + TITLE

        return self
