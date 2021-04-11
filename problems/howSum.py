'''
Prompt:
Write a function howSu(targetSum, numbers) that takes in a 
targetSum and an array of numbers as arguments.

The function should return an array containing any combinations
of elements that add up to exactly the targetSum. If there is no
combination that adds up to the targetSum, then return null.

If there are multiple combinations possible, you may return any single one.
'''

def howSum(targetSum, numbers, combination = [], cache = set([])):
  if targetSum in cache:
    return None

  if targetSum == 0:
    return combination
  
  if targetSum < 0:
    return None

  for n in numbers:
    result = howSum(targetSum - n, numbers, [*combination, n])
    if result is not None:
      return result
    
    cache.add(targetSum-n)

  cache.add(targetSum)
  return None

print(howSum(300, [7, 14]))