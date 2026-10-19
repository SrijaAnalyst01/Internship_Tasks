# Problem 3: Mars Exploration
# HackerRank Link: https://www.hackerrank.com/challenges/mars-exploration/problem

import math
import os
import random
import re
import sys

def marsExploration(s):
    # Write your code here
    altered_count=0
    for i in range(len(s)):
        if i%3==0 or i%3==2:
            if s[i]!="S":
                altered_count+=1
        elif i%3==1:
            if s[i]!="O":
                altered_count+=1
    return altered_count
