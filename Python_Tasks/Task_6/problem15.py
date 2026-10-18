# Problem 15: Set .difference() Operation
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-difference-operation/problem

n=input()
english_sub=set(map(int,input().split()))
m=input()
french_subs=set(map(int,input().split()))
only_eng=english_sub.difference(french_subs)
print(len(only_eng))
