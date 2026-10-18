# Problem 13: Set .union() Operation
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-union/problem
n=int(input())
eng=set(map(int,input().split()))
m=int(input())
french=set(map(int,input().split()))
sub1=eng.union(french)
print(len(sub1))
