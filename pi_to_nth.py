#! /usr/bin/env python3

import math, sys

def pi_to(n):
    if n > 48:
        number_of_places = 48
        print("\nThe precision of pi in python is limited to 48 decimal places.\
            \nReturning the max representable size of pi:\n")
    else:
        number_of_places = n
    return "{:.{}f}".format(math.pi, number_of_places)

def main(n=7):
    try:
        a = pi_to(int(n))
        print(a)
    except ValueError as e:
        print("You need to enter an integer")
        print("Here is PI to 7 places:", pi_to(7))
        exit()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("Using default value of n (7)")
        main()