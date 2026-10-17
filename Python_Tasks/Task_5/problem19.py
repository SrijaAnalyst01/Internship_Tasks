# Problem 19: Merge the Tools!
# HackerRank Link: https://www.hackerrank.com/challenges/merge-the-tools/problem
def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        s =string[i:i+k]
        t="".join(dict.fromkeys(s))
        print(t)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
