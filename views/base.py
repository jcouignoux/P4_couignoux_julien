

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
