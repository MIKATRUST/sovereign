
'''MVC/Controller'''

import sys
import hashlib
import binascii

import pdb

from sovereign.model.model import Model
from sovereign.view.view import View
from sovereign.bip39.bip39 import Bip39

def check_system_compatibility():
    """Function printing python version."""
    print("To be implemented")

# Mnemonic to Seed
# test vector, see : https://bitcoin.stackexchange.com/questions/85293/how-to-use-bip39-test-vectors

class Controller:
    '''Demonstrates triple double quotes
    docstrings and does nothing really.'''

    def __init__(self):
        """Function printing python version."""
        if __debug__:
            print("Controller constructor ")
        check_system_compatibility()

        self.model = Model()
        self.view = View()
        self.bip39 = Bip39()

        self.options = {
            "0": self.option0,
            "1": self.option1,
            "2": self.option2,
            "3": self.option3,
            "4": self.option4,
            "5": self.option5,
            "6": self.option6,
            "7": self.exit_program,
            "20": self.option20,
            "21": self.option21,
        }

    def bip39_sentances_xor(self, bip39_sentances):
        """Function printing python version."""
        sentance_xored = int(0)
        bip39_sentance_xored = ""
        bin_bip39_sentance_length = self.model.get_mode()*11

        #compute xored BIP39 sentances value
        for sentance in bip39_sentances:
            int_sentance = int(0)    
            for word in sentance.split():
                int_sentance = (int_sentance << 11) + self.bip39.get_word_index(word)
            bin_sentance = format(int_sentance, 'b').zfill(bin_bip39_sentance_length)
            sentance_xored = sentance_xored ^ int(bin_sentance,2)
            bin_sentance_xored = bin(sentance_xored)[2:].zfill(bin_bip39_sentance_length)

        #Contruct BIP39 sentance from bip39 xored binary
        for i in range (self.model.get_mode()):
            bin_word = bin_sentance_xored[i*11:(i+1)*11]
            bip39_sentance_xored = bip39_sentance_xored + self.bip39.get_word(int(bin_word,2)) + " "

        return(self.bip39.fix_bip39_checksum(bip39_sentance_xored))
            

    def option0(self):
        """Change BIP39 sentance length"""
        self.view.clear()
        #print(f"Supported BIP39 modes are {self.bip39.get_supported_bip39_length()} words")
        user_input = self.view.gather_mode(self.bip39.get_supported_mnem_lengths())
        #self.view.gather_mode()
        self.model.set_mode(user_input)
        self.view.clear()

    def option1(self):
        """Create BIP39 sentance from flipping a coin."""
        self.view.clear()
        print("You selected Option 1")

        words = ""
        base = 2
        group_size = 11

        while len(words) < (self.model.get_mode() * group_size):
            user_input = self.view.gather_group_input(base, group_size)
            if user_input == 'q':
                return
            if user_input is not None:
                words = words + user_input
            else:
                print("Error: invalid user_input")

            bip39_words = self.bip39.binary_words_to_bip39_phrase(words)

            self.view.display_base2_groups(bip39_words, self.bip39.get_word_index)

        print("Fixing the BIP39 sentance with a valid checksum")
        print("The BIP39 sentance below is valid (the checksum is correct)")

        bip39_sentance = self.bip39.binary_words_to_bip39_phrase(words)
        fixed_bip39_sentance = self.bip39.fix_bip39_checksum(bip39_sentance)
        self.view.display_bip39_sentance(fixed_bip39_sentance, self.bip39.get_word_index)

    def option2(self):
        """Create BIP39 sentance from rolling a dice."""
        print("You selected Option 2")
        words = ""

        while len(words) < self.model.get_mode() * 6 :
            user_input = self.view.gather_6s_dice_input()
            if user_input == 'q':
                return 'q'
            elif user_input is not None:
                words = words + user_input
            else:
                print("Error: invalid user_input")

            #convert from base4 words to binary_words
            bip39_sentance = self.bip39.dice_to_bip39_phrase(words)
            self.view.display_6s_dice_groups(bip39_sentance, self.bip39.get_word_index)


        print("Fixing the BIP39 sentance...")
        print("The BIP39 sentance below is valid (the checksum is correct)")

        fixed_bip39_sentance = self.bip39.fix_bip39_checksum(bip39_sentance)
        self.view.display_bip39_sentance(fixed_bip39_sentance, self.bip39.get_word_index)

    def option3(self):
        """Create BIP39 sentance from BIP39 word random selection."""
        print("You selected Option 3")
        words = ""

        while len(words.split()) < self.model.get_mode():
            word = self.view.gather_bip39_word_input(self.bip39.is_valid_words)
            if word == 'q':
                return
            elif word is not None:
                #words.append(word)
                words = words + ' ' + word
            else:
                print("Error: invalid BIP39 word")
            self.view.clear()
            self.view.display_bip39_sentance(words, self.bip39.get_word_index)

        if self.bip39.is_valid_bip39_sentence(words):
            print("The entered BIP39 sentance above is valid (checksum is correct)")
        else:
            print("The entered BIP39 sentance above is invalid (checksum is incorrect)")
            print("Fixing the BIP39 sentance...")
            print("The BIP39 sentance below is valid (the checksum is correct)")
            valide_bip39_sentance = self.bip39.fix_bip39_checksum(words)
            self.view.display_bip39_sentance(valide_bip39_sentance, self.bip39.get_word_index)

    def option4(self):
        """Load a BIP39 sentance."""
        print("You selected Option 4")
        words = ""
        group_count = self.model.get_mode()

        while len(words.split()) < group_count:
            word = self.view.gather_bip39_word_input(self.bip39.get_word_index)
            if word == 'q':
                return 'q'
            if word is not None:
                words = words + ' ' + word
            else:
                print("Error: invalid BIP39 word")
            self.view.clear()
            self.view.display_bip39_sentance(words, self.bip39.get_word_index)

        print("Checking BIP39 sentance")
        if self.bip39.is_valid_bip39_sentence(words):
            print("The BIP39 sentance below is valid")
            self.model.add_bip39_sentance(words)
            self.view.display_bip39_sentance(words, self.bip39.get_word_index)
        else:
            print("The entered BIP39 is not valid")

    def option5(self):
        """Show loaded BIP39 sentance(s)"""
        print("You selected Option 5")
        sentances = self.model.get_bip39_sentances()
        print("Number of BIP39 sentances: " + str(len(sentances)))
        for count, sentance in enumerate(sentances):
            self.view.display_bip39_sentance(sentance, self.bip39.get_word_index, "BIP39 sentance #" + str(count + 1))

    def option6(self):
        """Compute xor of loaded BIP39 sentances."""
        print("You selected Option 6")
        #!!! before, we need to check that there are at least 2 BIP39 sentances
        bip39_sentance = self.bip39_sentances_xor(
            self.model.bip39_sentances)
        self.view.display_bip39_sentance(
            bip39_sentance, self.bip39.get_word_index, "BIP39 XORED sentance")

    def option20(self):
        """Load 3 12 words BIP39 sentances."""
        print("You selected Option 20")
        # self.bip39Sentances
        self.model.load_3_12w_bip39_sentances()

    def option21(self):
        """Load 3 24 words BIP39 sentances.."""
        print("You selected Option 21")
        self.model.load_3_24w_bip39_sentances()

    def exit_program(self):
        """Quit."""
        quit()        
        sys.exit("Exiting...")

