'''
Prompt:
Write a function that, fiven a string, returns the length of the longest palindromic
subsequence.

Ex: 
input: "abaxyaba", output: 7. Because "abaxaba", or "abayaba"
are the longest palindromic subsequence.
'''

# Solution with no memoization. Time: O(2^n), Space: O(n)
# We could use memoization and cache the (left, right) idxs 
# and reduce time to O(n) while maintaining O(n) space.
def longestPalindromicSubsequence(string, left=0, right=None):
  if right is None:
    right = len(string)-1
	
  if left > right:
    return 0

  if left == right:
    return 1

  if string[left] != string[right]:
    return max(
      longestPalindromicSubsequence(string, left+1, right),
      longestPalindromicSubsequence(string, left, right-1),
    )

  return 2 + longestPalindromicSubsequence(string, left+1, right-1)

print(longestPalindromicSubsequence("abaxyaba"))

