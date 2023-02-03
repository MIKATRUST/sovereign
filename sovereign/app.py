
from sovereign.model.model import Model
from sovereign.view.view import View
from sovereign.controller.controller import Controller

def run():
#    print("RR This is the main function.")
#    controller = Controller()

# Client code
#if __name__ == "__main__":
    controller = Controller()
#    model = Model()
#    view = View()

    controller.view.clear()

    while True:
        controller.view.display_menu(int(controller.model.get_mode()))
        choice = controller.view.get_menu_choice()
        #controller.userInputIsValid()
        if choice in controller.options:
            controller.options[choice]()
            #getattr(toto, "option" + user_input)()
            #toto.option1()
        else:
            controller.view.handle_invalid_choice()

