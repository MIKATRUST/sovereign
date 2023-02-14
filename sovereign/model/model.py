#!/usr/bin/env python3

'''MVC/Model'''

class Model():
    """Class for the Model component of the MVC architecture.

    Attributes:
        bip39_sentances (list): List of BIP39 sentences.
        mode (int): Mode of the model.
    """

    def __init__(self):
        """Initialize the model.

        Loads the BIP39 wordlist from the english.txt file and sets up the wordlist and nums attributes.
        """
        if __debug__:
            print("Model constructor")

        self.bip39_sentances = []
        self.mode = 24
    
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

    def load_3_12w_bip39_sentances(self): # pragma: no cover
        """Function printing python version."""
        self.set_mode = int(12)
        fun = self.add_bip39_sentance
        
        fun('zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo abstract')
        fun('zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo wrong')  
        fun('abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about')

        if __debug__:
            print("Loaded load_3_12w_bip39_sentances")

    def load_3_24w_bip39_sentances(self): # pragma: no cover
        """Function printing python version."""
        self.set_mode = int(24)
        fun = self.add_bip39_sentance
        
        fun('zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo vote')
        fun('zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo buddy')
        fun('abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon art')

        if __debug__:
            print("Loaded load_3_24w_bip39_sentances")
