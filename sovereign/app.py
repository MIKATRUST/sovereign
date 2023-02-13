#!/usr/bin/env python3


'''Demonstrates triple double quotes
docstrings and does nothing really.'''

from sovereign.controller.controller import Controller


def run():
    '''Demonstrates triple double quotes
    docstrings and does nothing really.'''

    controller = Controller()
    controller.view.clear()

    while True:
        controller.view.display_menu(controller.model.get_mode)
        choice = controller.view.get_menu_choice()
        if choice in controller.options:
            controller.options[choice]()
        else:
            controller.view.handle_invalid_choice()
