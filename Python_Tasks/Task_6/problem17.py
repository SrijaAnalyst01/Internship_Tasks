# Problem 17: Check Strict Superset
# HackerRank Link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem
def check_superset():
    a=set(map(int,input().split()))
    num=int(input())
    for _ in range(num):
        b=set(map(int,input().split()))
        c=b.issubset(a) and len(a)>len(b)
        
        if not c:
            print(False)
            return
    print(True)
if __name__=="__main__":
    check_superset()
