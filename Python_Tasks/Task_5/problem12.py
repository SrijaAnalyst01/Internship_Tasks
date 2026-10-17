# Problem 12: Capitalize!
# HackerRank Link: https://www.hackerrank.com/challenges/capitalize/problem

def solve(s):
    words=s.split(" ")
    capitalized_words=[word.capitalize() for word in words]
    return " ".join(capitalized_words)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
