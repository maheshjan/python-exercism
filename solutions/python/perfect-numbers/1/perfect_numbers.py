def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    param_number = 0
    for i in range(1, number):
        if number % i == 0:
            param_number += i

    if param_number == number:
        return "perfect"

    if param_number > number:
        return "abundant"

    if param_number < number:
        return "deficient"
        
