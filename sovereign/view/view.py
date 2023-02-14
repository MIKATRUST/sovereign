#!/usr/bin/env python3

'''MVC/View'''

from os import system, name
from prettytable import PrettyTable

import pdb

def base_m_to_int(numbers, base_m):
    """Function printing python version."""
    return int(''.join([str(n) for n in numbers]), base_m)

def base6_to_base2(numbers):
    """Function printing python version."""
    base2_numbers = []
    for number in numbers:
        binary_number = format(int(number), '05b')
        base2_numbers.append(binary_number)
    return base2_numbers

def number_to_base(n, b):
    """Function printing python version."""
    if n == 0:
        return 0
    digits = ""
    while n:
        digits = digits + str(int(n % b))
        n //= b
    return digits[::-1]

class View:

    '''Demonstrates triple double quotes
    docstrings and does nothing really.'''

    def __init__(self):
        if __debug__:
            print("View constructor")

    def clear(self):
        """Function printing python version."""
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def show_error(self, error_msg):
        """Function printing python version."""
        print("Error:", error_msg)

    def gather_6s_dice_input(self) -> str:
        """Function printing python version."""
        group_size = 6
        try:
            user_input = input(
                f"Enter 6 characters between 1 and 4, if the dice does not roll to one of this value, please roll again (q to quit): ")
            if user_input.strip().lower() == 'q':
                return 'q'
            elif not user_input:
                raise ValueError("Input cannot be empty")
            elif len(user_input) != group_size:
                raise ValueError(
                    f"Input must have exactly {group_size} characters")
            for char in user_input:
                if int(char) > 4 or int(char) < 1:
                    raise ValueError(
                        f"Invalid character '{char}' entered, expected values between 1 and 4")
            return user_input
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def gather_group_input(self, base: int, group_size: int) -> str:
        """Function printing python version."""
        try:
            user_input = input(
                f"Enter {group_size} characters between 0 and {base - 1} (q to quit): ")
            if user_input.strip().lower() == 'q':
                return 'q'
            elif not user_input:
                raise ValueError("Input cannot be empty")
            elif len(user_input) != group_size:
                raise ValueError(
                    f"Input must have exactly {group_size} characters")
            for char in user_input:
                if int(char) >= base or int(char) < 0:
                    raise ValueError(
                        f"Invalid character '{char}' entered, expected values between 0 and {base - 1}")
            return user_input
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def display_base2_groups(self, bip39_words, get_bip39_word_value):
        """Function printing python version."""
        table = PrettyTable()

        table.field_names = [
            "Word",
            "Coin",
            "Int value",
            "BIP39 word"]

        table.align["Word"] = "r"

        for count, word in enumerate (bip39_words.split()):
            table.add_row([f"{str(count + 1).zfill(2)}",
                bin(get_bip39_word_value(word))[2:].zfill(11),
                get_bip39_word_value(word),
                word])

        #pdb.set_trace()

        print(table.get_string(title="Coin acquisition"))
    
    def display_6s_dice_groups(self, bip39_words, get_bip39_word_value):
        """Function printing python version."""
        table = PrettyTable()
        table.field_names = [
            "Word",
            "Dice",
            "Int value",
            "Int value % 2048",
            "BIP39 word"]
        table.align["Int value % 2048"] = "r"

        #pdb.set_trace()
            
        for count, word in enumerate (bip39_words.split()):
            #pdb.set_trace()
            table.add_row([f"{str(count + 1).zfill(2)}",
                str(number_to_base(get_bip39_word_value(word), 4)).zfill(6).replace("0", "4"),
                bin(get_bip39_word_value(word))[2:].zfill(11),
                get_bip39_word_value(word),
                word])

        print(table.get_string(title="Dice acquisition"))


    def gather_bip39_word_input(self, is_valid_words) -> str:
        """Function printing python version."""
        try:
            user_input = input(f"Enter BIP39 word (q to quit): ")
            #pdb.set_trace()
            if user_input.strip().lower() == 'q':
                return 'q'
            elif not user_input:
                raise ValueError("Input cannot be empty")
            #TBD : bug belo,always true
            elif is_valid_words(user_input.strip().lower()):
                return user_input.strip().lower()
        except ValueError as e:
            print(f"Error, not a BIP39 dictionnary word: {e}")
            return None

    def gather_mode(self, supported_modes) -> str:
        """Function printing python version."""
        print(f"Supported BIP39 modes are {supported_modes} words")
        while True:
            user_input = input(f"Enter expected mode: ")
            if (str(user_input) in str(supported_modes)):
                break
            else:
                print ('Value not supported')         
        return user_input

    def display_bip39_sentance(self, words, get_bip39_word_value, title=None):
        """Function printing python version."""
        table = PrettyTable()
        table.field_names = ["Word", "BIP39 word", "Int value"]

        try:
            for count, word in enumerate(words.split()):
                table.add_row(
                    [f"{str(count + 1).zfill(2)}", word, get_bip39_word_value(word)])
            if title is not None:
                print(table.get_string(title=title))
            else:
                print(table.get_string(title="Table"))
        except Exception as e:
            print(f"Error: {e}")

    def display_menu(self, get_mode):
        """Function printing python version."""
        # clear()
        print("Menu:")
        print(f"Mode is {get_mode()} words BIP39 sentance")
        print("   0. Toggle mode")
        print("Physical entropy generation, create and fix BIP39 sentance")
        print("   1. Create BIP39 sentance from flipping a coin")
        print("   2. Create BIP39 sentance from rolling a dice")
        print("   3. Create BIP39 sentance from random manual selection of BIP39 words, fix checksum")
        print("Combine BIP39 sentances")
        print("   4. Load BIP39 sentance")
        print("   5. Show loaded BIP39 sentance(s)")
        print("   6. Combine loaded BIP39 sentances (XOR)")
        print("Hierarchical Deterministic (HD) wallets")
        print("   7. Load password (optional) [tbd]")
        print("   8. Compute seed [tbd]")
        print("Other")
        print("   7. Exit")
        print("   8. Print BIP39 words [tbd]")
        print("Tests")
        print("   20. Load 3 BIP39 12 words sentances")
        print("   21. Load 3 BIP39 24 words sentances")

    def get_menu_choice(self):
        """Function printing python version."""
        return input("Enter your choice: ")
        # user_input = input("Enter your choice: ")

    def handle_invalid_choice(self):
        """Function printing python version."""
        print("Invalid input, please enter a number between 1 and 7")
