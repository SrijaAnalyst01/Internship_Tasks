# Problem 15: Word Order
# HackerRank Link: https://www.hackerrank.com/challenges/word-order/problem
import sys

def solve():
    input_data=sys.stdin.read().splitlines()
    if not input_data:
        return
    n=int(input_data[0])
    
    word_count={}
    for i in range(1,n+1):
        word=input_data[i].strip()
        if word:
            word_count[word]=word_count.get(word,0)+1
            
    print(len(word_count))
    print(*(word_count.values()))
if __name__=="__main__":
    solve()
