'''
Prompt:
Given a string, write a function to check if it is a permutation of a palindrome.

A palindrome is a word or phrase that is the same forwards as backwards.

A permutation is a rearrangement of letters. 
The palindrome does not need to be limited to just dictionary words.
'''


# brute force: generate all permutations of string, then check if any of them is a palindrome
from isPalindrome import isPalindrome
from permutations import permutations
def bruteForce(string):
  permuts = permutations(string)
  for p in permuts:
    if isPalindrome(p):
      return True

  return False

# Count characters then if n-1 characters have a count % 2 == 0, then there must exist a palindrome.

from collections import Counter

def palindromePermutation(string):
  charCounter = Counter(string.lower().replace(' ',''))
  foundOneOddCount = False
  for c in charCounter:
    if charCounter[c] % 2 == 0:
      continue

    if foundOneOddCount:
      return False

    foundOneOddCount = True

  return True

def palindromePermutationLittleOptimization(string):
  hashMap = {}
  oddCount = 0
  for c in string:
    if c not in hashMap:
      hashMap[c] = 0  
    hashMap[c] += 1

    oddCount += 1 if hashMap[c] % 2 == 1 else -1

  return oddCount <= 1

print(palindromePermutation('Tact Coa'))


