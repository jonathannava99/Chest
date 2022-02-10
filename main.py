#! /usr/bin/envs python3
# coding: utf-8
from controller.control_menus.control_main_menu import ControlMainmenu
from database.tables import Tables


def main():
    table = Tables()
    table.create_table_game()
    table.create_table_player()
    table.create_table_turn()
    table.create_table_tournament()
    mainview = ControlMainmenu()
    mainview.changeView()


if __name__ == "__main__":
    main()
else:
    print('You must launch the file in main file')
