# Problem 16: Collections.Counter()
# HackerRank Link: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter
if __name__=="__main__":
    shoe_number=int(input())
    shoe_sizes=list(map(int,input().split()))
    s=Counter(shoe_sizes)
    cust_num=int(input())
    total_earn=0
    for _ in range(cust_num):
        size,price=map(int,input().split())
        if s[size]>0:
            total_earn+=price
            s[size]-=1
    print(total_earn)
