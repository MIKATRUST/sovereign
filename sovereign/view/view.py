
'''MVC/View'''

from os import system, name
from prettytable import PrettyTable

def base_m_to_int(numbers, base_m):
    """Function printing python version."""
    return int(''.join([str(n) for n in numbers]), base_m)

# def is_string_length_equal_to(length, string):
#    """Function printing python version."""
#    try:
#        if len(string) == 0:
#            raise ValueError("The string is empty.")
#        elif len(string) != length:
#            raise ValueError(
#                "The length of the string does not match the specified value of n.")
#        return True
#    except ValueError as ve:
#        print(ve)
#        return False

def base6_to_base2(numbers):
    """Function printing python version."""
    base2_numbers = []
    for number in numbers:
        binary_number = format(int(number), '05b')
        base2_numbers.append(binary_number)
    return base2_numbers


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

    def gather_group_input(self, base: int, group_size: int) -> str:
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

    def display_base2_groups(self, words, group_count, word_list):
        """Function printing python version."""
        table = PrettyTable()
        table.field_names = [
            "Word",
            "Coin",
            "Int value",
            "Int value % 2048",
            "BIP39 word"]
        table.align["Int value % 2048"] = "r"

        try:
            for count, word in enumerate(words):
                if group_count and count >= group_count:
                    break
                int_value = base_m_to_int(word, 2)
                table.add_row([f"Word {str(count + 1).zfill(2)}",
                               list(word),
                               int_value,
                               int_value % 2048,
                               word_list[int_value % 2048]])
            print(table.get_string(title="Coin acquisition"))
        except Exception as e:
            print(f"Error: {e}")

    def display_base6_groups(self, words, group_count, word_list):
        """Function printing python version."""
        table = PrettyTable()
        table.field_names = [
            "Word",
            "Dice",
            "Int value",
            "Int value % 2048",
            "BIP39 word"]
        table.align["Int value % 2048"] = "r"

        try:
            for count, word in enumerate(words):
                if group_count and count >= group_count:
                    break
                int_value = base_m_to_int(word, 6)
                table.add_row([f"Word {str(count + 1).zfill(2)}",
                               list(word),
                               int_value,
                               int_value % 2048,
                               word_list[int_value % 2048]])
                print(table.get_string(title="Dice acquisition"))
        except Exception as e:
            print(f"Error: {e}")

    def gather_bip39_word_input(self, nums) -> str:
        """Function printing python version."""
        print("!!!! within gather_bip39_word_input")
        try:
            user_input = input(f"Enter BIP39 word (q to quit): ")
            if user_input.strip().lower() == 'q':
                return 'q'
            elif not user_input:
                raise ValueError("Input cannot be empty")
            elif user_input.strip().lower() in nums:
                return user_input.strip().lower()
        except ValueError as e:
            print(f"Error, not a BIP39 dictionnary word: {e}")
            return None

    def display_bip39_sentance(self, words, nums, title=None):
        """Function printing python version."""
        table = PrettyTable()
        table.field_names = ["Word", "BIP39 word", "Int value"]
        try:
            for count, word in enumerate(words):
                table.add_row(
                    [f"Word {str(count + 1).zfill(2)}", word, nums[word]])
            if title is not None:
                print(table.get_string(title=title))
            else:
                print(table.get_string(title="Table"))
        except Exception as e:
            print(f"Error: {e}")

    def display_menu(self, mode):
        """Function printing python version."""
        # clear()
        print("Menu:")
        print("Mode is " + str(mode) + " words BIP39 sentance")
        print("   0. Toggle mode")
        print("Physical entropy generation, create and fix BIP39 sentance")
        print("   1. Create BIP39 sentance from flipping a coin")
        print("   2. Create BIP39 sentance from rolling a dice")
        print("   3. Create BIP39 sentance from random selection of BIP39 words, fix checksum")
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
