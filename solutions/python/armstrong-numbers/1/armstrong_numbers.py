def is_armstrong_number(number):
    digits = list(str(number))
    number_of_digits = len(digits)
    total_sum = 0
    for i in digits:
        total_sum += int(i) ** number_of_digits
    if total_sum == number:
        return True
    else: return False
