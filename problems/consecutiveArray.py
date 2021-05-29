'''
Prompt:
Given an unsorted array, find the length of the longest sequence of
consecutive numbers in the array.

consecutive([ 4 , 2 , 1 , 6 , 5 ]) = 3 , [ 4 , 5 , 6 ]
consecutive([ 5 , 5 , 3 , 1 ]) = 1 , [ 1 ], [ 3 ], or [ 5 ]
'''

# Idea: sort the array!
# Time: O(nlogn), Space: O(1) 
def consecutiveSorting(array):
  if len(array) == 0:
    return []

  array.sort()
  consecutiveCount = 0
  runningConsecutiveCount = 0
  for idx in range(1, len(array)):
    if array[idx] == array[idx-1] + 1:
      runningConsecutiveCount += 1
      continue
    solution = max(runningConsecutiveCount, consecutiveCount)
    consecutiveCount = 1

  return max(runningConsecutiveCount, consecutiveCount)
  
def consecutive(array):
  hashSet = set([n for n in array])
  bestConsecutiveCount = 0
  
  for idx in range(len(array)):
    if array[idx]-1 in hashSet:
      continue

    runningConsecutiveCount = 0
    i=array[idx]
    while i in hashSet:
      runningConsecutiveCount += 1
      i += 1
    
    bestConsecutiveCount = max(runningConsecutiveCount, bestConsecutiveCount)
  
  return bestConsecutiveCount

print(consecutive([ 4 , 2 , 1 , 6 , 5 ]))
print(consecutive([ 5 , 5 , 3 , 1 ]))