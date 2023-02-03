
from os import system, name
import os
import sys
import hashlib
import binascii
from prettytable import PrettyTable

# Model

class Model:
    def __init__(self):
        print("CONSTRUCTOR MODEL")
        print(os.getcwd())
        print("yep")
        self.bip39_sentances = []
        self.mode = int(24)
        # Initialize a list to store the BIP39 words
        self.wordlist = []
        # Initialize a dictionary to store the word-to-number mapping
        self.nums = {}
        # Load word list
        with open('./sovereign/model/english.txt') as fin:
            i = 0
            for word in fin:
                self.nums[word.strip()] = i
                self.wordlist.append(word.strip())
                i = i + 1
        if(len(self.wordlist) != 2048): 
            sys.exit('\nError. '+ str(len(self.wordlist)) +' words loaded, should have been 2048. Exited from the script.\n')

    def add_bip39_sentance(self, sentance):
        print(len(self.bip39_sentances))
        self.bip39_sentances.append(sentance)
        print(self.bip39_sentances)
    
    def get_bip39_sentances(self):
        return self.bip39_sentances

    def load_3_12w_bip39_sentances(self):
        self.mode = int(12)
        self.bip39_sentances.append(['zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','wrong'])
        self.bip39_sentances.append(['zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','abstract'])
        self.bip39_sentances.append(['abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'surface'])
        print("loaded load_3_12w_bip39_sentances")
    
    def load_3_24w_bip39_sentances(self):
        self.mode = int(24)
        self.bip39_sentances.append(['zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','vote'])
        self.bip39_sentances.append(['zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo', 'vote'])
        self.bip39_sentances.append(['abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon','abandon','street'])
        print("loaded load_3_24w_bip39_sentances")

    def set_mode(self, mode):
        self.mode = int(mode)

    def get_mode(self):
        return int(self.mode)

