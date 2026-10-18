# Problem 18: Set Mutations
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-mutations/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def process_mutations():
    raw_lines=sys.stdin.read().splitlines()
    if not raw_lines:
        return
    main_collection=set(map(int,raw_lines[1].split()))
    line_ptr=3
    total_commands=int(raw_lines[2])
    actions={
        "update":lambda s,o:s.update(o), 
        "intersection_update":lambda s,o: s.intersection_update(o), 
        "difference_update":lambda s,o:s.difference_update(o), 
        "symmetric_difference_update": lambda s,o: s.symmetric_difference_update(o) 
        
    }
    for _ in range(total_commands):
        cmd=raw_lines[line_ptr].split()[0]
        payload=set(map(int,raw_lines[line_ptr+1].split()))
        actions[cmd](main_collection,payload)
        line_ptr+=2
    grand_total=0
    for element in main_collection:
        grand_total+=element
    print(grand_total)
if __name__=="__main__":
    process_mutations()
