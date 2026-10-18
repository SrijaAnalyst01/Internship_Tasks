# Problem 14: Set .intersection() Operation
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
n= int(input())
eng_sub=set(map(int,input().split()))
m=int(input())
french_sub=set(map(int,input().split()))
combined=eng_sub.intersection(french_sub)
print(len(combined))
