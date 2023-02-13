#!/usr/bin/env python3

'''BIP39'''

import hashlib

class Bip39():
    """BIP39 implementation
       English only 

    Attributes:
        supported_bip39_length (int): supported BIP39 word length.
        wordlist (list): List of words from the BIP39 wordlist.
        nums (dict): Dictionary mapping words to numbers.
    """

    def __init__(self, file_path = './sovereign/model/english.txt'):
        """Initialize the model.
        Loads the BIP39 wordlist from the english.txt file and sets up the wordlist and nums attributes.
        """
        if __debug__:
            print("Bip39 constructor ")

        self.supported_bip39_length = [12, 15, 18, 21, 24]
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

    #    if not check_file_hash(file_path, expected_hash):
    #        raise ValueError(
    #            f"Error: The signature hash for the dictionary file is incorrect, not as expected: {expected_hash}")
    
    def binary_words_to_bip39_words(self, words):
        """Convert a binary sequence of words into a BIP39 sentance."""
        sentance = ""
        for i in range (int(len(words)/11)):
            bin_word = words[i*11:(i+1)*11]
            sentance = sentance + self.get_bip39_word(int(bin_word,2)) + " "
        return sentance[:-1]

    def dice_words_to_bip39_words(self, dice_words):
        """Convert a dice sequence of words [1-4] into a BIP39 sentance."""
        sentance = ""
        for i in range (int(len(dice_words)/6)):
            dice_word = dice_words[i*6:(i+1)*6]
            #transform word dice base to base 4  
            dice_word = dice_word.replace('4', '0')
            #pdb.set_trace()
            #6 dice rolls (12 bits), maximum value = 4095, need to get back to 11 bits
            sentance = sentance + self.get_bip39_word(int(dice_word,4) % 2048) + " "
            #pdb.set_trace()
        return sentance[:-1]

    def is_valid_bip39_words(self, sentance):
        """Check if all words of a BIP39 sequence are valid."""
        return not any(word not in self.nums for word in sentance.split())

    def is_valid_bip39_length(self, sentance):
        """Check if a BIP sentance has valid length."""
        if len(sentance.split()) in self.supported_bip39_length: return True
        else: return False

    def is_valid_bip39_sentence(self, bip39_sentance, hash_method=hashlib.sha256):
        """Return true if the BIP39 sentance is valid,i.e. the checksum is valid."""
        
        #BIP39 sentance has between 12 and 24 words
        #Each BIP39 word is encoded with 11 bits
        #For every set of 33 bits in the BIP39 sentence, 1 bit serves as a checksum.

        #Get the word count of the BIP39 sentance  
        word_count = len(bip39_sentance.split())

        #Compute BIP39 sentance integer value
        int_sentance = int(0)
        for word in bip39_sentance.split():
            int_sentance = (int_sentance << 11) + self.nums[word]
        
        #Compute BIP39 sentance binary value
        bin_sentance = bin(int_sentance)[2:].zfill(11 * word_count)

        #Get bin data part and binary checksum part
        bin_data = bin_sentance[: int(32 * 11 * word_count / 33)]
        bin_checksum = bin_sentance[-int((11 * word_count) / 33):]

        #Compute checksum
        bytes_data = int(bin_data, 2).to_bytes(int(32 * 11 * word_count / 33 / 8), byteorder="big")
        bin_computed_checksum = bin(int(hash_method(bytes_data).hexdigest(), 16))[2:].zfill(256)[: int(11 * word_count / 33)]
        
        return bin_computed_checksum == bin_checksum

    def fix_bip39_checksum(self, bip39_sentance, hash_method=hashlib.sha256):
        """Fix the BIP39 checksum and return a new BIP39 sentance (last word modified)"""
        #BIP39 sentance has between 12 and 24 words
        #Each BIP39 word is encoded with 11 bits
        #For every set of 33 bits in the BIP39 sentence, 1 bit serves as a checksum.

        #Get the word count of the BIP39 sentance  
        word_count = len(bip39_sentance.split())

        #Compute BIP39 sentance integer value
        int_sentance = int(0)
        for word in bip39_sentance.split():
            int_sentance = (int_sentance << 11) + self.nums[word]
        
        #Compute BIP39 sentance binary value
        bin_sentance = bin(int_sentance)[2:].zfill(11 * word_count)

        #Get bin data part and binary checksum part
        bin_data = bin_sentance[: int(32 * 11 * word_count / 33)]
        bin_checksum = bin_sentance[-int((11 * word_count) / 33) :] #Not used

        #Get data part, convert to bytes
        bytes_data = int(bin_data, 2).to_bytes(int(32 * 11 * word_count / 33 / 8), byteorder="big")

        #Compute checksum
        bin_computed_checksum = bin(int(hash_method(bytes_data).hexdigest(), 16))[2:].zfill(256)[: int(11 * word_count / 33)]
        last_word_bin = bin_data[-(11-len(bin_computed_checksum)):]+bin_computed_checksum
        
        #compute last word integer value
        last_word_int = int(last_word_bin,2)
        
        #get corresponding BIP39 word
        last_word = self.wordlist[last_word_int]
        
        #construct BIP39 sentance
        bip39_sentance_except_last_word = bip39_sentance.split()[:len(bip39_sentance.split())-1]
        #return fixed bip39_sentance
        return (" ".join(bip39_sentance_except_last_word) + " " + last_word)

    def get_bip39_word(self, int_value):
        """Get the BIP39 word from the integer value."""
        return self.wordlist[int_value]

    def get_bip39_word_value(self, word):
        """Get the integer value for the given BIP39 word."""
        return self.nums[word]

    def get_supported_bip39_length(self):
        """Get the supported modes, i.e BIP39 supoported word length for this module."""
        return self.supported_bip39_length

#if __name__ == '__main__':
#    bip39 = Bip39()
