# Problem 12: Making Anagrams
# HackerRank Link: https://www.hackerrank.com/challenges/making-anagrams/problem

import math
import os
import random
import re
import sys
from collections import Counter
def makingAnagrams(s1, s2):
    a = Counter(s1)
    b = Counter(s2)
    delete = 0
    
    result=set(a.keys()).union(set(b.keys()))
    
    for char in result:
        delete += abs(a.get(char,0) - b.get(char,0))
    return delete
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
