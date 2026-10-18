# Problem 16: Check Subset
# HackerRank Link: https://www.hackerrank.com/challenges/py-check-subset/problem
import sys
def check_subset():
    input_data=sys.stdin.read().splitlines()

    if not input_data:
        return
    num_test=int(input_data[0])
    
    m=1
    for _ in range(num_test):
        _=int(input_data[m])    
        
        a=set(map(int,input_data[m+1].split()))
        _=int(input_data[m+2])
        
        b=set(map(int,input_data[m+3].split()))
        print(a.issubset(b))
        m+=4
if __name__=="__main__":
    check_subset()
        
