import random
from decimal import Decimal


""" Exercise 1: Guessing Game """
# WORDS = [one_word.strip() for one_word in open('words.txt')]


def guessing_game(chances):
    """ Guessing Game """
    answer = random.randint(0, 100)
    remaining_guesses = chances - 1
#    required_base = random.choice([2, 8, 10, 16])  # binary/octal/decimal/hex
#    answer = random.choice(WORDS)

    while remaining_guesses >= 0:
        remaining_guesses -= 1
        user_guess = int(input('What is your guess? '))
#        user_guess = int(input('What is your guess? '), required_base)

        if user_guess == answer:
            print(f'RIGHT! The answer is {user_guess}')
            break
        elif user_guess < answer:
            print(f'Your guess of {user_guess} is Too Low!')
        else:
            print(f'Your guess of {user_guess} is Too High!')
    else:
        print(f'Your {chances} chances are up!')


""" Exercise 2: Summing Numbers """


def my_sum(*numbers, start=0):
    """ Summing numbers """
    output = start
    for number in numbers:
        output += number
    return output


def mean(numbers):
    """ Mean of numbers """
    return sum(numbers) / len(numbers)


def summarize(words):
    """Accepts a list of strings.
    Returns a 3-element tuple containing three integers: (a) length of the shortest word,
    (b) length of the longest word, and (c) average word length. """
    word_lengths = [len(one_word) for one_word in words]
    return min(word_lengths), max(word_lengths), sum(word_lengths)/len(word_lengths)


def is_intable(one_item):
    try:
        int(one_item)
        return True
    except ValueError:
        return False


def sum_intable(items):
    """Accepts a list of Python objects. Sums those objects that are integers or can be turned into integers. """
    return sum(one_item for one_item in items if is_intable(one_item))


""" Exercise 3: Run Timing """


def run_timing():
    """Asks the user repeatedly for numeric input. Prints the average time and number of runs. """
    number_of_runs = 0
    total_time = 0

    while True:
        one_run = input('Enter 10 km run time: ')

        if not one_run:
            break

        number_of_runs += 1
        total_time += float(one_run)

    average_time = total_time / number_of_runs

    print(f'Average of {average_time}, over {number_of_runs} runs')


def before_after_dot(f, before, after):
    """Accepts a float, and two integers.
    Returns a float containing before digits preceding the decimal point,
    and after digits following the decimal point. """
    s = str(f)
    i = s.index('.')
    return s[i-before:i+after+1]


def decimal_add(first, second):
    """Accepts two strings, turns them into decimals, and returns a float representing the sum of these two. """
    return float(Decimal(first) + Decimal(second))


""" Exercise 4: Hexadecimal Output """


def hex_output():
    """Ask the user to enter a valid hexadecimal number, and print the decimal equivalent. """
    dec_num = 0
    hex_num = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hex_num)):
        dec_num += int(digit, 16) * (16 ** power)
    print(dec_num)


def ord_hex_output():
    """Get a hex number to convert. Use ord to turn it into an integer, and print the decimal equivalent. """
    dec_num = 0
    hex_num = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hex_num)):
        if 48 <= ord(digit) <= 57:
            dec_digit = ord(digit) - 48
        elif 97 <= ord(digit) <= 102:
            dec_digit = ord(digit) - 87

        dec_num += dec_digit * (16 ** power)
    print(dec_num)


def name_triangle():
    """Get the user's name. Print a name triangle, starting with the first letter, then the first two letters, etc. """
    name = input("Enter your name: ")

    for i in range(len(name)):
        print(name[:i+1])


""" Exercise 1 """
# guessing_game(5)


""" Exercise 2 """
print(my_sum(10, 20, 30, 40))
print(mean([60, 40, 30, 90]))
print(summarize(["Can", "Seran", "Ayana"]))


""" Exercise 3 """


""" Exercise 4 """
