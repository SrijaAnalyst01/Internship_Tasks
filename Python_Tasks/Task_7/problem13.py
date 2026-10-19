# Problem 13: Sherlock and the Valid String
# HackerRank Link: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
import math
import os
import random
import re
import sys
from collections import Counter
def isValid(s):
    char_counts=Counter(s)
    freq_counts=Counter(char_counts.values())
    if len(freq_counts)==1:
        return "YES"
    if len(freq_counts)>2:
        return "NO"
    (f1,count1),(f2,count2)=freq_counts.items()
    if (f1==1 and count1==1) or (f2 ==1 and count2==1):
        return "YES"
    if (f1-f2==1 and count1==1) or (f2-f1==1 and count2==1):
        return "YES"
    return "NO"
    
if __name__=="__main__":
    fptr=open(os.environ["OUTPUT_PATH"],"w")
    s=input() 
    result=isValid(s)
    fptr.write(result+"\n")
    fptr.close()
