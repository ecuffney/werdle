import random
import time
from random_words import words
from werdle_standard import play_werdle_std
from werdle_easy import play_werdle_easy
from werdle_hard import play_werdle_hard

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(3)

def choose_level():
    askLevel= input('\nWelcome to Werdle! Type 1, 2, or 3 to choose your difficulty level.\n'
           '\n 1. EASY - Guess the 5 letter word: Unlimited guesses.\n '
           '2. STANDARD - Guess the 5 letter word: 5 guesses.\n'
           ' 3. HARD- Guess the 6 letter word: 6 guesses.\n')
    if askLevel == '1':
        print_pause('Loading Werdle level: EASY')
        play_werdle_easy()
    elif askLevel == '2':
        print_pause('Loading Werdle level: STANDARD')
        play_werdle_std()
    elif askLevel == '3':
        print_pause('Loading Werdle level: HARD')
        play_werdle_hard()
    else:
        print('Please enter 1, 2, or 3.')
        choose_level()

if __name__ == '__main__':
    choose_level()
