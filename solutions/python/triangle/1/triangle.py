def equilateral(sides):
    if not is_valid_triangel(sides):
        return False
    a, b, c = sides

    if any(side <= 0  for side in sides):
        return False

    return a == b == c


def isosceles(sides):
    if not is_valid_triangel(sides):
        return False
    a, b, c = sides

    if any(side <= 0  for side in sides):
        return False
        
    return a == b or b == c or a == c


def scalene(sides):
    if not is_valid_triangel(sides):
        return False
    a, b, c = sides

    if any(side <= 0  for side in sides):
        return False
        
    return a != b and b != c and a != c

def is_valid_triangel(sides):
    a, b, c = sides
    if any(side <= 0 for side in sides):
        return False

    return (
        a + b >= c and
        a + c >= b and 
        b + c >= a
    )