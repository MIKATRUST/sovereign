#!/usr/bin/env python3

'''MVC/Model'''

import os
import hashlib

def check_file_hash(filename, expected_hash, hash_method = hashlib.sha256):
    """Calculate the hash of a file and compare it to the expected value.

    Args:
        filename (str): The path to the file to check.
        expected_hash (str): The expected hash value, encoded as a hexadecimal string.

    Returns:
        bool: True if the calculated hash matches the expected value, False otherwise.
    """
    with open(filename, 'rb') as file:
        content = file.read()
        calculated_hash = hash_method(content).hexdigest()
        return calculated_hash == expected_hash

class Model():
    """Class for the Model component of the MVC architecture.

    Attributes:
        bip39_sentances (list): List of BIP39 sentences.
        mode (int): Mode of the model.
        wordlist (list): List of words from the BIP39 wordlist.
        nums (dict): Dictionary mapping words to numbers.
    """

    def __init__(self, file_path = './sovereign/model/english.txt'):
        """Initialize the model.

        Loads the BIP39 wordlist from the english.txt file and sets up the wordlist and nums attributes.
        """
        if __debug__:
            print("Model constructor Dir:", os.getcwd())

        self.bip39_sentances = []
        self.mode = 24
        self.wordlist = []
        self.nums = {}
        expected_hash = '2f5eed53a4727b4bf8880d8f3f199efc90e58503646d9ff8eff3a2ed3b24dbda'

        # check_file_hash(file_path, expected_hash)

        with open(file_path, encoding="utf-8") as fin:
            for i, word in enumerate(fin):
                self.nums[word.strip()] = i
                self.wordlist.append(word.strip())

        if len(self.wordlist) != 2048:
            raise ValueError(
                f"Error: {len(self.wordlist)} The dictionary file does not contain 2048 words.")

        if not check_file_hash(file_path, expected_hash):
            raise ValueError(
                f"Error: The signature hash for the dictionary file is incorrect, not as expected: {expected_hash}")
    
    def add_bip39_sentance(self, sentance: str):
        """Add a BIP39 sentence to the model.

        Args:
            sentance (str): BIP39 sentence to add.
        """
        self.bip39_sentances.append(sentance)

    def get_bip39_sentances(self):
        """Get the BIP39 sentences in the model.

        Returns:
            list: List of BIP39 sentences.
        """
        return self.bip39_sentances

    def set_mode(self, mode: int):
        """Set the mode of the model.

        Args:
            mode (int): Mode to set.
        """
        self.mode = int(mode)

    def get_mode(self):
        """Get the mode of the model.

        Returns:
            int: Current mode of the model.
        """
        return self.mode

    def load_3_12w_bip39_sentances(self):
        """Function printing python version."""
        self.mode = int(12)
        self.bip39_sentances.append('zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo abstract')
        self.bip39_sentances.append('zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo wrong')  
        self.bip39_sentances.append('abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about')

        if __debug__:
            print("Loaded load_3_12w_bip39_sentances")

    def load_3_24w_bip39_sentances(self):
        """Function printing python version."""
        self.mode = int(24)
        self.bip39_sentances.append('zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo vote')
        self.bip39_sentances.append('zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo buddy')
        self.bip39_sentances.append('abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon art')

        if __debug__:
            print("Loaded load_3_24w_bip39_sentances")
