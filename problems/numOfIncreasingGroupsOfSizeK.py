'''
Given an array of integers and a number k, find the
number of consecutive intervals of length k that are
strictly increasing

Example:
numberOfIncreasingGroupsOfSizeK([2,2,3,4,5], 2) == 3
Explanation:
  len([[2,3], [3,4], [4,5]]) == 3
'''

def createWindow(nums, k):
	window = []
	for i in range(k):
		window.append(nums[i])
  
  return window
    
def isStrictlyIncreasing(array):
  for i in range(1, len(array)):
    if array[i] > array[i-1]:
      continue
    return False

  return True

# Time: O(n*k), Space: O(k)
def numberOfIncreasingGroupsOfSizeK(nums, k):
  window = createWindow(nums, k)
  numOfIncreasingGroups = 1 if isStrictlyIncreasing(window) else 0
  
  for i in range(k, len(nums)):
    window.pop(0)
    window.append(nums[i])
    if isStrictlyIncreasing(window):
      numOfIncreasingGroups += 1
    
  return numOfIncreasingGroups
  