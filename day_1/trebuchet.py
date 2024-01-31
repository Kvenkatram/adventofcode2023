#!/usr/bin/env python3

"""Advent of Code 2023 Question 1"""

import re
import sys
import argparse

sys.path.append("..")
from utils.utils import file_to_list


def part1(file_lines: list) -> int:
    
    sum = 0
    for line in file_lines:
        result = re.findall(r"[0-9]", line)
        sum += int(result[0] + result[-1])
    return sum


def part2(file_lines: list) -> int:
    
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
    sum = 0
    for line in file_lines:
        digits = []
        for index, item in enumerate(line):
            if item.isdigit():
                digits.append(item)
            else:
                for key in values.keys():
                    if line[index:].startswith(key):
                        digits.append(values[key])

        sum += int(digits[0]+digits[-1])
    return sum

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    file_lines = file_to_list(args.file)

    print(f"Part 1 answer: {part1(file_lines)}")
    print(f"Part 2 answer: {part2(file_lines)}")


    
     


