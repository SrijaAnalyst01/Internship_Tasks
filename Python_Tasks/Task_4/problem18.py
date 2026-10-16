# Problem 18: Lists
# HackerRank Link: https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    my_list=[]
    for _ in range(N):
        parts=input().split()
        commands=parts[0]
        
        if commands=="insert":
            index=int(parts[1])
            elements=int(parts[2])
            my_list.insert(index,elements)
        elif commands=="print":
            print(my_list)
        elif commands=="remove":
            elements=int(parts[1])
            my_list.remove(elements)
        elif commands=="append":
            elements=int(parts[1])
            my_list.append(elements)
        elif commands=="sort":
            my_list.sort()
        elif commands=="pop":
            my_list.pop()
        elif commands=="reverse":
            my_list.reverse()
