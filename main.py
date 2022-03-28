#!/usr/bin/env python
# -*- coding: utf-8 -*-

from controllers.base import Controller

from views.base import Views
from datas.tinydb import DataBase


def main():

    view = Views()
    dbase = DataBase()

    game = Controller(view, dbase)
    game.run()


if __name__ == "__main__":
    main()
