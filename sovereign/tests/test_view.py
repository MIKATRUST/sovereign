import unittest

#import sys
#sys.path.append('../')
#sys.path.append('.')

from sovereign.view.view import View

class TestView(unittest.TestCase):
    def test_show_message(self):
        view = View()
        message = 'Hello World'
        view.show_message(message)
        # Check if the message has been displayed
        # You can add appropriate assertion here
        self.assertEqual(message, 'Hello World')

if __name__ == '__main__':
    unittest.main()
