#!/usr/bin/env python3

'''BIP39'''

import hashlib

class Bip39():
    """Implementation of the BIP39 standard for mnemonic phrases. Supports English only.
       This class implements BIP39 checksum verification and correction.

    Attributes:
        SUPPORTED_PHRASE_LENGTHS (list of int): Supported lengths for BIP39 phrases in words.
        word_list (list of str): List of words from the BIP39 wordlist.
        word_index (dict): Dictionary mapping words to their index in the wordlist.
    """

    def __init__(self, wordlist_file = './sovereign/model/english.txt'):
        """Initialize the BIP39 class.

        Loads the BIP39 wordlist from the specified file and sets up the `word_list` and `word_index` attributes.

        Args:
            wordlist_file (str, optional): Path to the file containing the BIP39 wordlist. Defaults to './sovereign/model/english.txt'.
        """
        if __debug__:
            print("Bip39 constructor ")

        self.wordlist = self._load_wordlist(wordlist_file)
        self.word_to_index = {word: index for index, word in enumerate(self.wordlist)}
        self.SUPPORTED_PHRASE_LENGTHS = [12, 15, 18, 21, 24]

    @staticmethod
    def _load_wordlist(file_path):
        with open(file_path, encoding="utf-8") as f:
            return [word.strip() for word in f]

    def get_word(self, index: int) -> str:
        """Get the BIP39 word from index value."""
        return self.wordlist[index]

    def get_word_index(self, word: str) -> int:
        """Get the index from the BIP39 word."""
        return self.word_to_index[word]

    def is_valid_words(self, sentance: str) -> bool:
        """Check if word(s) are valid BIP39 word(s).""" 
        words = sentance.split()
        return all(word in self.wordlist for word in words)

    def get_supported_mnem_lengths(self) -> list:
        """Get the supported modes, i.e BIP39 supoported mnemonic lengths."""
        return self.SUPPORTED_PHRASE_LENGTHS

    def is_supported_mnem_length(self, mnemonic: str) -> bool:
        """Check if a mnemonic is supported."""
        words = mnemonic.split()
        return len(words) in self.SUPPORTED_PHRASE_LENGTHS
    
    def binary_words_to_bip39_phrase(self, binary_words: str) -> str:
        """Convert a binary sequence into a BIP39 phrase.
        Args:
            binary_words (str): Binary sequence to convert.

        Returns:
            str: BIP39 phrase.
        """
        phrase = ""
        for i in range (int(len(binary_words)/11)):
            binary_word = binary_words[i*11:(i+1)*11]
            phrase += self.get_word(int(binary_word,2)) + " "
        return phrase.strip()

    def dice_to_bip39_phrase(self, dice_words: str) -> str:
        """Convert a dice sequence [1-4] into a BIP39 phrase.
           To keep uniform probability and simplify process auditing, 
           this function use number from 1 to 4.
        Args:
            dice_words (str): Dice sequence to convert.

        Returns:
            str: BIP39 phrase.
        """
        phrase = ""
        for i in range (int(len(dice_words) / 6)):
            dice_word = dice_words[i*6:(i+1)*6].replace('4', '0')
            #6 dice rolls (12 bits), maximum value = 4095, need to get back to 11 bits
            phrase += self.get_word(int(dice_word, 4) % 2048) + " "
        return phrase.strip()

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
            int_sentance = (int_sentance << 11) + self.word_to_index[word]
        
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
            int_sentance = (int_sentance << 11) + self.word_to_index[word]
        
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

#if __name__ == '__main__':
#    bip39 = Bip39()