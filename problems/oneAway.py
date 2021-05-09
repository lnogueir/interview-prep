'''
Prompt:
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. 
Given two strings, write a function to check if they are one edit (or zero edits) away.
'''

def isOneReplaceAway(src, dst):
  if len(src) != len(dst):
    return False
  
  hasReplaced = False
  for c1, c2 in zip(src, dst):
    if c1 == c2:
      continue

    if hasReplaced:
      return False
    hasReplaced = True

  return True

def isOneInsertOrDeletionAway(src, dst):
  if abs(len(src) - len(dst)) != 1:
    return False
  
  longerStr = max(src, dst, key=lambda i: len(i))
  smallerStr = min(src, dst, key=lambda i: len(i))

  hasInsertedOrDeleted = False
  i = 0
  j = 0
  while i < len(longerStr) and j < len(smallerStr):
    if longerStr[i] != smallerStr[j]:
      if hasInsertedOrDeleted:
        return False
      hasInsertedOrDeleted = True
      i += 1

    i += 1
    j += 1

  return True


def oneAway(src, dst):
  if abs(len(dst) - len(src)) >= 2:
    return False  
  
  return isOneReplaceAway(src, dst) or isOneInsertOrDeletionAway(src, dst)

print(oneAway('pale', 'ple'))
print(oneAway('pales', 'pale'))
print(oneAway('pale', 'bale'))
print(oneAway('pale', 'bake'))


