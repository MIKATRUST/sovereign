
'''MVC/Controller'''

import sys
import hashlib
import binascii

#For pbkdf2
#import hashlib
import hmac
import os # unused ?

from sovereign.model.model import Model
from sovereign.view.view import View

def check_system_compatibility():
    """Function printing python version."""
    # Exit if the version of Python is not Python3
    if sys.version_info[0] != 3:
        sys.exit('\nError. Using Python' +
                 str(sys.version_info[0]) +
                 ': This script uses 264 bit integers and requires Python 3. Integers in Python 3 are of unlimited size. Exited from the script.\n')
    # Exit if your machine is not little endian
    if sys.byteorder != 'little':
        sys.exit('\nError. This machine is ' + str(sys.byteorder) +
                 ' endian. This software has only been tested on little endian machine.\n')

def binary_words_to_bip39_words(binary_words, wordlist):
    """Function printing python version."""
    return [wordlist[int(binary_word, 2)] for binary_word in binary_words]
    # return [str(int(binary_word, 2)) for binary_word in binary_words]

def senary_words_to_bip39_words(senary_words, wordlist):
    """Function printing python version."""
    return [wordlist[(int(senary_word, 6) & 0x07ff)]
            for senary_word in senary_words]
    # To check, the conversion is the same than %2048

def is_valid_bip39_sentence(bip39_sentance, nums, wordlist, hash_method=hashlib.sha256):
    """Function printing python version."""
    entropy = 0
    for word in bip39_sentance:
        entropy = (entropy << 11) + nums[word]

    if len(bip39_sentance) == 12:
        nhex = format(entropy, '033x')
        hash_result = hash_method(binascii.unhexlify(nhex[:-1])).hexdigest()
        return hash_result[0] == nhex[-1]
    elif len(bip39_sentance) == 24:
        nhex = format(entropy, '066x')
        hash_result = hash_method(binascii.unhexlify(nhex[:-2])).hexdigest()
        return hash_result[1] == nhex[-1] and hash_result[0] == nhex[-2]
    else:
        raise ValueError("Invalid number of words")

def fix_bip39_checksum(words, nums, wordlist):
    """Function printing python version."""
    cand = []
    if len(words) == 24 or len(words) == 12:
        # org_words = words
        for i in range(2048):
            cand = words[:-1] + [wordlist[i]]
            if is_valid_bip39_sentence(cand, nums, wordlist):
                return cand
    else:
        raise ValueError("Invalid number of words")

# Compute xor of several Bip39 sentances
# Return the xored sentance under the form of an integer
#
# !! before combining, we should check the checksum for each entance and trigger exception if needed
#

def bip39_sentances_xor(bip39_sentances, wordlist, nums):
    """Function printing python version."""
    Nxored = int(0)
    sentance_part = []

    for sentance in bip39_sentances:
        N = 0
        for word in sentance:
            N = (N << 11) + nums[word]
        Nxored = Nxored ^ N

    for _ in range(0, len(sentance)):
        j = Nxored & 0x07ff
        Nxored = Nxored >> 11
        sentance_part.insert(0, wordlist[j])

    for i in range(2048):
        cand = sentance_part[:-1] + [wordlist[i]]
        if is_valid_bip39_sentence(cand, nums, wordlist):
            print("xor result BIP39 sentance is valid")
            return cand


# Mnemonic to Seed
# test vector, see : https://bitcoin.stackexchange.com/questions/85293/how-to-use-bip39-test-vectors
def pbkdf2(password, salt, iterations, dklen, digest):
    """Implements the PBKDF2 key derivation function.

    Args:
        password (bytes): The password to derive the key from.
        salt (bytes): The salt to use in the key derivation.
        iterations (int): The number of iterations to perform.
        dklen (int): The length of the derived key in bytes.
        digest (callable): The hash function to use, e.g. hashlib.sha256.

    Returns:
        bytes: The derived key.
    """
    if dklen > (2**32 - 1) * digest().block_size:
        raise ValueError("Requested key length too long")

    password = password.encode("utf-8")
    salt = salt.encode("utf-8")
    
    h = hmac.new(password, None, digest)

    def xor(a, b):
        return bytes(x ^ y for x, y in zip(a, b))

    def prf(h, data):
        hm = h.copy()
        hm.update(data)
        return hm.digest()

    dkey = b''
    block = 0
    while len(dkey) < dklen:
        block += 1
        U = prf(h, salt + block.to_bytes(4, "big"))
        T = U
        for _ in range(iterations - 1):
            U = prf(h, U)
            T = xor(T, U)
        dkey += T
    return dkey[:dklen]


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

    def option0(self):
        """Change mode 12 or 24 BIP39 sentance."""
        self.view.clear()
        if self.model.get_mode() == int(24):
            self.model.set_mode(int(12))
        else:
            self.model.set_mode(int(24))

    def option1(self):
        """Create BIP39 sentance from flipping a coin."""
        self.view.clear()
        print("You selected Option 1")

        words = []
        base = 2
        group_count = self.model.get_mode()  # 12 or 24
        group_size = 11

        while len(words) < group_count:
            user_input = self.view.gather_group_input(base, group_size)
            if user_input == 'q':
                return
            if user_input is not None:
                words.append(user_input)
            else:
                print("Error: invalid user_input")
            self.view.display_base2_groups(
                words, group_count, self.model.wordlist)

        print("Fixing the BIP39 sentance with a valid checksum")
        print("The BIP39 sentance below is valid (the checksum is correct)")

        bip39_words = binary_words_to_bip39_words(words, self.model.wordlist)
        valid_bip39_sentance = fix_bip39_checksum(
            bip39_words, self.model.nums, self.model.wordlist)
        self.view.display_bip39_sentance(valid_bip39_sentance, self.model.nums)

    def option2(self):
        """CCreate BIP39 sentance from rolling a dice."""
        print("You selected Option 2")
        words = []
        base = 6
        group_count = self.model.get_mode()
        group_size = 5

        while len(words) < group_count:
            user_input = self.view.gather_group_input(base, group_size)
            if user_input == 'q':
                return 'q'
            elif user_input is not None:
                words.append(user_input)
            else:
                print("Error: invalid user_input")
            self.view.display_base6_groups(
                words, group_count, self.model.wordlist)

        print("Fixing the BIP39 sentance...")
        print("The BIP39 sentance below is valid (the checksum is correct)")
        bip39_words = senary_words_to_bip39_words(words, self.model.wordlist)
        valid_bip39_sentance = fix_bip39_checksum(
            bip39_words, self.model.nums, self.model.wordlist)
        self.view.display_bip39_sentance(valid_bip39_sentance, self.model.nums)

    def option3(self):
        """Create BIP39 sentance from BIP39 word random selection."""
        print("You selected Option 3")
        words = []
        group_count = self.model.get_mode()  # 12 or 24

        while len(words) < group_count:
            word = self.view.gather_bip39_word_input(self.model.nums)
            if word == 'q':
                return
            elif word is not None:
                words.append(word)
            else:
                print("Error: invalid BIP39 word")
            self.view.clear()
            self.view.display_bip39_sentance(words, self.model.nums)

        print(words)
        if is_valid_bip39_sentence(
                words,
                self.model.nums,
                self.model.wordlist):
            print("The entered BIP39 sentance above is valid (checksum is correct)")
        else:
            print("The entered BIP39 sentance above is invalid (checksum is incorrect)")
            print("Fixing the BIP39 sentance...")
            print("The BIP39 sentance below is valid (the checksum is correct)")
            valide_bip39_sentance = fix_bip39_checksum(
                words, self.model.nums, self.model.wordlist)
            self.view.display_bip39_sentance(
                valide_bip39_sentance, self.model.nums)

    def option4(self):
        """Load a BIP39 sentance."""
        print("You selected Option 4")
        words = []
        group_count = self.model.get_mode()  # 12 or 24

        while len(words) < group_count:
            word = self.view.gather_bip39_word_input(self.model.nums)
            if word == 'q':
                return 'q'
            if word is not None:
                words.append(word)
            else:
                print("Error: invalid BIP39 word")
            self.view.clear()
            self.view.display_bip39_sentance(words, self.model.nums)

        print("Checking BIP39 sentance")
        if is_valid_bip39_sentence(
                words,
                self.model.nums,
                self.model.wordlist,
                hash_method=hashlib.sha256):
            print("The BIP39 sentance below is valid")
            self.model.add_bip39_sentance(words)
            self.view.display_bip39_sentance(words, self.model.nums)
        else:
            print("The entered BIP39 is not valid")

    def option5(self):
        """Show loaded BIP39 sentance(s)"""
        print("You selected Option 5")
        sentances = self.model.get_bip39_sentances()
        print("Number of BIP39 sentances: " + str(len(sentances)))
        for count, sentance in enumerate(sentances):
            self.view.display_bip39_sentance(
                sentance, self.model.nums, "BIP39 sentance #" + str(count + 1))

    def option6(self):
        """Compute xor of loaded BIP39 sentances."""
        print("You selected Option 6")
        #!!! before, we need to check that there are at least 2 BIP39_entances
        bip39_sentance = bip39_sentances_xor(
            self.model.bip39_sentances,
            self.model.wordlist,
            self.model.nums)
        print(bip39_sentance)
        self.view.display_bip39_sentance(
            bip39_sentance, self.model.nums, "BIP39 XORED sentance")

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

