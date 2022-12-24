from random import randint


MAX_NUM = 100
GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_prime_question():
    random_number = randint(0, MAX_NUM)
    question = random_number
    if is_prime(random_number):
        answer = 'yes'
    else:
        answer = 'no'
    question_and_answer = (question, answer)
    return question_and_answer


def is_prime(number):
    if number <= 1:  # Negative numbers can't be prime
        return False
    # We divide the number by the range to the number itself
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
