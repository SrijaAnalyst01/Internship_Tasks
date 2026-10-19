# Problem 2: The Captain's Room
# HackerRank Link: https://www.hackerrank.com/challenges/py-the-captains-room/problem
from collections import Counter
k=int(input())
room_numbers=list(map(int,input().split()))
counts=Counter(room_numbers)
for room,count in counts.items():
    if count==1:
        print(room)
        break
