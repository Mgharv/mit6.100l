# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

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
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    has_won = True

    for letter in secret_word:
        if letter not in letters_guessed:
            has_won = False

    return has_won



def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """

    progress = list(secret_word)

    for i in range(len(progress)):
        if secret_word[i] not in letters_guessed:
            progress[i] = "*"
    return  "".join(progress)


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    available_letters = []
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available_letters.append(letter)
    return ''.join(available_letters)


def hangman(secret_word, with_help):
    print("Welcome to Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("------")

    guesses_left = 10
    letters_guessed = []
    remaining_letters = list(set(secret_word))
    vowels = ['a', 'e', 'i', 'o', 'u']

    #Run game while there are still guesses left
    while guesses_left > 0:

        #check if player has won, end game
        if has_player_won(secret_word, letters_guessed):
            unique_letters = len(set(secret_word))
            total_score = (guesses_left + 4 * unique_letters) + (3 * len(secret_word))
            print("Congratulations, you won!")
            print("Your total score for this game is:", total_score)
            return

        #Inform player number of guesses left
        if guesses_left == 1:
            print("You have 1 guess left.")
        else:
            print("You have", guesses_left, "guesses left.")

        # Informs user letters to choose from
        print("Available letters:", get_available_letters(letters_guessed))

        guess = input("Please guess a letter: ").lower()

        #help functionality
        if guess == "!" and with_help:
            if guesses_left >= 3:
                reveal_letter = random.choice(remaining_letters)
                letters_guessed.append(reveal_letter)
                remaining_letters.remove(reveal_letter)
                print("Letter revealed:", reveal_letter)
                print(get_word_progress(secret_word, letters_guessed))
                guesses_left -= 3
            else:
                print("Oops! Not enough guesses left:", get_word_progress(secret_word, letters_guessed))
            print("------")
            continue
        elif guess == "!" and not with_help:
            print("Sorry, help function is turned off.")

        # check if guess is valid input
        if not guess.isalpha() or len(guess) != 1:
            print("Oops! That is not a valid letter. Please input a letter from the alphabet:",
                  get_word_progress(secret_word, letters_guessed))
            print("------")
            continue

        #check if letter has already been guessed
        if guess in letters_guessed:
            print("Oops! You've already guessed that letter:",
                  get_word_progress(secret_word, letters_guessed))
            print("------")
            continue

        letters_guessed.append(guess)

        #user guessed correctly
        if guess in secret_word:
            if guess in remaining_letters:
                remaining_letters.remove(guess)
            print("Good guess:", get_word_progress(secret_word, letters_guessed))
        else:
            print("Oops! That letter is not in my word:",
                  get_word_progress(secret_word, letters_guessed))
            guesses_left -= 2 if guess in vowels else 1

        print("------")

    print("Sorry, you ran out of guesses. The word was", secret_word)




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = False
    hangman(secret_word, with_help)

    pass

