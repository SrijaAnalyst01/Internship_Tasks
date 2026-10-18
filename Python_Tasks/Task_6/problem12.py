# Problem 12: Set .discard(), .remove() & .pop()
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
n = int(input())
s = set(map(int, input().split()))
num_commands=int(input())

for _ in range(num_commands):
    command=input().split()
    name=command[0]
    
    if name=="pop":
        s.pop()
    else:
        val=int(command[1])
        getattr(s,name)(val)
print(sum(s))
