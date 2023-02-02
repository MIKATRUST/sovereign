
from sovereign.model.model import Model
from sovereign.view.view import View

class Controller:
    def __init__(self):
        print("constructor Controller")
        self.model = Model(10)
        self.view = View()

    def get_message(self):
        message = self.model.get_data()
        return message
