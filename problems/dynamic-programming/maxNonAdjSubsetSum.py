'''
Write a function that takes in an array of positive integers and
returns the maximum sum of non-adjacent elements in the array.

Ex:
Input: [75, 105, 120, 75, 90, 135]
Output: 330 // 75 + 120 + 135
'''

def maxSubsetSumNoAdjacent(array, i=0, cache=None):
  if cache is None:
    cache = {}
		
  if i in cache:
    return cache[i]
		
  if i >= len(array):
    return 0
	
  cache[i] = max(array[i] + maxSubsetSumNoAdjacent(array, i+2), maxSubsetSumNoAdjacent(array, i+1))
  return cache[i]

print(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]))
print(maxSubsetSumNoAdjacent([9, 3, 7, 8, 1, 10]))