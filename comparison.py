""" This file is part of the File I/O exercise.

It should be used with the two input files, fruits_1.txt and fruits_2.txt."""

def open_and_read_file(filename):
    """Opens file as a file object and returns list of contents."""

    # Write your code below.


    fruit_file = open(filename)
    make_list = fruit_file.read().strip()
    print make_list.split("\n")


def compare(lst1, lst2):
    """Takes in two lists and returns a list of items in common. """

    # Write your code below.


    pass



open_and_read_file("fruits_1.txt")
open_and_read_file("fruits_2.txt")