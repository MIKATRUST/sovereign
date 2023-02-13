#!/usr/bin/env python3

'''Demonstrates triple double quotes
docstrings and does nothing really.'''

import unittest
from ..bip39.bip39 import Bip39

'''Demonstrates triple double quotes
docstrings and does nothing really.'''


class TestBip39(unittest.TestCase):

    def test_is_valid_bip39_words(self):
        """Function printing python version."""
        bip39 = Bip39() 
        self.assertEqual(True, bip39.is_valid_bip39_words('zoo zoo zoo'))
        self.assertEqual(False, bip39.is_valid_bip39_words('zoo zooo zoo'))
        self.assertEqual(False, bip39.is_valid_bip39_words('zooo zooo zoo'))
        self.assertEqual(False, bip39.is_valid_bip39_words('zoo zooo zooo'))
        self.assertEqual(True, bip39.is_valid_bip39_words('abandon abandon abandon'))
        self.assertEqual(False, bip39.is_valid_bip39_words('aaaabandon abandon abandon'))
        self.assertEqual(False, bip39.is_valid_bip39_words('abandon aaaabandon abandon'))
        self.assertEqual(False, bip39.is_valid_bip39_words('abandon abandon aaaabandon'))

    def test_is_valid_bip39_length(self):
        """Function printing python version."""
        bip39 = Bip39()
        #correct sentances
        sentance_12c = 'pigeon pave board visual mixed monitor trophy couple hungry expand lawsuit next'
        sentance_15c = 'insane citizen junk trim violin dog damp audit license then ski donor dust similar decorate'
        sentance_18c = 'stamp crush area flag since index chalk wild cattle coffee december local polar sick agent execute brown author'
        sentance_21c = 'hole bonus chat essence ten wrestle other payment name old purpose decline again need twelve devote execute chief notice install syrup'
        sentance_24c = 'choice excess visual burger forum caution like sugar fan card use alone orient doll legal good exclude rebel fold boy tobacco solid fix foot'

        self.assertEqual(True, bip39.is_valid_bip39_length(sentance_12c))
        self.assertEqual(True, bip39.is_valid_bip39_length(sentance_15c))
        self.assertEqual(True, bip39.is_valid_bip39_length(sentance_18c))
        self.assertEqual(True, bip39.is_valid_bip39_length(sentance_21c))
        self.assertEqual(True, bip39.is_valid_bip39_length(sentance_24c))
        self.assertEqual(False, bip39.is_valid_bip39_length(''))
        self.assertEqual(False, bip39.is_valid_bip39_length('zoo'))
        self.assertEqual(False, bip39.is_valid_bip39_length('zoo zoo'))
        self.assertEqual(False, bip39.is_valid_bip39_length('zoo zoo zoo'))
        self.assertEqual(False, bip39.is_valid_bip39_length('1 2 3 4 5 6 7 8 9 10 11 12 13'))

    def test_is_valid_bip39_sentence(self):
        """Function printing python version."""
        bip39 = Bip39()

        #correct sentances
        sentance_12c = 'pigeon pave board visual mixed monitor trophy couple hungry expand lawsuit next'
        sentance_15c = 'insane citizen junk trim violin dog damp audit license then ski donor dust similar decorate'
        sentance_18c = 'stamp crush area flag since index chalk wild cattle coffee december local polar sick agent execute brown author'
        sentance_21c = 'hole bonus chat essence ten wrestle other payment name old purpose decline again need twelve devote execute chief notice install syrup'
        sentance_24c = 'choice excess visual burger forum caution like sugar fan card use alone orient doll legal good exclude rebel fold boy tobacco solid fix foot'

        #incorrect sentances
        sentance_12i = 'zoo zoo board visual mixed monitor trophy couple hungry expand lawsuit next'
        sentance_15i = 'zoo citizen junk trim violin dog damp audit license then ski donor dust similar decorate'
        sentance_18i = 'zoo crush area flag since index chalk wild cattle coffee december local polar sick agent execute brown author'
        sentance_21i = 'zoo zoo chat essence ten wrestle other payment name old purpose decline again need twelve devote execute chief notice install syrup'
        sentance_24i = 'zoo excess visual burger forum caution like sugar fan card use alone orient doll legal good exclude rebel fold boy tobacco solid fix foot'

        self.assertEqual(True, bip39.is_valid_bip39_sentence(sentance_12c))
        self.assertEqual(True, bip39.is_valid_bip39_sentence(sentance_15c))
        self.assertEqual(True, bip39.is_valid_bip39_sentence(sentance_18c))
        self.assertEqual(True, bip39.is_valid_bip39_sentence(sentance_21c))
        self.assertEqual(True, bip39.is_valid_bip39_sentence(sentance_24c))

        print(bip39.is_valid_bip39_sentence(sentance_12i))
        print(bip39.is_valid_bip39_sentence(sentance_15i))
        print(bip39.is_valid_bip39_sentence(sentance_18i))
        print(bip39.is_valid_bip39_sentence(sentance_21i))
        print(bip39.is_valid_bip39_sentence(sentance_24i))

    def test_fix_bip39_checksum(self):
        """Function printing python version."""
        bip39 = Bip39()
        #incorrect sentances
        sentance_12i = 'zoo zoo board visual mixed monitor trophy couple hungry expand lawsuit next'
        sentance_15i = 'zoo citizen junk trim violin dog damp audit license then ski donor dust similar decorate'
        sentance_18i = 'zoo crush area flag since index chalk wild cattle coffee december local polar sick agent execute brown author'
        sentance_21i = 'zoo zoo chat essence ten wrestle other payment name old purpose decline again need twelve devote execute chief notice install syrup'
        sentance_24i = 'zoo excess visual burger forum caution like sugar fan card use alone orient doll legal good exclude rebel fold boy tobacco solid fix foot'

        #corrected sentances
        sentance_12c = 'zoo zoo board visual mixed monitor trophy couple hungry expand lawsuit news'
        sentance_15c = 'zoo citizen junk trim violin dog damp audit license then ski donor dust similar degree'
        sentance_18c = 'zoo crush area flag since index chalk wild cattle coffee december local polar sick agent execute brown ankle'
        sentance_21c = 'zoo zoo chat essence ten wrestle other payment name old purpose decline again need twelve devote execute chief notice install spike'
        sentance_24c = 'zoo excess visual burger forum caution like sugar fan card use alone orient doll legal good exclude rebel fold boy tobacco solid fix drop'

        self.assertEqual(bip39.fix_bip39_checksum(sentance_12i), sentance_12c)
        self.assertEqual(bip39.fix_bip39_checksum(sentance_15i), sentance_15c)
        self.assertEqual(bip39.fix_bip39_checksum(sentance_18i), sentance_18c)
        self.assertEqual(bip39.fix_bip39_checksum(sentance_21i), sentance_21c)
        self.assertEqual(bip39.fix_bip39_checksum(sentance_24i), sentance_24c)
    
    def test_get_bip39_word(self):
        """Function printing python version."""
        bip39 = Bip39()
        self.assertEqual(bip39.get_bip39_word(int(0)), 'abandon')
        self.assertEqual(bip39.get_bip39_word(int(1235)), 'omit')
        self.assertEqual(bip39.get_bip39_word(int(1710)), 'still')
        self.assertEqual(bip39.get_bip39_word(int(190)), 'blind')
        self.assertEqual(bip39.get_bip39_word(int(2047)), 'zoo')
    
    def test_get_bip39_word_value(self):
        """Function printing python version."""
        bip39 = Bip39()
        self.assertEqual(bip39.get_bip39_word_value('abandon'), int(0))
        self.assertEqual(bip39.get_bip39_word_value('omit'), int(1235))
        self.assertEqual(bip39.get_bip39_word_value('still'), int(1710))
        self.assertEqual(bip39.get_bip39_word_value('blind'), int(190))
        self.assertEqual(bip39.get_bip39_word_value('zoo'), int(2047))

    def test_get_supported_bip39_length(self):
        """Function printing python version."""
        bip39 = Bip39()
        target = []
        target.extend([12, 15, 18, 21, 24])
        self.assertListEqual(bip39.get_supported_bip39_length(), target)

    def test_binary_words_to_bip39_words(self):
        """Function printing python version."""
        bip39 = Bip39()
        bin_words = '00000000000111111111110000000000111111111110'
        expected_res = 'abandon zoo ability zone'
        self.assertEqual(bip39.binary_words_to_bip39_words(bin_words), expected_res)

    def test_dice_words_to_bip39_words(self):
        """Function printing python version."""
        bip39 = Bip39()
        # 222222 base 4 = 2730 base 10. 2730 % 2048 = 682
        # 111111 base 4 = 1365 base 10. 
        dice_words = '444444333333222222111111'
        expected_res = 'abandon zoo fetch primary'
        self.assertEqual(bip39.dice_words_to_bip39_words(dice_words), expected_res)

if __name__ == '__main__':
    unittest.main()
