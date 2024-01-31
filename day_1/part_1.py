#!/usr/bin/env python3

"""Advent of Code 2023 Question 1: Part 1"""

import re
import sys
import argparse

sys.path.append("..")
from utils.utils import file_to_list


def findCalibrationVal(elements: str) -> int:
    
    result = re.findall(r"[0-9]", elements)
    return int(result[0] + result[-1])


    

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


    
     


