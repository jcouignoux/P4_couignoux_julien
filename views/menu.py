LINE = "-----------------------------------------------"
TITLE = "##############################################"


class Menus:

    def main_menu(self):
        self.title = TITLE + "\n ACCUEIL \n" + TITLE
        self.choices = [
            "1: Gestion Tournois",
            "2: Gestion Joueurs",
            "B: Sauvegarder tout",
            "Q: Quitter"
        ]
        self.responses = {
            "1": "1",
            "2": "2",
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
            "R: Retour"
        ]
        self.responses = {
            "S": "Start",
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
