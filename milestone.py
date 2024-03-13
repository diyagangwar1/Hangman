#Name : Diya Gangwar
#Game : Hangman

import random
from BigD import *
import colorama
from colorama import Fore, Back, Style

class Board:
    """A data type representing a HangMan board
       with an arbitrary number of blanks for any word.
    """
    
    def __init__(self, blank):
        """Construct objects of type Board, with the given parameters"""
        self.blank = blank
        self.word = [('_ ') for col in range(self.blank)]
        self.wordlist = { 'A': 'A ',  'B': 'B ',  'C': 'C ',  'D': 'D ',  'E': 'E ',
                          'F': 'F ',  'G': 'G ',  'H': 'H ',  'I': 'I ',  'J': 'J ',
                          'K': 'K ',  'L': 'L ',  'M': 'M ',  'N': 'N ',  'O': 'O ',
                          'P': 'P ',  'Q': 'Q ',  'R': 'R ',  'S': 'S ',  'T': 'T ',
                          'U': 'U ',  'V': 'V ',  'W': 'W ',  'X': 'X ',  'Y': 'Y ',  
                          'Z': 'Z '   }
        man_height = 5
        self.man = [('  ||               ') for row in range(man_height)]


    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        a = " ________________________ " "\n"
        b = "|________________________|" "\n"
        #c = "  ||            |  " "\n"
        #d = "  ||            O  " "\n"
        #e = "  ||           /|\ " "\n"
        #f = "  ||            |  " "\n"
        #g = "  ||           / \ " "\n"
        man = ''
        for row in range(5):
            man += self.man[row] + "\n"

        h = "  ||               " "\n"
        i = " /__\ ___________________" "\n" "\n"
        word = ''
        for col in range(self.blank):
            word += self.word[col]
            #self.word += '_ '
        wordlist = list(self.wordlist.values())
        wordstr = ''.join(wordlist)

        return a + b + man + h + i + "          " + word + "\n" "\n" + wordstr


    def addLimb(self,letter,w_guess):
        """ add limbs to the hangman (also changes letter to 🅾️ in wordlist)
        """
        self.wordlist.update({letter: '🅾️  '})
        if w_guess == 1:
            
            self.man[0] = "  ||            |  "
        if w_guess == 2:
            if self.man[1] == '  ||               ':
                self.man[1] = "  ||            O  "
        if w_guess == 3:
            if self.man[2] == '  ||               ':
                self.man[2] = "  ||            |  "
        if w_guess == 4:
            if self.man[2] == "  ||            |  ":
                self.man[2] = "  ||           /|  "
        if w_guess == 5:
            if self.man[2] == "  ||           /|  ":
                self.man[2] = "  ||           /|\ "
        if w_guess == 6:
            if self.man[3] == '  ||               ':
                self.man[3] = "  ||            |  "
        if w_guess == 7:
            if self.man[4] == '  ||               ':
                self.man[4] = "  ||           /   "
        if w_guess == 8:
            if self.man[4] == "  ||           /   ":
                self.man[4] = "  ||           / \ "
                
        
    def addLetter(self,letter,col):
        """add letter to blank (also changes letter to ❎ in wordlist)
        """
        self.wordlist.update({letter: '❎ '})
        
        for letters in range(self.blank):
            if letters == col:
                if self.word[col] == '_ ':
                    self.word[col] = letter + ' ' 


    def setBoard(self, moveString):
        """ accepts a string and places that string into the blanks on the board
            
        """
        col = 0
        for char in moveString: 
                self.addLetter(char,col)
                col += 1

    def matchingLetters(self,word,letter):
        """ checks if a given letter is in the word and returns True or False
        """
        if letter in word:
            return True
        else:
            return False

    def matchingLetterspos(self,word,letter):
        """ returns the position of the matching letter in the word
        """
        if self.matchingLetters(word,letter) == True:
            return word.index(letter)
        

    def clear(self):
        """ clears board
        """
        self.wordlist.update({ 'A': 'A ',  'B': 'B ',  'C': 'C ',  'D': 'D ',  'E': 'E ',
                               'F': 'F ',  'G': 'G ',  'H': 'H ',  'I': 'I ',  'J': 'J ',
                               'K': 'K ',  'L': 'L ',  'M': 'M ',  'N': 'N ',  'O': 'O ',
                               'P': 'P ',  'Q': 'Q ',  'R': 'R ',  'S': 'S ',  'T': 'T ',
                               'U': 'U ',  'V': 'V ',  'W': 'W ',  'X': 'X ',  'Y': 'Y ',  
                               'Z': 'Z '   })
        for letters in range(self.blank):          
            if self.word[letters] != '_ ':
                self.word[letters] =  '_ ' 
        for rows in range(5):
            if self.man[rows] != '  ||               ':
                self.man[rows] = '  ||               '
 
        

    def allowsMove(self, input):
        """ return True if the calling object does allow a move into blank space.
        """
        # needs to be changes so that user can not input same character over and over again
        # needs to check if input is values for self.wordlist 
        if input not in "A B C D E F G H I J K L M N O P Q R S T R U V W X Y Z":
            return False
        else:
            return True


    def winsFor(self):
        """ returns True, if all the blanks are not empty
        """ 
        result = 0
        blank = int(self.blank)  
        for letters in range(blank):
            if self.word[letters] != '_ ':
                result += 1
        return result == blank

    def AI_word(self):
        """ comp chooses a word randomly from BigD.py
        """
        word = str(random.choice(Dictionary)) 
        return word

    def AI_letter(self):
        """ comp chooses a letter randomly from alphabet 
        """
        letter = str(random.choice(("A", "B", "C", "D", "E", "F", "G",
                             "H", "I", "J", "K", "L", "M", "N",
                             "O", "P", "Q", "R", "S", "T", "R",
                             "U", "V", "W", "X", "Y", "Z")))
        return letter
            

    def hostGame_AI(self,user1_word):
        """hostGame hosts a game of Hangman with two human players
        """
        while True:
            
            #user1_word = input("User Enter a word (in all CAPS): ")
            
            #word_len1 = len(user1_word)

            #self.blank = len(user1_word)
            
            print(self)
            w_guess2 = 0
            while w_guess2 < 8:  #while number of wrong guesses by user is less than 8
                user2 = self.AI_letter()
                print("Comp's Letter is ",user2)

                while self.allowsMove(user2) == False:
                    print("Invalid input")
                    if user2 not in "A B C D E F G H I J K L M N O P Q R S T R U V W X Y Z":
                        print("Error type : not a character")
                    else:
                        # this never runs as I have not completely fixed allowsMove
                        print("That letter has already been inputted")
                    user2 = input("Enter a letter (in all CAPS):" )

                if self.allowsMove(user2) == True:
                    if self.matchingLetters(user1_word,user2) == False:
                        w_guess2 += 1 
                        self.addLimb(user2, w_guess2)
                        
                        print(self) 
                    else:      #self.matchingLetters(user1_word,user2) == True
                        
                        self.addLetter(user2, self.matchingLetterspos(user1_word,user2))
                        print(self)

                if self.winsFor() == True:
                    print("The Hidden word was", user1_word)
                    print("Comp was able to guess the word")
                    print("Comp wins--Congratulations!")
                    #g.num_comp_wins += 1
                    
                    self.clear()

            print("The Hidden word was", user1_word)
            print("Comp was not able to guess the word")        
            print("User wins--Congratulations")
            #g.num_user_wins += 1
            self.clear()
            

            return





    def hostGame_human(self,user1_word,):
        """hostGame hosts a game of Hangman with two human players
        """
        while True:
            
            #user1_word = self.AI_word()
            
            #word_len1 = len(user1_word
            
            print(self)
            
            w_guess2 = 0
            while w_guess2 < 8:  #while number of wrong guesses by user is less than 8
                user2 = input("User Enter a letter (in all CAPS): ")
                #print("User_2's Letter is ",user2)

                while self.allowsMove(user2) == False:
                    print("Invalid input")
                    if user2 not in "A B C D E F G H I J K L M N O P Q R S T R U V W X Y Z":
                        print("Error type : not a character")
                    else:
                        # this never runs as I have not completely fixed allowsMove
                        print("That letter has already been inputted")
                    user2 = input("Enter a letter (in all CAPS):" )

                if self.allowsMove(user2) == True:
                    if self.matchingLetters(user1_word,user2) == False:
                        w_guess2 += 1 
                        self.addLimb(user2, w_guess2)
                        
                        print(self) 
                    else:      #self.matchingLetters(user1_word,user2) == True
                        
                        self.addLetter(user2, self.matchingLetterspos(user1_word,user2))
                        print(self)

                if self.winsFor() == True:
                    print("The Hidden word was", user1_word)
                    print("User was able to guess the word")
                    print("User wins--Congratulations!")
                    #user2_score += 1
                    
                    self.clear()

            print("The Hidden word was", user1_word)
            print("User was not able to guess the word")        
            print("Comp wins--Congratulations")
            self.clear()
            return
           
#
# RPS encapsulated into a class
#

import random
import webbrowser

class RPSGame:
    """An RPS rivalry that tracks, saves, and loads games"""

    def __init__(self):
        """The constructor.
           Should include count of wins for each player.
        """
        self.num_comp_wins = 0
        self.num_user_wins = 0
        self.num_ties = 0


    def __repr__(self):
        """The representation function.
           Should return a string of some sort.
        """
        s = ''
        s += "I have won" + str(self.num_comp_wins) + "games.\n"
        s += "You have won" + str(self.num_user_wins) + "games.\n"
        s += "We've tied" + str(self.num_ties) + "games.\n"
        return s


    def play_one_round(self):
        """Plays one game."""
        

    def lookup(self, abbreviation):
        """Looks up the full name of each RPS gesture"""
        G = {"r": "rock", "s": "scissors", "p": "paper"}
        if abbreviation in G:
            return G[abbreviation]
        else:
            return "????"

    def status(self):
        """Prints the current status."""
        print("\n+ Current tally +")
        print("    My wins:", self.num_comp_wins)
        print("  Your wins:", self.num_user_wins)
        print("       Ties:", self.num_ties)
        print()


    def menu(self):
        """Prints the menu."""
        print()
        self.status()
        print("Menu:")
        print("  (1) Continue our Hangman rivalry")
        print("  (2) Load our game")
        print("  (4) Save our game")
        print("  (8) Quit")
        print()
        uc = input("Your choice: ")
        try:
            uc = int(uc)  # try converting to an integer
            if uc not in [1, 2, 4, 8, 42]:  # Easter eggs are welcome!
                print("    Didn't recognize that input\n")
            else:
                return uc  # _must_ be a 1, 2, 4, or 42

        except ParseError as e:  # it wasn't an integer...
            print("    Didn't understand that input\n")
            # print("The error was:", e)
        
        return self.menu()


    def play(self):
        """Hosts a series of games or turns."""
        while True:
            userchoice = self.menu()  # Prints the welcome and menu 

            if userchoice == 1:
                
                self.play_one_round()

            if userchoice == 8:
                print("Til next time!")
                break

            if userchoice == 4:
                self.save_game("gamefile.txt")

            if userchoice == 2:
                self.load_game("gamefile.txt")
                print("Welcome back!")

            if userchoice == 42:  # Lofi!
                webbrowser.open_new_tab("https://www.youtube.com/watch?v=5qap5aO4i9A")


    def play_one_round(self):
        """plays one round of hangman
        """
        print("Welcome to Hangman")
        print(" '❎' means that the input is correct and matches the hidden word ")
        print(" '🅾️' means that the input is wrong and does not match the hidden word")
        



        user = str(input("Enter a word (in all CAPS):"))
        u_w = int(len(user))
        u = Board(u_w)
        u.hostGame_AI(user)

        comp = str(random.choice(Dictionary))
        cc =comp.upper()
        c_w = int(len(comp))
        c = Board(c_w)
        c.hostGame_human(cc)

        return


        
        







    def save_game(self, filename):
        """Save to a file."""
        f = open(filename, "w")  # Open file for writing
        print(self.num_comp_wins, file = f)
        print(self.num_user_wins, file = f)
        print(self.num_ties, file = f)
        f.close()
        print(filename, "saved.")


    def load_game(self, filename):
        """Load from a file."""
        f = open(filename, "r")  # Open file for reading
        self.num_comp_wins = int(f.readline())
        self.num_user_wins = int(f.readline())
        self.num_ties = int(f.readline())
        f.close()
        print(filename, "loaded.")
            
g = RPSGame()

# play when run
g.play()


             
b = Board(5)
# ❌ ⭕️ 