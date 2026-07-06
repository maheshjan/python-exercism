"""
Module: is for check the triangle values. 
"""

def equilateral(sides):
    """ 
    to check all sides are equal
    """
    if not is_valid_triangel(sides):
        return False
    side_a, side_b, side_c = sides

    if any(side <= 0  for side in sides):
        return False

    return side_a == side_b == side_c


def isosceles(sides):
    """
    To check one side equal to one of the other side
    """
    if not is_valid_triangel(sides):
        return False
    side_a, side_b, side_c = sides

    if any(side <= 0  for side in sides):
        return False
        
    return side_a == side_b or side_b == side_c or side_a == side_c


def scalene(sides):
    """
    To check one side not equal to any one other side
    """
    if not is_valid_triangel(sides):
        return False
    side_a, side_b, side_c = sides

    if any(side <= 0  for side in sides):
        return False
        
    return side_a != side_b and side_b != side_c and side_a != side_c

def is_valid_triangel(sides):
    """
    To check the side values are not zero .
    To check sum of two side is greater than other side. 
    """
    side_a, side_b, side_c = sides
    if any(side <= 0 for side in sides):
        return False

    return (
        side_a + side_b >= side_c and
        side_a + side_c >= side_b and 
        side_b + side_c >= side_a
    )