'''
Prompt:
Write a function that given a string, returns its longest palindromic substring.

input: "abaxyzzyxf". output: "xyzzyx"
'''
# First solution O(n^3). Idea is, loop through all 
# substrings and see use biggest palindrome
def getPalindromeSize(string, left, right):
  l = left
  r = right
  while left < right:
    if string[left] != string[right]:
      return 0
    left += 1
    right -= 1
  return r - l

def longestPalindromicSubstring(string):
  longest = None
  maxLength = -float('inf')
  for i in range(len(string)):
    for j in range(len(string)-i):
      currentLength = getPalindromeSize(string, j, j+i)
      if maxLength < currentLength:
        maxLength = currentLength
        longest = (j, j+i)
			
  return "" if longest is None else string[longest[0]:longest[1]+1]

# Here i would use the fact that 'ab|ba', 'ab|c|ba'.
# So loop through the string starting at 1 and compute the 
# longest odd and even palindromes.
def longestPalindromicSubstring_V2(string):
  pass

print(longestPalindromicSubstring("abaxyzzyxf"))