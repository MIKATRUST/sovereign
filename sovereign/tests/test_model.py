#!/usr/bin/env python3

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

    def test_add_get_bip39_sentance(self):
        model = Model()
        fun1 = model.add_bip39_sentance
        fun2 = model.get_bip39_sentances

        SENT0 = ('zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo abstract')
        SENT1 = ('zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo wrong')  
        SENT2 = ('abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about')

        fun1(SENT0)
        self.assertEqual(len(fun2()), 1)
        self.assertEqual(fun2()[0], SENT0)

        fun1(SENT1)
        self.assertEqual(len(fun2()), 2)
        self.assertEqual(fun2()[0], SENT0)
        self.assertEqual(fun2()[1], SENT1)

        fun1(SENT2)
        self.assertEqual(len(fun2()), 3)
        self.assertEqual(fun2()[0], SENT0)
        self.assertEqual(fun2()[1], SENT1)
        self.assertEqual(fun2()[2], SENT2)

    def test_get_set_mode(self):
        model = Model()
        fun1 = model.get_mode
        fun2 = model.set_mode

        #default mode is 24 words
        self.assertEqual(fun1(), 24)

        fun2(12)
        self.assertEqual(fun1(), 12)

        fun2(18)
        self.assertEqual(fun1(), 18)

if __name__ == '__main__':
    unittest.main()
