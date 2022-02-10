#! /usr/bin/envs python3
# coding: utf-8
from view.lists.template_list import TemplateList


class TemplateMenu:

    def choice_menu(self, menu: list) -> str:
        """Create the main menu with the options inside the list.

        Attrs:
        - menu (list): la liste est utilisé pour créer le menu.

        Returns:
        - the number of the option chosen by the user
        """
        menu_id = TemplateList().choicelist("Choissisez une option", menu)[0]
        return menu_id
