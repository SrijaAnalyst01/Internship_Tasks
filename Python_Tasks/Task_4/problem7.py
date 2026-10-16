# Problem 1: String Split and Join
# HackerRank Link: https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    split=line.split(" ")
    join="-".join(split)
    return join
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
