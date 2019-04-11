#! /usr/bin/env python3

'''
This program returns PI to the designated number of decimal places, truncating after 48, which is the maximum precision of PI in Python 3
It performs type checking on the arguments to ensure the value supplied is an integer
It ignores all arguments past the first
'''

import math, sys

def pi_to(n):
    if n > 48:
        number_of_places = 48
        print("\nThe precision of pi in python is limited to 48 decimal places.\
            \nReturning the max representable size of pi:\n")
    else:
        number_of_places = n
    return "PI to {} places: {:.{}f}".format(number_of_places, math.pi, number_of_places)

def main(n=7):
    try:
        print(pi_to(int(n)))
    except ValueError as e:
        print("You need to enter an integer")
        print(pi_to(7))
        exit()

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        main(sys.argv[1])
    elif len(sys.argv) == 1:
        print("Using default value of n (7)")
        main()