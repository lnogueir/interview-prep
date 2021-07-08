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

# idea is: 
# 1. make all the negative numbers be greater than n by taking abs and multiplying by (n+1)
# 2. negate the value at the index of numbers <= n
# 3. return first positive index found

def makeNonPositiveNumbersGreaterThanN(array, N):
  for i in range(len(array)):
    if array[i] <= 0:
      array[i] = abs(array[i] - N)*(N+1)
  
def negateValueAtIndexOfNumbersLessEqN(array, N):
  for i in range(len(array)):
    if array[i] <= N:
      if array[abs(array[i])-1] > 0:
        array[abs(array[i])-1] *= -1

def getFirstPositiveNumberIdx(array):
  for i in range(len(array)):
    if array[i] > 0:
      return i + 1

  return len(array) + 1

def findSmallestPositiveInteger(array):
  N = len(array)
  makeNonPositiveNumbersGreaterThanN(array, N)
  negateValueAtIndexOfNumbersLessEqN(array, N)
  return getFirstPositiveNumberIdx(array)