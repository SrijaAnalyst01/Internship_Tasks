# Problem 20: Piling Up!
# HackerRank Link: https://www.hackerrank.com/challenges/piling-up/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
def run():
    lines=sys.stdin.read().splitlines()
    if not lines:
        return
    t = int(lines[0])
    idx=1
    
    for _ in range(t):
        n=int(lines[idx])
        arr=[int(x) for x in lines[idx + 1].split()]
        idx+=2
        
        i=0
        j=n-1
        m=float("inf")
        ok=True
        
        while i<=j:
            if arr[i]>=arr[j]:
                v=arr[i]
                i+=1
            else:
                v=arr[j]
                j-=1
                
                if v>m:
                    ok=False
                    break
                    
                m=v
        if ok:
            print('Yes')
        else:
            print("No")

if __name__=="__main__":
    run()
                    
