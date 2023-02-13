#!/usr/bin/env python3

'''Demonstrates triple double quotes
docstrings and does nothing really.'''

import unittest
from ..bip39.bip39 import Bip39

'''Demonstrates triple double quotes
docstrings and does nothing really.'''


class TestBip39(unittest.TestCase):

    
    def test_get_word(self):
        """Function printing python version."""
        bip39 = Bip39()
        fun = bip39.get_word

        self.assertEqual(fun(int(0)), 'abandon')
        self.assertEqual(fun(int(1235)), 'omit')
        self.assertEqual(fun(int(1710)), 'still')
        self.assertEqual(fun(int(190)), 'blind')
        self.assertEqual(fun(int(2047)), 'zoo')
    
    def test_word_index(self):
        """Function printing python version."""
        bip39 = Bip39()
        fun = bip39.get_word_index

        self.assertEqual(fun('abandon'), int(0))
        self.assertEqual(fun('omit'), int(1235))
        self.assertEqual(fun('still'), int(1710))
        self.assertEqual(fun('blind'), int(190))
        self.assertEqual(fun('zoo'), int(2047))

    def test_is_valid_words(self):
        """Function printing python version."""
        bip39 = Bip39()
        fun = bip39.is_valid_words

        self.assertEqual(True, fun('zoo zoo zoo'))
        self.assertEqual(False, fun('zoo zooo zoo'))
        self.assertEqual(False, fun('zooo zooo zoo'))
        self.assertEqual(False, fun('zoo zooo zooo'))
        self.assertEqual(True, fun('abandon abandon abandon'))
        self.assertEqual(False, fun('aaaabandon abandon abandon'))
        self.assertEqual(False, fun('abandon aaaabandon abandon'))
        self.assertEqual(False, fun('abandon abandon aaaabandon'))

    def test_get_supported_mnem_lengths(self):
        """Get a list of supported mnemonic lengths."""
        bip39 = Bip39()
        fun = bip39.get_supported_mnem_lengths

        target = []
        target.extend([12, 15, 18, 21, 24])
        self.assertListEqual(fun(), target)    

    def is_supported_mnem_length(self):
        """Function printing python version."""
        bip39 = Bip39()
        fun = bip39.is_supported_mnem_length

        #correct sentances
        sentance_12c = 'pigeon pave board visual mixed monitor trophy couple hungry expand lawsuit next'
        sentance_15c = 'insane citizen junk trim violin dog damp audit license then ski donor dust similar decorate'
        sentance_18c = 'stamp crush area flag since index chalk wild cattle coffee december local polar sick agent execute brown author'
        sentance_21c = 'hole bonus chat essence ten wrestle other payment name old purpose decline again need twelve devote execute chief notice install syrup'
        sentance_24c = 'choice excess visual burger forum caution like sugar fan card use alone orient doll legal good exclude rebel fold boy tobacco solid fix foot'

        self.assertEqual(True, fun(sentance_12c))
        self.assertEqual(True, fun(sentance_15c))
        self.assertEqual(True, fun(sentance_18c))
        self.assertEqual(True, fun(sentance_21c))
        self.assertEqual(True, fun(sentance_24c))
        self.assertEqual(False, fun(''))
        self.assertEqual(False, fun('zoo'))
        self.assertEqual(False, fun('zoo zoo'))
        self.assertEqual(False, fun('zoo zoo zoo'))
        self.assertEqual(False, fun('1 2 3 4 5 6 7 8 9 10 11 12 13'))

    def test_binary_words_to_bip39_phrase(self):
        """Function printing python version."""
        bip39 = Bip39()
        fun = bip39.binary_words_to_bip39_phrase

        # 00000000000 = 0 base 10.
        # 11111111111 = 2047 base 10.
        # 00000000001 = 1 base 10. 
        # 11111111110 = 2046 base 10.

        bin_words = '00000000000111111111110000000000111111111110'
        expected_res = 'abandon zoo ability zone'
        self.assertEqual(fun(bin_words), expected_res)

    def test_dice_to_bip39_phrase(self):
        """Function printing python version."""
        bip39 = Bip39()
        fun = bip39.dice_to_bip39_phrase
        
        # 444444 base 4 = 0 base 10.
        # 333333 base 4 = 2047 base 10.
        # 222222 base 4 = 2730 base 10. 2730 % 2048 = 682
        # 111111 base 4 = 1365 base 10.

        dice_words = '444444333333222222111111'
        expected_res = 'abandon zoo fetch primary'
        self.assertEqual(fun(dice_words), expected_res)

    def test_is_valid_bip39_sentence(self):
        """Function printing python version."""
        bip39 = Bip39()
        fun = bip39.is_valid_bip39_sentence

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

        self.assertEqual(True, fun(sentance_12c))
        self.assertEqual(True, fun(sentance_15c))
        self.assertEqual(True, fun(sentance_18c))
        self.assertEqual(True, fun(sentance_21c))
        self.assertEqual(True, fun(sentance_24c))

        print(fun(sentance_12i))
        print(fun(sentance_15i))
        print(fun(sentance_18i))
        print(fun(sentance_21i))
        print(fun(sentance_24i))

    def test_fix_bip39_checksum(self):
        """Function printing python version."""
        bip39 = Bip39()
        fun = bip39.fix_bip39_checksum

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

        self.assertEqual(fun(sentance_12i), sentance_12c)
        self.assertEqual(fun(sentance_15i), sentance_15c)
        self.assertEqual(fun(sentance_18i), sentance_18c)
        self.assertEqual(fun(sentance_21i), sentance_21c)
        self.assertEqual(fun(sentance_24i), sentance_24c)
    


 

if __name__ == '__main__':
    unittest.main()
