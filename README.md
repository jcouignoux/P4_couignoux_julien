# P4_couignoux_julien

![](https://user.oc-static.com/upload/2020/09/22/16007793690358_chess%20club-01.png)
## ChessApp

Application to manage an chess tournament with swiss rules.

-----
> Run the script with the command *python main.py*

## TOURNAMENT

![](README/main_page.png)

> Manage the tournaments from __1: Gestion Tournois__

![](README/tournament_manage_page.png)

> Create a new tournament with  __N: Nouveau tournoi__ and add players

![](README/create_tournament_page.png)

![](README/add_player_page.png)

> Or open a tournament with its __id__

![](README/tournement_details.png)

![](README/create_tournament_page.png)

> Enter the score with the match id and validate the round with __V: Valider le tour__

![](README/math_update.png)

The next round is automatly created



![](README/round_added.png)

## PLAYER

> Manage the players from __2: Gestion Joueurs__

![](README/player_manage_page.png)

> Create new player with __C: Ajouter Nouveau joueur__ or modify rank with player id 

![](README/create_player.png)

![](README/modify_player.png)

> Backup players and tournaments with __B: Sauvegarder tout__

![](README/main_page.png)

## REPORT

> Manage the Report from __3: Reports__

![](README/report_page.png)
-----
> How to generate a flake8 report

From the root directory, run : 

*flake8 --format=html --htmldir=flake-report*