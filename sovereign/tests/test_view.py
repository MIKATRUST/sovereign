'''Demonstrates triple double quotes
docstrings and does nothing really.'''

import unittest
from sovereign.view.view import View

class TestView(unittest.TestCase):

    '''Demonstrates triple double quotes
    docstrings and does nothing really.'''

    def test_show_message(self):
        """Function printing python version."""
        view = View()
        self.assertEqual(5, 5)

    def test_one(self):
        """Function printing python version."""
        self.assertEqual(5, 5)

if __name__ == '__main__':
    unittest.main()
