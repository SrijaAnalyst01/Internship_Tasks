# Problem 7: Alphabet Rangoli
# HackerRank Link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    import string
    chars = string.ascii_lowercase
    width=4*size-3
    lines=[]
    for i in range(size):
        left=[chars[j] for j in range(size - 1, i-1,-1)]
        r=left+left[:-1][::-1]
        s="-".join(r) 
        lines.append(s.center(width,"-"))
    rangoli=lines[::-1]+lines[1:]
    print("\n".join(rangoli))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
