# Problem 14: Symmetric Difference
# HackerRank Link: https://www.hackerrank.com/challenges/symmetric-difference/problem

n=int(input())
country_set=set()
for _ in range(n):
    country_set.add(input().strip())

print(len(country_set))
