# Problem 1: Set .symmetric_difference() Operation
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
n1=int(input())
a=set(map(int,input().split()))
n2=int(input())
b=set(map(int,input().split()))

print(len(a.symmetric_difference(b)))
