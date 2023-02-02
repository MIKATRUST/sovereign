import unittest

#import sys
#sys.path.append('../')
#sys.path.append('.')

from sovereign.controller.controller import Controller

class TestController(unittest.TestCase):
    def test_get_message(self):
        controller = Controller()
        message1 = controller.get_message()
        #message2 = controller.show_message('Hello World')
        # Check if the message has been displayed
        # You can add appropriate assertion here
        self.assertEqual(message1, 20) #from model
        ##self.assertEqual(message2, 'Hello World') #from view

if __name__ == '__main__':
    unittest.main()

# def get_message(self):
#message = self.model.get_message()
#self.view.show_message(message)
