# Problem 15: Game of Thrones - I
# HackerRank Link: https://www.hackerrank.com/challenges/game-of-thrones/problem
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
def gameOfThrones(s):
    s=s.strip()
    char_counts=Counter(s)
    odd_counts=sum(1 for count in char_counts.values() if count%2!=0)
    if odd_counts<=1:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
