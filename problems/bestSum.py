'''
Prompt:
Write a function bestSum(targetSum, numbers) that takes 
in a targetSum and an array of numbers as arguments.

The function should return an array containing the
shortest combination of numbers that add up to exactly the targetSum.

If there is a tie for the shotest combination, you may return any of the shortest.
'''

# takes in a numbers array in decreasing order
def recurse(targetSum, numbers, combination = []):
  if targetSum == 0:
    return combination
  
  if targetSum < 0:
    return None
  
  for n in numbers:
    result = recurse(targetSum-n, numbers, [*combination, n])
    if result is not None:
      return result

  return None

# Greedy approach. This only works on some sets of coins.
# Why? Consider this input: bestSum(8, [1, 4, 5])
# Should return [4, 4], but we are returning [5, 1, 1, 1]
def bestSum(targetSum, numbers):
  numbers.sort(reverse=True)
  return recurse(targetSum, numbers)

# Correct optimal solution with dynamic programming
def bestSum_V2(targetSum, numbers, cache = {}):
  if targetSum in cache:
    return cache[targetSum]

  if targetSum == 0:
    return []
  
  if targetSum < 0:
    return None
  
  best = None
  for n in numbers:
    result = bestSum_V2(targetSum-n, numbers, cache)
    if result is not None:
      current = [*result, n]
      if best is None or len(best) > len(current):
        best = current

  cache[targetSum] = best
  return best



# print(bestSum(28, [7, 2, 1, 10, 5]))
# print(bestSum(7, [5, 3, 4, 7]))
# print(bestSum(8, [1, 4, 5]))

# print(bestSum_V2(28, [7, 2, 1, 10, 5]))
# print(bestSum_V2(7, [5, 3, 4, 7]))
# print(bestSum_V2(300, [100, 150, 7, 14]))
print(bestSum_V2(8, [1, 4, 5]))
  
