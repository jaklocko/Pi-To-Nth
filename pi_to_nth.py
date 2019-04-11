#! /usr/bin/env python3

'''
This program returns pi to the designated number of decimal places, truncating after 48, which is the maximum precision of pi in Python 3
It performs type checking on the arguments to ensure the value supplied is an integer
It ignores all non-integer arguments and returns a result for each valid integer argument
'''

import math, sys

def pi_to(n=7):
    if n > 48:
        number_of_places = 48
        print("\nThe precision of pi in python is limited to 48 decimal places.\
            \nReturning the max representable size of pi:\n")
    else:
        number_of_places = n
    return "pi to {} places: {:.{}f}".format(number_of_places, math.pi, number_of_places)

def parse_args(args):
    for arg in args[1:]:
        if not isinstance(arg, int):
            try:
                print(pi_to(int(arg)))
            except ValueError as e:
                print("\t{} is not castable as an integer".format(arg))
        else:
            print(pi_to(int(arg)))

if __name__ == '__main__':
    parse_args(sys.argv)