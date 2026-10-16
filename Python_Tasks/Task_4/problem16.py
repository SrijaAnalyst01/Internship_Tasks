# Problem 16: Nested Lists
# HackerRank Link: https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    unique_scores=sorted(list(set([score for name, score in students])))
    second_lowest_score=unique_scores[1]
    result_names=sorted([name for name,score in students if score == second_lowest_score])
    for name in result_names:
        print(name)
        
