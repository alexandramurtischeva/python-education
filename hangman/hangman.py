"""
This script realizes a fun game called hangman
"""

from random import choice
from ascii import stages, logo
from words import word_list

used_words = []
print(logo)


def menu() -> None:
    """This function navigates a player through the game"""
    print("""
                        Type 
                p - to start the game
                s - to see guessed words
                q - to exit hangman """)
    output = input().lower()
    if output == "p":
        play()
    elif output == "s":
        show_words(used_words)
    elif output == "q":
        game_over()
    else:
        print("Please type the correct letter.")
        menu()


def play() -> None:
    """
    Function that calls all needed functions to play hangman

    Variables:
        int: lives - stores amount lives that a player has;
        str: picked_word - receives a word that has to be guessed;
        list: hidden_word_list - stores and "hides "each letter of the picked_word in a list.
    """
    lives = 6
    picked_word = pick_word()
    record_word(picked_word)
    hidden_word_list = hide_word(picked_word)
    print_word(hidden_word_list)
    hangman(lives, hidden_word_list, picked_word)


def pick_word() -> str:
    """
    Randomly picks a word from words.py module

    Returns:
        str: a picked word to play the game
    """
    word_choice = choice(word_list)
    return word_choice


def record_word(word_to_record: str) -> None:
    """
    Appends a picked word to a global list used_word
    Args:
        word_to_record (str): a string that stores a word that has to be guessed
    """
    global used_words
    used_words.append(word_to_record)


def show_words(list_of_words: list) -> None:
    """
    Prints out words that were used while playing hangman.
    Redirects to a "menu"
    Args:
        list_of_words(list): a list of words that were shown to a player
    """
    if not list_of_words:
        print("You haven't tried to guess any words")
        menu()
    else:
        print("You have tried to guess such words:")
        for word in list_of_words:
            print(word)
        menu()


def hide_word(picked_word: str) -> list:
    """
    Creates a list that contains spaces worth of the length of the word
    Args:
        picked_word (str): a string that stores a word has to be guessed

    Returns:
        list: list of spaces that "hide" letters of picked_word
    """
    hidden_word = []
    for space in picked_word:
        hidden_word.append("_")
    print("You need to guess the word: ")
    return hidden_word


def print_word(word_to_print: list) -> None:
    """
    Prints out word_to_print.
    Args:
        word_to_print (list): contains a list whose elements have to be printed out
    """
    output = " ".join(word_to_print)
    print(output)


def game_over() -> None:
    """
    Cleans a global list used_words that stores all words that were used while playing.
    After that calls system function quit() that kills the playing session
    """
    global used_words
    used_words.clear()
    print("We are sorry to see you go...")
    quit()


def print_state(lives: int) -> None:
    """
    Prints out the amount of lives a player plays and a hangman.
    Args:
        lives (int): amount of lives/attempts a player has.
    """
    print(f"You have {lives} lives left")
    print(stages[lives])


def hangman(lives: int, hidden_word: list, picked_word: str) -> None:
    """
    Contains the main logic of the game. It considers such cases:
    1) A player doesn't guess any letter, then they lose a life
    2) A player mentions the same letter, they have guessed. They don't lose a life
    3) A player guesses a letter in a targeted word

    Args:
        lives (int): amount of lives/attempts a player has.
        hidden_word (list): list that contains spaces.
        picked_word (str): a targeted word.
    """
    while lives:
        print_state(lives)
        guess = input("Guess a letter: ").lower()
        # In case a player repeats a guessed letter
        if guess in hidden_word:
            print(f"You have already guessed {guess}.")
            print_word(hidden_word)
            continue
        # A player's guessed a letter
        elif guess in picked_word:
            random_encouragements = ["Yes!!! You got it right!", "Keep going!",
                                     "Well done!", "You are a hangman boss!", "You are good at this!"]
            print(choice(random_encouragements))
            for index, letter in enumerate(picked_word):
                if guess == letter:
                    hidden_word[index] = letter
            print_word(hidden_word)
        # A player's not guessed any letter
        else:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            print_word(hidden_word)
            lives -= 1
        # Check if all letters were guessed
        if "_" not in hidden_word:
            print("You win.")
            record_word(pick_word())
            break
        elif lives == 0:
            print(f"The word was {picked_word}")
            print("You lose.")

    print("Would you like to play again?")
    menu()


if __name__ == "__main__":
    menu()
