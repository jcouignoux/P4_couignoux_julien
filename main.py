#!/usr/bin/env python
# -*- coding: utf-8 -*-

from controllers.base import Controller

from views.base import Views
# from views.bash import BashView


def main():

    # active_view = BashView()
    # views = Views(active_view)
    view = Views()

    game = Controller(view)
    game.run()


if __name__ == "__main__":
    main()
