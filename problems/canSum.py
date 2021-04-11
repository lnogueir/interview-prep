'''
Prompt:

Write a function canSum(targetSum, numbers) that takes in a
target Sum and an array of nubmers as arguments.

The function should return a boolean indicating whether or not 
it is possible to generate the targetSum using numbers from the array.

You may use an element of the array as may times as needed.
You may assume that all input numbers are nonnegative.
'''

def canSum(targetSum, numbers, currentSum = 0):
  if currentSum > targetSum:
    return False
  
  if currentSum == targetSum:
    return True

  for n in numbers:
    if canSum(targetSum, numbers, currentSum + n):
      return True
  return False

# soln with dynamic programming
def canSum_DP(targetSum, numbers, currentSum = 0, cache = set({})):
  if currentSum in cache:
    return False

  if currentSum > targetSum:
    return False
  
  if currentSum == targetSum:
    return True
  
  for n in numbers:
    if canSum_DP(targetSum, numbers, currentSum + n, cache):
      return True
    cache.add(currentSum + n)

  return False


print(canSum(700, [2, 4, 7]))
print(canSum(7, [2, 4, 7]))
print(canSum_DP(300, [14, 7, 7]))

