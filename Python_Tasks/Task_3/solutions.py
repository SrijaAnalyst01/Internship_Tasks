#Q1. Find the Frequency of Each Word in a Sentence

def freq(sentence):
    frequency={}

    for i in sentence.split():
        if i in frequency:
            frequency[i]+=1
        else:
            frequency[i]=1
    return frequency

#----------------------------------------------------------------------------------------------
#Q2. Find the Frequency of Each Character in a Word
def char_freq(word):
    frequency1={}
    for char in word:
        if char in frequency1:
            frequency1[char]+=1
        else:
            frequency1[char]=1
    return frequency1

#----------------------------------------------------------------------------------------------
#Q3. Find the First Non-Repeating Character in a Word
def first_non_repeating(word):
    frequency=char_freq(word)
    for char in word:
        if frequency[char]==1:
            return char
    return None

#----------------------------------------------------------------------------------------------
#Q4. Check Whether Two Strings Are Anagrams
def anagram(s1,s2):
    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()
    return char_freq(s1)==char_freq(s2)

#----------------------------------------------------------------------------------------------
#Q5. Find the First Repeating Character in a String
def first_repeating(word1):
    word=word1.replace(" ","").lower()
    fir_char=set()
    for char in word:
        if char in word:
            return char
        else:
            fir_char.add(char)
        return None

#----------------------------------------------------------------------------------------------
#Q6. Move All Zeros to the End of a List
def list_of_nums(nums):
    non_zeros=[]
    for num in nums:
        if num!=0:
            non_zeros.append(num)

    zero_num=len(nums)-len(non_zeros)

    return non_zeros+[0]*zero_num

#----------------------------------------------------------------------------------------------
#Q7. Find the Second Highest Distinct Number in a List
def second_largest_distinct(lst):
    unique_nums=set(lst)
    if(len(unique_nums)<2):
        return None
    return sorted(unique_nums)[-2]

#----------------------------------------------------------------------------------------------
#Q8. Remove Duplicates Without Changing the Original Order.
def remove_duplicates(lst):
    list1=set()
    result=[]

    for item in lst:
        if item not in list1:
            list1.add(item)
            result.append(item)
    return result

#----------------------------------------------------------------------------------------------
#Q9. Find the Missing Number from 1 to N
def missing_nums(nums,n):
    expected_sum=n*(n+1)/2
    actual_sum=sum(nums)

    return int(expected_sum - actual_sum)

#----------------------------------------------------------------------------------------------
#Q10. Find Two Numbers Whose Sum Equals a Target
def two_sum(nums, target):
    s=set()

    for num in nums:
        required_num=target-num

        if required_num in s:
            return [required_num,num]

        s.add(num)
    return []
#----------------------------------------------------------------------------------------------
#Q11. Find the Number Closest to Zero
def closest_to_zero(nums):
    if not nums:
        return None
    return min(nums,key=lambda num:(abs(num),-num))

#----------------------------------------------------------------------------------------------
#Q12. Find Common Elements Between Two Lists
def common_elements(list1,list2):
    s=set(list2)
    result=[]
    s1=set()

    for num in list1:
        if num in s and num not in s1:
            result.append(num)
            s1.add(num)
    return result
#----------------------------------------------------------------------------------------------
#Q13. Rotate a List to the Right by K Positions
def rotate(nums,K):
    if not nums:
        return []
    K=K%len(nums)
    return nums[-K:]+nums[:-K] if K else nums[:]
#----------------------------------------------------------------------------------------------
#Q14. Find the Maximum Sum of Two Consecutive Elements
def max_consecutive_sum(nums):
    max_sum=nums[0]+nums[1]

    for i in range(1,len(nums)-1):
        current_sum=nums[i]+nums[i+1]

        if current_sum>max_sum:
            max_sum=current_sum
    return max_sum
#----------------------------------------------------------------------------------------------
#Q15. Find All Pairs of Numbers Whose Sum Equals a Target
def all_pairs(nums,target):
    pairs=set()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                pair=tuple(sorted((nums[i],nums[j])))
                pairs.add(pair)
    return [list(pair) for pair in sorted(pairs)]

