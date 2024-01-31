#!/usr/bin/env python3

""" General purpose functions for Advent of Code Problems"""


def file_to_list(filename: str) -> list:
    """ 
    Read in a file.
    Return a list where list[X] contains the X'th line of the file.
    """

    data = []
    with open(filename) as file:
        for line in file:

            data.append(line.strip())
    return data



