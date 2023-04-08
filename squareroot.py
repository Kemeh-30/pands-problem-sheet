# squareroot.py
# Author : Adedoyinsola Fifo


def sqrt(num):
    if num < 0:
             return None

    
    lower_bound = 0.0
    upper_bound = num

    while upper_bound - lower_bound > 0.0001:
        mid_point = (lower_bound + upper_bound) / 2.0
        if mid_point**2 < num:
            lower_bound = mid_point
        else:
            upper_bound = mid_point

    return (lower_bound + upper_bound) / 2.0
