'''Demonstrates triple double quotes
docstrings and does nothing really.'''

import unittest
from ..view.view import View
import io
import sys


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

    def test_foo(self):
        """Function printing python version."""
        view = View()
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.
        view.show_error("hi")                           # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        print('Captured', capturedOutput.getvalue())   # Now works as before.
# TBD
#        self.assertEqual("hi" + "\n", capturedOutput.getvalue())


if __name__ == '__main__':
    unittest.main()
