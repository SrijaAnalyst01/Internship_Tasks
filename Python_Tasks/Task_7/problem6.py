# Problem 6: Pangrams
# HackerRank Link: https://www.hackerrank.com/challenges/pangrams/problem

import math
import os
import random
import re
import sys

def pangrams(s):
    s=s.lower()
    unique_letters=set(char for char in s if char.isalpha())
    if len(unique_letters)==26:
        return "pangram"
    else:
        return "not pangram"
         
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
