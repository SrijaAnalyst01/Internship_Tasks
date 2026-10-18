# Problem 8: Tuples
# HackerRank Link: https://www.hackerrank.com/challenges/python-tuples/problem
import sys

def deterministic_tuple_hash(elements):
   
    BIT_MASK = 0xFFFFFFFFFFFFFFFF
    current_multiplier = 1000003
    hash_accumulator = 0x345678
    total_elements = len(elements)
    
    for idx, item in enumerate(elements):
        hash_accumulator = ((hash_accumulator ^ item) * current_multiplier) & BIT_MASK
        remaining_elements = total_elements - 1 - idx
        current_multiplier = (current_multiplier + 82520 + 2 * remaining_elements) & BIT_MASK
        
    hash_accumulator = (hash_accumulator + 97531) & BIT_MASK

    if hash_accumulator >= 0x8000000000000000:
        hash_accumulator -= 0x10000000000000000
        
    return -2 if hash_accumulator == -1 else hash_accumulator

if __name__ == '__main__':
    _ = input()

    numbers = [int(val) for val in input().split()]

    print(deterministic_tuple_hash(numbers))

    

