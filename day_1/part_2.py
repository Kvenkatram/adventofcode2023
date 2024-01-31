#!/usr/bin/env python3

"""Advent of Code 2023 Question 1: Part 2"""
import re
import sys
import argparse

sys.path.append("..")
from utils.utils import file_to_list


def find_calibration_value(elements: str) -> int:

    result = re.findall(r"[0-9]|one|two|three|four|five|six|seven|eight|nine", elements)

    val = [result[0], result[-1]]
    for index, item in enumerate(val):
        if item == "one":
            val[index] = '1'
        elif item == "two":
            val[index] = '2'
        elif item == "three":
            val[index] = '3'
        elif item == "four":
            val[index] = '4'
        elif item == "five":
            val[index] = '5'
        elif item == "six":
            val[index] = '6'
        elif item == "seven":
            val[index] = '7'
        elif item == "eight":
            val[index] = '8'
        elif item ==  "nine":
            val[index] = '9'
    
    
    return int(val[0] + val[1])
    




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


    
     


