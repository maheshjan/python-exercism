"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.

EXPECTED_BAKE_TIME = 40


#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(actual_minutes):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remaining_time = EXPECTED_BAKE_TIME - actual_minutes
    return remaining_time


#TODO (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the prepation time.

    Parameters:
        prepartion time: preparation time of each layer

    Returns:
        int: preparation time in (int)

    Funtion that takes number of layers and then multiple with 2
    """
    preparation_time = number_of_layers * 2
    return preparation_time
    


#TODO (student): define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time.

    Parameters:
        number of layers: total number of layers
        elapsed bake time: preparation time + elapsed bake time

    Returns:
        int: elapsed time by adding preparation time and elapsed bake time.

    Funtion that takes number of layers and elapsed bake time as input and then calculate the elapsed time in minutes.
    """
    elapsed_time = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return elapsed_time
    


# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)