'''
Prompt:
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1.
(e.g., "waterbottle" is a rotation of "erbottlewat").

Follow up:
What if you could use one call of a helper method isSubstring?
'''

# Time: O(n), Space: O(n)
def isStringRotation(s1, s2):
  if len(s1) != len(s2):
    return False
  
  strLength = len(s1) or len(s2)
  s1Prefix = []
  s1Suffix = [c for c in s1]
  s2Prefix = [c for c in s2]
  s2Suffix = []
  for idx in range(strLength):
    if s1Suffix == s2Prefix and s1Prefix == s2Suffix:
      return True

    s1Prefix.append(s1Suffix.pop(0))
    s2Suffix.insert(0, s2Prefix.pop())

  return False


'''
Follow up:
Notice that if isStringRotation(s1, s2) == True
Let `p` be the prefix of the string and `s` the suffix.
Then s1 can be broken down into s1=`ps` and s2=`sp`

Therefore, notice that s1s1 = `psps`, so s2 must be a substring.
So: return isSubstring(s1+s1, s2)
'''


print(isStringRotation("waterbottle", "erbottlewat"))
print(isStringRotation("waterbottle", "erbottlewqt"))
print(isStringRotation("waterbottle", "eniottlewdt"))
print(isStringRotation("lucas", "sluca"))
print(isStringRotation("lucas", "wluca"))






