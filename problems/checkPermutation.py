'''
Prompt:
Given two strings, write a method to decide if one is a permutation of the other.
'''

from collections import Counter

# O(nlogn + mlogm)
def checkPermutation(s1, s2):
  return sorted(s1) == sorted(s2)


def checkPermutationV2(s1, s2):
  c1 = Counter(s1)
  c2 = Counter(s2)
  
  return c1 == c2

print(checkPermutationV2('abc', 'acb'))

