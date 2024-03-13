#Name : Diya Gangwar
#Game : Hangman

import random
from BigD import *

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


    def addLimb(self,letter):
        """ add limbs to the hangman (also changes letter to X in wordlist)
        """
        self.wordlist.update({letter: '* '})
        return
        if w_guess == 1:
            
            self.man[w_guess] == "  ||            |  "
        if w_guess == 2:
            if self.man[1] == '  ||               ':
                self.man[1] == "  ||            O  "
        if w_guess == 3:
            if self.man[2] == '  ||               ':
                self.man[2] == "  ||            |  "
        if w_guess == 4:
            if self.man[2] == "  ||            |  ":
                self.man[2] == "  ||           /|  "
        if w_guess == 5:
            if self.man[2] == "  ||           /|  ":
                self.man[2] == "  ||           /|\ "
        if w_guess == 6:
            if self.man[3] == '  ||               ':
                self.man[3] == "  ||            |  "
        if w_guess == 7:
            if self.man[4] == '  ||               ':
                self.man[4] == "  ||           /   "
        if w_guess == 8:
            if self.man[4] == "  ||           /   ":
                self.man[4] == "  ||           / \ "
                  
   
        
    def addLetter(self,letter,col):
        """add letter to blank (also changes letter to O in wordlist)
        """
        self.wordlist.update({letter: '# '})
        
        for letters in range(self.blank):
            if letters == col:
                if self.word[col] == '_ ':
                    self.word[col] = letter + ' ' 


    def setBoard(self, moveString):
        """ accepts a string and places that string into the blanks on the board

        """
        for col in range(self.blank): 
            for char in moveString: 
                
                self.addLetter(char,col)

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
 
        print(self)

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
        print(random.choice(Dictionary)) 

    def AI_letter(self):
        """ comp chooses a letter randomly from alphabet 
        """
        print(random.choice(("A", "B", "C", "D", "E", "F", "G",
                             "H", "I", "J", "K", "L", "M", "N",
                             "O", "P", "Q", "R", "S", "T", "R",
                             "U", "V", "W", "X", "Y", "Z")))
            

    def hostGame(self):
        """hostGame hosts a game of Hangman with two human players
        """
        print("Welcome to Hangman")
        print(" '#' means that the input is correct and matches the hidden word ")
        print(" '*' means that the input is wrong and does not match the hidden word")
        print("Please note that the hangman is for visual appeal")
        print("It is actually very hard to program the limbs appearing and disappearing")
        print("Please enjoy !!!")
        
        while True:
            user1_word = input("User_1 Enter a word (in all CAPS): ")
            
            word_len1 = len(user1_word)
            print(Board(word_len1))
            w_guess2 = 0
            while w_guess2 < 8:  #while number of wrong guesses by user is less than 8
                user2 = input("Enter a letter (in all CAPS): ")
                print("User_2's Letter is ",user2)

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
                        self.addLimb(user2) 
                        print(self) 
                    else:      #self.matchingLetters(user1_word,user2) == True
                        
                        self.addLetter(user2, self.matchingLetterspos(user1_word,user2))
                        print(self)

                if self.winsFor() == True:
                    print("The Hidden word was", user1_word)
                    print("User 2 was able to guess the word")
                    print("User 2 wins--Congratulations!")
                    
                    self.clear()

            print("The Hidden word was", user1_word)
            print("User 2 was not able to guess the word")        
            print("User 1 wins--Congratulations")



            user2_word = input("User_2 Enter a word (in all CAPS): ")
            word_len2 = len(user2_word)
            print(Board(word_len2))
            w_guess1 = 0
            while w_guess1 < 8:  #while number of wrong guesses by user is less than 8
                user1 = input("Enter a letter (in all CAPS): ")

                while self.allowsMove(user1) == False:
                    print("Invalid input")
                    if user1 not in "A B C D E F G H I J K L M N O P Q R S T R U V W X Y Z":
                        print("Error type : not a character")
                    else:
                        # this never runs as I have not completely fixed allowsMove
                        print("That letter has already been inputted")
                    user1 = input("Enter a letter (in all CAPS):" )

                if self.allowsMove(user1) == True:
                    if self.matchingLetters(user2_word,user1) == False:
                        w_guess1 += 1
                        self.addLimb(user1) 
                        print(self) 
                    else:      #self.matchingLetters(user1_word,user2) == True
                        
                        self.addLetter(user1, self.matchingLetterspos(user2_word,user1))
                        print(self)

                if self.winsFor() == True:
                    print("The Hidden word was", user2_word)
                    print("User 1 was able to guess the word")
                    print("User 1 wins--Congratulations!")
                    
                    self.clear()

            print("The Hidden word was", user2_word)
            print("User 1 was not able to guess the word")        
            print("User 2 wins--Congratulations")
            return



             
b = Board(5)
# ❌ ⭕️