#!/usr/bin/env python
# -*- coding: utf-8 -*-

from controllers.base import Controller

from views.base import Views
from views.bash import BashView
from views.tkinter import TkinterView
from datas.base import DataBase
from datas.tinydb import TinyDb


def main():

    active_view = BashView()
    # active_view = TkinterView(None)
    # passive_views = (active_view, TkinterView(None))
    # views = Views(active_view, passive_views)
    views = Views(active_view)

    active_db = TinyDb()
    db = DataBase(active_db)

    game = Controller(views, db)
    game.run()


if __name__ == "__main__":
    main()
    # apps(None).mainloop()
