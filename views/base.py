

class Views:

    # def __init__(self, active_view, views):
    def __init__(self, active_view):
        self.active_view = active_view
        # self.views = views

    def prompt_for_main(self, menu, message):
        return self.active_view.prompt_for_main(menu, message)

    def prompt_for_player(self, menu, players, message):
        return self.active_view.prompt_for_player(menu, players, message)

    def prompt_for_add_player(self, menu, tournament, players, message):
        return self.active_view.prompt_for_add_player(menu, tournament, players, message)

    def prompt_for_create_player(self, menu, message):
        return self.active_view.prompt_for_create_player(menu, message)

    def prompt_for_modify_player(self, menu, player, message):
        return self.active_view.prompt_for_modify_player(menu, player, message)

    def prompt_for_tournament(self, menu, tournaments, message):
        return self.active_view.prompt_for_tournament(menu, tournaments, message)

    def prompt_for_new_tournament(self, menu, message):
        return self.active_view.prompt_for_new_tournament(menu, message)

    def prompt_for_tournament_detail(self, menu, tournament, message):
        return self.active_view.prompt_for_tournament_detail(menu, tournament, message)

    def prompt_for_match_detail(self, menu, tournament, match_index, message):
        return self.active_view.prompt_for_match_detail(menu, tournament, match_index, message)

    def prompt_for_players_report(self, menu, players, sort, message):
        return self.active_view.prompt_for_players_report(menu, players, sort, message)

    def prompt_tournament_players_report(self, menu, tournaments, tournament, players, sort, message):
        return self.active_view.prompt_tournament_players_report(menu, tournaments, tournament, players, sort, message)

    def prompt_tournaments_report(self, menu, tournaments):
        return self.active_view.prompt_tournament_report(menu, tournaments)

    def prompt_tournament_rounds_report(self, menu, tournaments, tournament, message):
        return self.active_view.prompt_tournament_rounds_report(menu, tournaments, tournament, message)

    def prompt_tournament_matchs_report(self, menu, tournaments, tournament, message):
        return self.active_view.prompt_tournament_matchs_report(menu, tournaments, tournament, message)
