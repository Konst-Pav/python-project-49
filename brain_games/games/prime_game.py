from random import randint


MAX_NUM = 100
GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_prime_question():
    random_number = randint(0, MAX_NUM)
    print(GAME_RULE)
    print(f'Question: {random_number}')
    return 'yes' if is_prime(random_number) else 'no'


def is_prime(number):
    if number <= 1:  # Negative numbers can't be prime
        return False
    # We divide the number by the range to the number itself
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
