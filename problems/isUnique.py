'''
Prompt:

Implement an algorithm to determine if a string has all unique characters.

Follow up:
What if you cannot use additional data structures?
'''

def isUnique(string):
  hashSet = set([])
  for c in string:
    if c in string:
      return False
    hashSet.add(c)

  return True

def isUniqueFollowUp(string):
  sortedString = sorted(string)
  for idx in range(len(string)-1):
    if string[idx] == string[idx+1]:
      return False
      
  return True
