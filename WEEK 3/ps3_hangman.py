# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    flag = False
    for char in secretWord:
        if char in lettersGuessed:
            flag = True
        else:
            flag = False
            break
    
    return flag


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word = ""
    for char in secretWord:
        if char in lettersGuessed:
            word += char
        else:
            word += "_"
        word += "  "
    
    
    return word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    l = list(string.ascii_lowercase)

    for ele in lettersGuessed:
        if ele in l:
            l.remove(ele)
    
    availableLetters = "".join(l)
           
    return availableLetters
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game Hangman!")
    lenSecretWord = len(secretWord)
    print("I am thinking of a word that is", lenSecretWord, "letters long")
    print("-----------")
    numberOfGuess = 8
    letterGuessed =[]
    guessList = []
    flag = False
    
    while numberOfGuess > 0:
        print("You have", numberOfGuess,"guesses left")
        print("Available Letters:",getAvailableLetters(letterGuessed))
        guess = input("Please guess a letter: ")
        guess = guess.lower()
        letterGuessed.append(guess)
        w = getGuessedWord(secretWord, letterGuessed)
        
                  
        if guess in guessList:
            print("Oops! You've already guessed that letter:", w)
            
        elif guess not in secretWord:
            print("Oops! That letter is not in my word:", w)
            numberOfGuess -= 1
            
        else:
            print("Good guess: "+ w)
            
            if isWordGuessed(secretWord, letterGuessed):
               flag = True
               break     
            
            
        print("------------")
        
        if guess not in guessList:
            guessList.append(guess)
        
            
    if flag:
        print("-----------")
        print("Congratulations, you won!")

    if numberOfGuess == 0:
        print("Sorry, you ran out of guesses. The word was", secretWord+".")
        

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
