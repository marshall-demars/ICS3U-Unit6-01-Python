#!/usr/bin/env python3

# Created by: Marshall Demars 
# Created on: Dec 2022
# This program finds the average of 10 random numbers using arrays

import random


def main():
    # this function uses an array

    random_numbers = []

    # input
    for loop_counter in range(0, 10):
        single_random_number = random.randint(0, 100)
        random_numbers.append(single_random_number)

    for loop_counter in range(0, 10):
        print("The random number is: {0}".format(random_numbers[loop_counter]))
    average = sum(random_numbers) / len(random_numbers)
    print("\nThe average is {0}".format(average))

    print("\nDone.")


if __name__ == "__main__":
    main()
