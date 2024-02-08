import random
from typing import List, Set
from words import words
from hangman_visual import lives_visual_dict
import string


def get_valid_word(words: List[str]) -> str:
    """
    Selects a valid word for the Hangman game.

    Args:
        words (List[str]): A list of words from which to select.

    Returns:
        str: A valid word for the Hangman game.
    """
    word = random.choice(words)  
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    """Main function to play the Hangman game."""
    word = get_valid_word(words)
    word_letters = set(word)  
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  

    lives = 7

    while len(word_letters) > 0 and lives > 0:

        print(f"You have {lives} lives left and you have used these letters: {' '.join(used_letters)}")

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print(lives_visual_dict[lives])
        print(f"Current word: {' '.join(word_list)}")

        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')


if __name__ == '__main__':
    hangman()