#Q12. You are given a string. Find the longest substring without repeating characters.
#Input : "abcabcbb"
#Output: "abc" (length 3)
#Input : "pwwkew"
#Output: "wke" (length 3)
#Input : "aaaa"
#Output: "a" (length 1)
#Input : ""
#Output: "" (length 0)

#def longest_substring(s):
#    longest = ""

#    for i in range(len(s)):
#        current = ""

#        for j in s[i:]:
#            if j in current:
#                break
#            current += j

#        if len(current) > len(longest):
#            longest = current

#    return longest


#print(longest_substring("abcabcbb"))

# Q11. You are given a list of words. Group them into anagram families.
#Input:  ["eat", "tea", "tan", "ate", "nat", "bat"]
#Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
#Input:  ["abc", "car", "arc", "dog", "god", "bca"]
#Output: [["abc", "bca"], ["car", "arc"], ["dog", "god"]]
#Input:  ["a", "b", "a"]
#Output: [["a", "a"], ["b"]]
 
#Input =  ["eat", "tea", "tan", "ate", "nat", "bat"]
#output=[]
#for anagram in Input:
#   group=[]
#    for word in Input:
#        for i in anagram:
#         for j in word:
#             if(i==j):
#                 break
#             else:
#                 break
#         else:
#             group.append(word)
        
#            if(group not in output):
#                      output.append(group)
#                      print(output)

#Q13. You are given a list of integers. Find the longest consecutive sequence.
#Input : [100, 4, 200, 1, 3, 2]
#Output: 4 (sequence: 1,2,3,4)
#Input : [0, -1, 1, 2]
#Output: 4 (sequence: -1,0,1,2)
#Input : [5]
#Output: 1
#Input : [0, -1, 1, 2]
#Output: 4 (sequence: -1,0,1,2)
#Input : [1, 1, 1, 1]
#Output: 1 (duplicates don't extend sequence)

#numbers = [100, 4, 200, 1, 3, 2]

#unique_numbers = []

#for num in numbers:
 #   if num not in unique_numbers:
  #      unique_numbers.append(num)

#unique_numbers.sort()

#longest = 1
#current = 1

#for i in range(1, len(unique_numbers)):
 #   if unique_numbers[i] == unique_numbers[i - 1] + 1:
  #      current += 1
   # else:
    #    if current > longest:
     #       longest = current
      #  current = 1

#if current > longest:
 #   longest = current

#print(longest)

#Q14. You are given a paragraph. Find the longest palindromic substring in it (ignore spaces and punctuation).
#Input : "never odd or even"
#Output: "neveroddoreven"
#Input : "racecar is a word"
#Output: "racecar"
#Input : "abcd"
#Output: any single character (no palindrome longer than 1)
#Input : "a"
#Output: "a"
 
 
# Q15. You are given two arrays. Without using any built-in set functions, find their intersection — elements that appear in both, without duplicates.
#Input : [1, 3, 5, 7, 3, 9] and [3, 5, 5, 8, 9]
#Output: [3, 5, 9]
#Input : [1, 2, 2, 3] and [2, 2, 3, 4]
#Output: [2, 3]
#Input : [1, 2, 3] and [4, 5, 6]
#Output: []
#Input : [] and [1, 2, 3]
#Output: []
  
arr1 = [1, 3, 5, 7, 3, 9]
arr2 = [3, 5, 5, 8, 9]
result = []

for i in arr1:
    if i in arr2 and i not in result:
        result.append(i)
        print(result)
        