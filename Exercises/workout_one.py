import random

""" Guessing Game"""
def guessing_game(remaining_guess):

    answer = random.randint(0, 100)
    remaining_guesses = remaining_guess - 1

    while remaining_guesses >= 0:
        remaining_guesses -= 1
        user_guess = int(input('What is your guess? '))

        if user_guess == answer:
            print(f'Right! The answer is {user_guess}')
            break
        elif user_guess < answer:
            print(f'Your guess of {user_guess} is Too Low!')
        else:
            print(f'Your guess of {user_guess} is Too High!')
    else:
        print(f'Your {remaining_guess} chances are up!')


guessing_game(5)
