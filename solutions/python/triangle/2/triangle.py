def equilateral(sides):
    if not is_valid_triangel(sides):
        return False
    side_a, side_b, side_c = sides

    if any(side <= 0  for side in sides):
        return False

    return side_a == side_b == side_c


def isosceles(sides):
    if not is_valid_triangel(sides):
        return False
    side_a, side_b, side_c = sides

    if any(side <= 0  for side in sides):
        return False
        
    return side_a == side_b or side_b == side_c or side_a == side_c


def scalene(sides):
    if not is_valid_triangel(sides):
        return False
    side_a, side_b, side_c = sides

    if any(side <= 0  for side in sides):
        return False
        
    return side_a != side_b and side_b != side_c and side_a != side_c

def is_valid_triangel(sides):
    side_a, side_b, side_c = sides
    if any(side <= 0 for side in sides):
        return False

    return (
        side_a + side_b >= side_c and
        side_a + side_c >= side_b and 
        side_b + side_c >= side_a
    )