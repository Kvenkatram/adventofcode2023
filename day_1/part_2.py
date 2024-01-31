#!/usr/bin/env python3

"""Advent of Code 2023 Question 1: Part 2"""
import re
import sys
import argparse

sys.path.append("..")
from utils.utils import file_to_list


def find_calibration_value(elements: str) -> int:

    values = {
        "one": "1", 
        "two": "2", 
        "three": "3", 
        "four": "4", 
        "five": "5", 
        "six": "6", 
        "seven": "7", 
        "eight": "8", 
        "nine": "9"
        }
    digits = []
    for index, item in enumerate(elements):
        if item.isdigit():
            digits.append(item)
        else:
            for key in values.keys():
                if elements[index:].startswith(key):
                    digits.append(values[key])

    return int(digits[0]+digits[-1])




if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    file_lines = file_to_list(args.file)

    sum = 0
    for line in file_lines:
        val = find_calibration_value(line)
        print (f"{sum} + {val} = {sum+val}")
        sum += val
    
    print(sum)


    
     


