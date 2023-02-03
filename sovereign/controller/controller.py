from os import system, name
import sys
import hashlib
import binascii
from prettytable import PrettyTable


from sovereign.model.model import Model
from sovereign.view.view import View

# Controller
def check_system_compatibility():
    # Exit if the version of Python is not Python3
    if(sys.version_info[0] != 3): 
        sys.exit('\nError. Using Python'+ str(sys.version_info[0]) +': This script uses 264 bit integers and requires Python 3. Integers in Python 3 are of unlimited size. Exited from the script.\n')
    # Exit if your machine is not little endian
    if(sys.byteorder != 'little'): 
        sys.exit('\nError. This machine is '+ str(sys.byteorder) +' endian. This software has only been tested on little endian machine.\n')

def binary_words_to_bip39_words(binary_words, wordlist):
    return [wordlist[int(binary_word, 2)] for binary_word in binary_words]
    #return [str(int(binary_word, 2)) for binary_word in binary_words]

def senary_words_to_bip39_words(senary_words, wordlist):
    return [wordlist[(int(senary_word, 6) & 0x07ff)] for senary_word in senary_words]
    #To check, the conversion is the same than %2048


def is_valid_bip39_sentence(ws, nums, wordlist, hash_method=hashlib.sha256):
    N = 0
    for w in ws:
        N = (N << 11) + nums[w]

    if len(ws) == 12:
        nhex = format(N, '033x')
        h = hash_method(binascii.unhexlify(nhex[:-1])).hexdigest()
        return h[0] == nhex[-1]
    elif len(ws) == 24:
        nhex = format(N, '066x')
        h = hash_method(binascii.unhexlify(nhex[:-2])).hexdigest()
        return h[1] == nhex[-1] and h[0] == nhex[-2]
    else:
        raise ValueError("Invalid number of words")

def fix_bip39_checksum(words, nums, wordlist):
    cand = []
    if len(words) == 24 or len(words) == 12:
        org_words = words
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
    Nxored = int(0)
    sentanceR = []

    for sentance in bip39_sentances:
        N = 0
        for w in sentance:
            N = (N<<11) + nums[w]
        Nxored = Nxored ^ N
    
    for x in range(0, len(sentance)):
        j = Nxored & 0x07ff
        Nxored = Nxored >> 11 
        sentanceR.insert(0, wordlist[j])

    for i in range(2048):
        cand = sentanceR[:-1] + [wordlist[i]]
        if is_valid_bip39_sentence(cand, nums, wordlist):
            print("xor result BIP39 sentance is valid")
            return(cand)

class Controller:
    def __init__(self):
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
        if(self.model.get_mode() == int(24)):
            self.model.set_mode(int(12))
        else:
            self.model.set_mode(int(24))
    
    def option1(self):
        self.view.clear()
        print("You selected Option 1")

        words=[]
        base = 2
        group_count = self.model.get_mode() # 12 or 24
        group_size = 11

        while len(words) < group_count:
            user_input= self.view.gather_group_input(base, group_size)
            if user_input == 'q':
                return
            if user_input is not None:
                words.append(user_input)
            else:
                print("Error: invalid user_input")
            self.view.display_base2_groups(words, group_count, self.model.wordlist)
        
        print("Fixing the BIP39 sentance with a valid checksum")
        print("The BIP39 sentance below is valid (the checksum is correct)")
       
        bip39_words = binary_words_to_bip39_words(words, self.model.wordlist)
        valid_bip39_sentance = fix_bip39_checksum(bip39_words, self.model.nums,self.model.wordlist)
        self.view.display_bip39_sentance(valid_bip39_sentance, self.model.nums)
 
    def option2(self):
        print("You selected Option 2")
        words=[]
        base = 6
        group_count = self.model.get_mode()
        group_size = 5

        while len(words) < group_count:
            user_input= self.view.gather_group_input(base, group_size)
            if user_input == 'q':
                return 'q'
            elif user_input is not None:
                words.append(user_input)
            else:
                print("Error: invalid user_input")
            self.view.display_base6_groups(words, group_count, self.model.wordlist)

        print("Fixing the BIP39 sentance...")
        print("The BIP39 sentance below is valid (the checksum is correct)")
        bip39_words = senary_words_to_bip39_words(words, self.model.wordlist)
        valid_bip39_sentance = fix_bip39_checksum(bip39_words, self.model.nums, self.model.wordlist)
        self.view.display_bip39_sentance(valid_bip39_sentance, self.model.nums)
  
    def option3(self):
        print("You selected Option 3")
        words=[]
        group_count = self.model.get_mode() # 12 or 24

        while len(words) < group_count:
            word = self.view.gather_bip39_word_input(self.model.nums)
            if word == 'q':
                return
            elif word is not None :
                words.append(word)
            else:
                print("Error: invalid BIP39 word")
            self.view.clear()
            self.view.display_bip39_sentance(words, self.model.nums)

        print(words)
        if is_valid_bip39_sentence(words, self.model.nums, self.model.wordlist):
            print("The entered BIP39 sentance above is valid (checksum is correct)")
        else:
            print("The entered BIP39 sentance above is invalid (checksum is incorrect)")
            print("Fixing the BIP39 sentance...")
            print("The BIP39 sentance below is valid (the checksum is correct)")
            valide_bip39_sentance = fix_bip39_checksum(words, self.model.nums, self.model.wordlist)
            self.view.display_bip39_sentance(valide_BIP39_sentance, self.model.nums)

    def option4(self):
        print("You selected Option 4")
        words=[]
        group_count = self.model.get_mode() # 12 or 24

        while len(words) < group_count:
            word = self.view.gather_BIP39_word_input(self.model.nums) 
            if word == 'q':
                return 'q'
            if word is not None :
                words.append(word)
            else:
                print("Error: invalid BIP39 word")
            self.view.clear()
            self.view.display_BIP39_sentance(words, self.model.nums)

        print("Checking BIP39 sentance")
        if is_valid_bip39_sentence(words, self.model.nums, self.model.wordlist, hash_method=hashlib.sha256):
            print("The BIP39 sentance below is valid")
            self.model.add_bip39_sentance(words)
            self.view.display_bip39_sentance(words, self.model.nums)
        else:
            print("The entered BIP39 is not valid")
 
    def option5(self):
        print("You selected Option 5")
        sentances = self.model.get_bip39_sentances()
        print("Number of BIP39 sentances: " + str(len(sentances)))
        for count, sentance in enumerate (sentances):
            self.view.display_bip39_sentance(sentance, self.model.nums, "BIP39 sentance #" + str(count+1))

    def option6(self):
        print("You selected Option 6")
        #!!! before, we need to check that there are at least 2 BIP39_entances
        bip39_sentance = bip39_sentances_xor(self.model.bip39_sentances, self.model.wordlist, self.model.nums)
        print(bip39_sentance)
        self.view.display_bip39_sentance(bip39_sentance, self.model.nums, "BIP39 XORED sentance")
    
    def option20(self):
        print("You selected Option 20")
        #self.bip39Sentances
        self.model.load_3_12w_bip39_sentances()

    def option21(self):
        print("You selected Option 21")
        self.model.load_3_24w_bip39_sentances()

    def exit_program(self):
        self.view.clear()
        quit()
        print("Exiting...")
