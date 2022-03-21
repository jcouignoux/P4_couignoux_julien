

class Views:

    # def __init__(self, active_view, views):
    def __init__(self, active_view):
        self.active_view = active_view
        # self.views = views

    def prompt_for_main(self, menu):
        return self.active_view.prompt_for_main(menu)

    def prompt_for_player(self, menu, players):
        return self.active_view.prompt_for_player(menu, players)

    def prompt_for_add_player(self, menu, tournament, players, message):
        return self.active_view.prompt_for_add_player(menu, tournament, players, message)

    def prompt_for_create_player(self, menu):
        return self.active_view.prompt_for_create_player(menu)

    def prompt_for_modify_player(self, menu, player):
        return self.active_view.prompt_for_modify_player(menu, player)

    def prompt_for_tournament(self, menu, tournaments):
        return self.active_view.prompt_for_tournament(menu, tournaments)

    def prompt_for_new_tournament(self, menu):
        return self.active_view.prompt_for_new_tournament(menu)

    def prompt_for_tournament_detail(self, menu, tournament):
        return self.active_view.prompt_for_tournament_detail(menu, tournament)

    def prompt_for_match_detail(self, menu, tournament, match_index):
        return self.active_view.prompt_for_match_detail(menu, tournament, match_index)
