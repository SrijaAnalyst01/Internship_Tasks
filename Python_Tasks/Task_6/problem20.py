# Problem 20: Validating the Phone Number
# HackerRank Link: https://www.hackerrank.com/challenges/validating-the-phone-number/problem
import sys
import re
def check_mobile_number():
    input_content = sys.stdin.read().splitlines()
    if not input_content:
        return
    total_records=int(input_content[0])
    validator=re.compile(r"^[789]\d{9}$")
    for idx in range(1,total_records+1):
        target_string=input_content[idx].strip()
        if validator.match(target_string):
            print("YES")
        else:
            print("NO")
    
if __name__=="__main__":
    check_mobile_number()
