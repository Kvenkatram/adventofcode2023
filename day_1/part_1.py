#!/usr/bin/env python3

"""Advent of Code 2023 Question 1: Part 1"""

import sys
import argparse

sys.path.append("..")
from utils.utils import file_to_list


def findCalibrationVal(string: str) -> int:
    
    first_digit = None
    second_digit = None
    
    fwrd_ptr = 0
    bckwd_ptr = len(string) - 1

    while first_digit == None:
        if string[fwrd_ptr].isdigit():
            first_digit = string[fwrd_ptr]
        else:
            fwrd_ptr += 1
    
    while second_digit == None:
        if string[bckwd_ptr].isdigit():
            second_digit = string[bckwd_ptr]
        else:
            bckwd_ptr -= 1
    
    val = first_digit + second_digit

    return int(val)


    

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    file_lines = file_to_list(args.file)

    sum = 0
    for line in file_lines:
        val = findCalibrationVal(line)
        sum += val

    print(sum)


    
     


