'''Demonstrates triple double quotes
docstrings and does nothing really.'''

import unittest
from ..model.model import Model

'''Demonstrates triple double quotes
docstrings and does nothing really.'''


class TestModel(unittest.TestCase):

    def test_set_mode(self):
        """Function printing python version."""
        model = Model()
        mode = int(model.get_mode())
        self.assertEqual(mode, 24)
        model.set_mode(12)
        mode = int(model.get_mode())
        self.assertEqual(mode, 12)

    def test_blabla(self):
        """Function printing python version."""
        self.assertEqual(5, 5)

    def test_blabla2(self):
        """Function printing python version."""
        self.assertEqual(5, 5)


if __name__ == '__main__':
    unittest.main()
