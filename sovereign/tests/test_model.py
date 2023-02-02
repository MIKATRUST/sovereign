import unittest

#import sys
#sys.path.append('../')
#sys.path.append('.')

from sovereign.model.model import Model

class TestModel(unittest.TestCase):
    def test_get_data(self):
        model = Model(10)
        message = model.get_data()
        self.assertEqual(message, 20)

if __name__ == '__main__':
    unittest.main()
