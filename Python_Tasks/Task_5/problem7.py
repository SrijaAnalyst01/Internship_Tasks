# Problem 7: Symmetric Difference
# HackerRank Link: https://www.hackerrank.com/challenges/symmetric-difference/problem
m_size=int(input())
set_a=set(map(int,input().split()))
n_size=int(input())
set_b=set(map(int,input().split()))
symmetric_diff=set_a.symmetric_difference(set_b)
for i in sorted(symmetric_diff):
    print(i)
