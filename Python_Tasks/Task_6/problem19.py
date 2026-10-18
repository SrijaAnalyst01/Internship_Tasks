# Problem 19: Company Logo
# HackerRank Link: https://www.hackerrank.com/challenges/most-commons/problem
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()

    letter_counts={}
    for character in s:
        letter_counts[character]=letter_counts.get(character,0)+1
    
    ordered_rankings=sorted(letter_counts.items(),key=lambda kv: (-kv[1],kv[0]))
    for idx in range(3):
        target_char,count=ordered_rankings[idx]
        print(f"{target_char} {count}")
        
