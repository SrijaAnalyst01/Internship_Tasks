# Problem 20: No Idea!
# HackerRank Link: https://www.hackerrank.com/challenges/no-idea/problem
a,b=map(int,input().split())
arr=input().split()
set_a=set(input().split())
set_b=set(input().split())
result=sum((1 if num in set_a else -1 if num in set_b else 0) for num in arr)
print(result)

