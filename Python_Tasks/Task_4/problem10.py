# Problem 10: Find a String
# HackerRank Link: https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    count=0
    start=0
    while True:
        start=string.find(sub_string,start)
        if start==-1:
            break
        count+=1
        start+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
