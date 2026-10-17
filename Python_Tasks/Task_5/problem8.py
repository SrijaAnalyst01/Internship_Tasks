# Problem 8: Set .add()
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-add/problem
n=int(input())
country_set=set()
for _ in range(n):
    country_set.add(input().strip())
print(len(country_set))
