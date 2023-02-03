from os import system, name
import sys
import hashlib
import binascii
from prettytable import PrettyTable

# Model

class Model:
    def __init__(self):
        #print("CONSTRUCTOR MODEL")
        #self.data = []
        self.bip39Sentances = []
        self.mode = int(24)
        # Initialize a list to store the BIP39 words
        self.wordlist = []
        # Initialize a dictionary to store the word-to-number mapping
        self.nums = {}
        # Load word list
        with open('english.txt') as fin:
            i = 0
            for word in fin:
                self.nums[word.strip()] = i
                self.wordlist.append(word.strip())
                i = i + 1
        if(len(self.wordlist) != 2048): 
            sys.exit('\nError. '+ str(len(self.wordlist)) +' words loaded, should have been 2048. Exited from the script.\n')

    def addBip39Sentance(self, sentance):
        print(len(self.bip39Sentances))
        self.bip39Sentances.append(sentance)
        print(self.bip39Sentances)
    
    def getBip39sentances(self):
        return self.bip39Sentances

    def load_3_12w_bip39_sentances(self):
        self.mode = int(12)
        self.bip39Sentances.append(['zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','wrong'])
        self.bip39Sentances.append(['zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','abstract'])
        self.bip39Sentances.append(['abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'surface'])
        print("loaded load_3_12w_bip39_sentances")
    
    def load_3_24w_bip39_sentances(self):
        self.mode = int(24)
        self.bip39Sentances.append(['zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','vote'])
        self.bip39Sentances.append(['zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo','zoo', 'vote'])
        self.bip39Sentances.append(['abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon','abandon','street'])
        print("loaded load_3_24w_bip39_sentances")

    def setMode(self, mode):
        self.mode = int(mode)

    def getMode(self):
        return int(self.mode)

# View
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def base_m_to_int(numbers,m):
    return int(''.join([str(n) for n in numbers]), m)

def isStringLengthEqualTo(n, string):
    try:
        if len(string) == 0:
            raise ValueError("The string is empty.")
        elif len(string) != n:
            raise ValueError("The length of the string does not match the specified value of n.")
        return True
    except ValueError as ve:
        print(ve)
        return False

def base6_to_base2(numbers):
    base2_numbers = []
    for number in numbers:
        binary_number = format(int(number), '05b')
        base2_numbers.append(binary_number)
    return base2_numbers

class View:
    def __init__(self):
        pass
        #print("CONSTRUCTOR VIEW")

    #def show_data(self, data):
    #    print("Data:", data)

    def clear(self):
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def show_error(self, error_msg):
        print("Error:", error_msg)

    def gather_group_input(self, base: int, group_size: int) -> str:
        try:
            user_input = input(f"Enter {group_size} characters between 0 and {base - 1} (q to quit): ")
            if user_input.strip().lower() == 'q':
                return 'q'
            elif not user_input:
                raise ValueError("Input cannot be empty")
            elif len(user_input) != group_size:
                raise ValueError(f"Input must have exactly {group_size} characters")
            for char in user_input:
                if int(char) >= base or int(char) < 0:
                    raise ValueError(f"Invalid character '{char}' entered, expected values between 0 and {base - 1}")
            return user_input
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def display_base2_groups(self, words, group_count, word_list):
        table = PrettyTable()
        table.field_names = ["Word", "Coin", "Int value", "Int value % 2048", "BIP39 word"]
        table.align["Int value % 2048"] = "r"

        try:
            for count, word in enumerate(words):
                if group_count and count >= group_count:
                    break
                int_value = base_m_to_int(word, 2)
                table.add_row([f"Word {str(count + 1).zfill(2)}", 
                           list(word), int_value, int_value % 2048, word_list[int_value % 2048]])
            print(table.get_string(title="Coin acquisition"))
        except Exception as e:
            print(f"Error: {e}")


    def display_base6_groups(self, words, group_count, word_list):
        table = PrettyTable()
        table.field_names = ["Word", "Dice", "Int value", "Int value % 2048", "BIP39 word"]
        table.align["Int value % 2048"] = "r"

        try:
            for count, word in enumerate(words):
                if group_count and count >= group_count:
                    break
                int_value = base_m_to_int(word, 6)
                table.add_row([f"Word {str(count + 1).zfill(2)}", 
                           list(word), int_value, int_value % 2048, word_list[int_value % 2048]])
                print(table.get_string(title="Dice acquisition"))
        except Exception as e:
            print(f"Error: {e}")
    
    def gather_BIP39_word_input(self, nums) -> str:
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

    def display_BIP39_sentance(self, words, nums, title = None):
        table = PrettyTable()
        table.field_names = ["Word", "BIP39 word", "Int value"]
        try:
            for count, word in enumerate(words):
                table.add_row([f"Word {str(count + 1).zfill(2)}", word, nums[word]])
            if title != None :
                print(table.get_string(title = title ))
            else:
                print(table.get_string(title="Table"))
        except Exception as e:
            print(f"Error: {e}")

    def displayMenu(self, mode):
        #clear()
        print("Menu:")
        print("Mode is " + str(mode) + " words BIP39 sentance")
        print("   0. Toggle mode")
        print("Create and fix BIP39 sentance")
        print("   1. Create BIP39 sentance from coin")
        print("   2. Create BIP39 sentance from dice")
        print("   3. Create BIP39 sentance from BIP39 words, fix checksum")
        print("Combine BIP39 sentances")
        print("   4. Load BIP39 sentance")
        print("   5. Show BIP39 sentance(s)")
        print("   6. !!TBD!!! Combine BIP39 sentances (XOR)")
        print("Hierarchical Deterministic (HD) wallets")
        print("     TBD")
        print("Other")
        print("   7. Exit")
        print("   8. Print BIP39 words")
        print("Tests")
        print("   20. Load 3 BIP39 12 words sentances")
        print("   21. Load 3 BIP39 24 words sentances")

    def getMenuChoice(self):
        return(input("Enter your choice: "))
        #user_input = input("Enter your choice: ")
    
    def handleInvalidChoice(self):
        print("Invalid input, please enter a number between 1 and 7")

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
def Bip39SentancesXor(Bip39sentances, wordlist, nums):
    Nxored = int(0)
    sentanceR = []

    for sentance in Bip39sentances:
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
        #print("CONSTRUCTOR CONTROLLER")
        check_system_compatibility()
        # self.model = Model()
        # self.view = View()

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
        if(model.getMode() == int(24)):
            model.setMode(int(12))
        else:
            model.setMode(int(24))
    
    def option1(self):
        view.clear()
        print("You selected Option 1")

        words=[]
        base = 2
        group_count = model.getMode() # 12 or 24
        group_size = 11

        while len(words) < group_count:
            user_input= view.gather_group_input(base, group_size)
            if user_input == 'q':
                return
            if user_input is not None:
                words.append(user_input)
            else:
                print("Error: invalid user_input")
            view.display_base2_groups(words, group_count, wordlist)
        
        print("Fixing the BIP39 sentance with a valid checksum")
        print("The BIP39 sentance below is valid (the checksum is correct)")
       
        bip39_words = binary_words_to_bip39_words(words, model.wordlist)
        valid_bip39_sentance = fix_bip39_checksum(bip39_words)
        view.display_BIP39_sentance(valid_bip39_sentance, model.nums)
 
    def option2(self):
        print("You selected Option 2")
        words=[]
        base = 6
        group_count = model.getMode()
        group_size = 5

        while len(words) < group_count:
            user_input= view.gather_group_input(base, group_size)
            if user_input == 'q':
                return 'q'
            elif user_input is not None:
                words.append(user_input)
            else:
                print("Error: invalid user_input")
            view.display_base6_groups(words, group_count, wordlist)

        print("Fixing the BIP39 sentance...")
        print("The BIP39 sentance below is valid (the checksum is correct)")
        bip39_words = senary_words_to_bip39_words(words, model.wordlist)
        valid_bip39_sentance = fix_bip39_checksum(bip39_words)
        view.display_BIP39_sentance(valid_bip39_sentance, model.nums)
  
    def option3(self):
        print("You selected Option 3")
        words=[]
        group_count = model.getMode() # 12 or 24

        while len(words) < group_count:
            word = view.gather_BIP39_word_input(model.nums)
            if word == 'q':
                return
            elif word is not None :
                words.append(word)
            else:
                print("Error: invalid BIP39 word")
            clear()
            view.display_BIP39_sentance(words, model.nums)

        print(words)
        if is_valid_bip39_sentence(words, model.nums, model.wordlist):
            print("The entered BIP39 sentance above is valid (checksum is correct)")
        else:
            print("The entered BIP39 sentance above is invalid (checksum is incorrect)")
            print("Fixing the BIP39 sentance...")
            print("The BIP39 sentance below is valid (the checksum is correct)")
            valide_BIP39_sentance = fix_bip39_checksum(words)
            view.display_BIP39_sentance(valide_BIP39_sentance, model.nums)

    def option4(self):
        print("You selected Option 4")
        words=[]
        group_count = model.getMode() # 12 or 24

        while len(words) < group_count:
            word = view.gather_BIP39_word_input(model.nums) 
            if word == 'q':
                return 'q'
            if word is not None :
                words.append(word)
            else:
                print("Error: invalid BIP39 word")
            clear()
            view.display_BIP39_sentance(words, model.nums)

        print("Checking BIP39 sentance")
        if is_valid_bip39_sentence(words, model.nums, model.wordlist, hash_method=hashlib.sha256):
            print("The BIP39 sentance below is valid")
            model.addBip39Sentance(words)
            view.display_BIP39_sentance(words, model.nums)
        else:
            print("The entered BIP39 is not valid")
 
    def option5(self):
        print("You selected Option 5")
        sentances = model.getBip39sentances()
        print("Number of BIP39 sentances: " + str(len(sentances)))
        for count, sentance in enumerate (sentances):
            view.display_BIP39_sentance(sentance, model.nums, "BIP39 sentance #" + str(count+1))

    def option6(self):
        print("You selected Option 6")
        #!!! before, we need to check that there are at least 2 BIP39_entances
        BIP39_sentance = Bip39SentancesXor(model.bip39Sentances, model.wordlist, model.nums)
        print(BIP39_sentance)
        view.display_BIP39_sentance(BIP39_sentance, model.nums, "BIP39 XORED sentance")
    
    def option20(self):
        print("You selected Option 20")
        #self.bip39Sentances
        model.load_3_12w_bip39_sentances()

    def option21(self):
        print("You selected Option 21")
        model.load_3_24w_bip39_sentances()

    def exit_program(self):
        clear()
        quit()
        print("Exiting...")
    
#    def add_data(self, item):
#        try:
#            self.model.add_data(item)
#        except Exception as e:
#            self.view.show_error(str(e))
#        else:
#            self.view.show_data(self.model.get_data())

# Client code
if __name__ == "__main__":
    controller = Controller()
    model = Model()
    view = View()

    view.clear()
    while True:
        view.displayMenu(int(model.getMode()))
        choice = view.getMenuChoice()
        #controller.userInputIsValid()
        if choice in controller.options:
            controller.options[choice]()
            #getattr(toto, "option" + user_input)()
            #toto.option1()
        else:
            view.handleInvalidChoice()

