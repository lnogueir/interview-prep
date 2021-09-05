'''
Prompt: Find the smallest missing positive integer

Given: An array on integers (un-sorted)

Goal: Find the smallest missing positive integer that does not exist in the array

Ex:
[1,2,-1]  -> 3

[1,2,3,5] -> 4

[7,8,9,11,12] -> 1

[3, 4, -1, 1, -5] -> 2

[5, 60, 120, 4, 3, -1] -> 2

[400,2], 1

[1,2,3], 4

Constraints: Time Complexity O(n), Use Constant space O(1)
'''

# Idea is:
# Let n = len(array).
# The max possible missing positive would be n + 1.
# So we can discard all elements that are not in the range (1, n).

def cleanUpArray(array):
  n = len(array)
  for i in range(n):
    if array[i] > n or array[i] <= 0:
      array[i] = 1

  return

def negateIndexes(array):
  n = len(array)
  for i in range(n):
    idxMap = abs(array[i])
    if array[idxMap-1] < 0:
      continue

    array[idxMap-1] *= -1


def firstPositiveIndex(array):
  n = len(array)
  for i in range(n):
    if array[i] > 0:
      return i + 1
  
  return n + 1

def findSmallestPositiveInteger(array):
  if 1 not in array:
    return 1
  
  cleanUpArray(array)
  negateIndexes(array)
  return firstPositiveIndex(array)

print(findSmallestPositiveInteger([7,8,9,11,12]))
