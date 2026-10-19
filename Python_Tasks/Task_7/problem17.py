# Problem 17: Separate the Numbers
# HackerRank Link: https://www.hackerrank.com/challenges/separate-the-numbers/problem
#!/bin/python3

import math
import os
import random
import re
import sys

def separateNumbers(s):
    if len(s)<=1 or s[0]=="0":
        print("NO")
        return
    for i in range(1,len(s)//2+1):
        first_num_str=s[:i]
        first_num=int(first_num_str)
        temp_str=first_num_str
        next_num=first_num
        while len(temp_str)<len(s):
            next_num+=1
            temp_str+=str(next_num)
        if temp_str==s:
            print(f"YES {first_num}")
            return
    print("NO")
    

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)

