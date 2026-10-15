#Q1. Find the Frequency of Each Word in a Sentence
from solutions import freq
sentence1="python easy and python is powerful"
print(freq(sentence1))

# Additional test case
sentence1="sql is useful and sql is easy to learn"
print(freq(sentence1))
#----------------------------------------------------------------------------------------------
#Q2. Find the Frequency of Each Character in a Word
from solutions import char_freq
word="banana"
print(char_freq(word))

# Additional test case
word="canada"
print(char_freq(word))
#----------------------------------------------------------------------------------------------
#Q3. Find the First Non-Repeating Character in a Word
from solutions import first_non_repeating
word="swiss"
print(first_non_repeating(word))

# Additional test case
word="aadhya"
print(first_non_repeating(word))
#----------------------------------------------------------------------------------------------
#Q4. Check Whether Two Strings Are Anagrams
from solutions import anagram
print(anagram("listen","silent"))

# Additional test case
print(anagram("earth","heart"))
#----------------------------------------------------------------------------------------------
#Q5. Find the First Repeating Character in a String
from solutions import first_repeating
word1="programming"
print(first_repeating(word1))

# Additional test case
word1="sense"
print(first_repeating(word1))
#----------------------------------------------------------------------------------------------
#Q6. Move All Zeros to the End of a List
from solutions import list_of_nums
print(list_of_nums([0, 3, 0, 1, 2, 0, 4]))

# Additional test case
print(list_of_nums([0, 0, 5, 7, 0, 9, 0]))
#----------------------------------------------------------------------------------------------
#Q7. Find the Second Highest Distinct Number in a List
from solutions import second_largest_distinct
lst=[10, 20, 40, 30, 40, 20]
print(second_largest_distinct(lst))

# Additional test case
lst=[300,700,400,100,100,500]
print(second_largest_distinct(lst))
#----------------------------------------------------------------------------------------------
#Q8. Remove Duplicates Without Changing the Original Order.
from solutions import remove_duplicates
lst=[4,2,4,5,2,7,5]
print(remove_duplicates(lst))

# Additional test case
lst=[12,14,12,13,17,14]
print(remove_duplicates(lst))
#----------------------------------------------------------------------------------------------
#Q9. Find the Missing Number from 1 to N
from solutions import missing_nums
print(missing_nums([1,2,4,5,6],6))

# Additional test case
print(missing_nums([1,3,4],4))
#----------------------------------------------------------------------------------------------
#Q10. Find Two Numbers Whose Sum Equals a Target
from solutions import two_sum
nums=[2, 7, 11, 15]
target=9
print(two_sum(nums,target))

# Additional test case
nums=[3,10,5,9]
target=15
print(two_sum(nums,target))
#----------------------------------------------------------------------------------------------
#Q11. Find the Number Closest to Zero
from solutions import closest_to_zero
nums=[-8, -3, 2, 5, -2]
print(closest_to_zero(nums))

# Additional test case
nums=[6, -1, 1, -9, 3]
print(closest_to_zero(nums))
#----------------------------------------------------------------------------------------------
#Q12. Find Common Elements Between Two Lists
from solutions import common_elements
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
print(common_elements(list1,list2))

# Additional test case
list1 = [20, 30, 40, 50, 60]
list2 = [30, 40, 50, 60, 70]
print(common_elements(list1,list2))
#----------------------------------------------------------------------------------------------
#Q13. Rotate a List to the Right by K Positions
from solutions import rotate
nums = [1, 2, 3, 4, 5]
K = 2
print(rotate(nums,K))

# Additional test case
nums = [13,16,7,14,20]
K = 3
print(rotate(nums,K))
#----------------------------------------------------------------------------------------------
#Q14. Find the Maximum Sum of Two Consecutive Elements
from solutions import max_consecutive_sum
nums=[4, 7, 2, 9, 5]
print(max_consecutive_sum(nums))
# Additional test case
nums=[1, 2, 3, 4, 5]
print(max_consecutive_sum(nums))
#----------------------------------------------------------------------------------------------
#Q15. Find All Pairs of Numbers Whose Sum Equals a Target
from solutions import all_pairs
nums = [2, 4, 3, 5, 7, 8, 1]
target = 9
print(all_pairs(nums,target))
# Additional test case
nums = [1,1,2,2,3,4]
target = 5
print(all_pairs(nums,target))