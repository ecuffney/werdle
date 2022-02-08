import random
from random_words import words

def valid_choice(words):
    word= random.choice(words)
    while '-' in word or ' ' in word or len(word) != 6:
        word= random.choice(words)
    return word.upper()

def valid_input(prompt):
    cons = "bcdfghjklmnpqrstvwxyz".upper()
    while True:
        ask = input(prompt).upper()
        vtest = any(i in ask for i in cons)
        if vtest == False:
            print('\n** Nice try! You must enter a real word.\n')
        elif len(ask) > 6:
            print('\n** Too many letters!\n')
        elif len(ask) < 6:
            print('\n** Not enough letters!\n')
        elif ask.isalpha() == False:
            print('\n** Your word contains a non-letter.\n')
        else:
            print(f'Your word: {ask}\n')
            return ask
    return ask

def play_again():
    again = input('Would you like to play again? y/n ?\n ').lower()
    if again == 'y':
        play_werdle_hard()
    elif again == 'n':
        print('Ok, bye!')
        exit()
    else:
        print("Please enter y or n.")
        play_again()

def intro():
    print('------------------------------------------------------------'
            '--------------------'
            '\nWelcome to Werdle! You have 6 chances to guess'
           ' the correct 6 letter word.\n'
            '\n *Any correct letter in the right place will '
            'replace a _ in the word.\n'
            '\n *All correct letters listed are somewhere in the word.\n'
            '\n *All incorrect letters listed are not in the word.\n'
            '\n GOOD LUCK!\n'
            '------------------------------------------------------------'
            '--------------------')

def play_werdle_hard():
    word= valid_choice(words)
    rightLetter= set()
    wrongLetter= set()
    lives = 6
    intro()
    while lives > 0:
        guess = valid_input('Please choose a 6 letter word: ')
        lives = lives -1
        if guess == word:
            print(f'\n*** CORRECT!!!The word is {word} ***\n ')
            play_again()
        for i in guess:
            if i in guess and i in word:
                rightLetter.add(i)
            else:
                wrongLetter.add(i)
        for i, x in enumerate(word):
            letter = guess[i]
            if letter == x:
                print(letter, end= ' ')
            elif letter != x:
                 print('-', end= ' ')
            else:
                print('Sorry no letters from that word match.')

        print(f'\nCorrect letters: {rightLetter}')
        print(f'\nWrong letters: {wrongLetter}\n')
        print(f'~~You have {lives} chances left~~\n')
        print('------------------------------------------------------------'
        '--------------------')

    if lives == 0:
        print(f'\nNo more guesses, sorry. The word was {word}.\n')
        play_again()


if __name__ == '__main__':
    play_werdle_hard()
