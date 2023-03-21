from random import randint


def fortune_teller():
    rand_number = randint(1, 10)
    if rand_number == 5:
        return "Your're going to die someday"
    return "Your're going to live forever"
