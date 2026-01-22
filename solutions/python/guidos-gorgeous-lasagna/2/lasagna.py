"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40 
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    bake_time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return bake_time_remaining

def preparation_time_in_minutes(number_of_layers):
    """Return preparation time in minutes.

    This function takes the number of layers & multiplies by minutes per layer
    """
    preparation_time = number_of_layers * PREPARATION_TIME
    return preparation_time

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    elapsed_prep_time = preparation_time_in_minutes(number_of_layers)
    elapsed_time_in_minutes = elapsed_prep_time + elapsed_bake_time
    return elapsed_time_in_minutes
    