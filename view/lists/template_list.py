#! /usr/bin/envs python3
# coding: utf-8
import inquirer


class TemplateList:

    def __init__(self):
        pass

    def choicelist(self, message: str, choices: list) -> str:
        """Create a the list of items that the user can select

        Attrs:
        - message (string): A message that the user gonna read
        - choices (list): A list that is the options of a menu

        Returns:
        - The option selected by the user
        """
        questions = [
            inquirer.List('options',
                          message=message,
                          choices=choices,
                          ),
        ]
        option = inquirer.prompt(questions)
        selected_option = option['options']
        return selected_option

    def list(self, list_elements: list, message1: str, message2: str) -> [str, int]:
        """Create a the list of items that the user can select

        Attrs:
        - message (string): A message that the user gonna read
        - choices (list): A list of tournament items like games, turns or players

        Returns:
        - A number int that represents the option selected by the user
        """
        if len(list_elements) == 0:
            return self.choicelist(message1, ["Revenir en arrière"])
        else:
            list_elements.insert(0, "Revenir en arrière")
            object_id = self.choicelist(message2, list_elements)
            if object_id != "Revenir en arrière":
                object_id = [s for s in object_id.split(",")]
                object_id = [int(s) for s in object_id[0].split() if s.isdigit()][0]
                return object_id

            else:
                return object_id
