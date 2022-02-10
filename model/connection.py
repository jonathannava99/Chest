#! /usr/bin/envs python3
# coding: utf-8

import sqlite3


class Connection:

    def getConnection(self):

        try:
            connection = sqlite3.connect("chest.db")
            return connection
        except NameError:
            print("La connexion à la base de données a échoué,{}".format(NameError))
