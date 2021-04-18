'''
Prompt:
Find the median of two sorted arrays of integers.

Prototype: median(arr1: list[int], arr2: list[int]) -> float
'''
import math

# brute force. time: O((n+m)log(n+m)), space: O(m+n)
# time could be easily reduced to O(n+m) with two pointers
def bruteForce(arr1, arr2):
  sortedArray = []
  for n in arr1:
    sortedArray.append(n)

  for n in arr2:
    sortedArray.append(n)
  
  sortedArray.sort()
  mid = math.floor(len(sortedArray) / 2)
  if len(sortedArray) % 2 == 0:
    return (sortedArray[mid] + sortedArray[mid+1])/2
  else:
    return sortedArray[mid]

def median(arr1, arr2):
  totalLen = len(arr1) + len(arr2)
  isEven = totalLen % 2 == 0
  medianIdx = math.floor(totalLen / 2) - 1 

  idx1 = 0
  idx2 = 0
  lesserThanIdx = 0
  while idx1 + idx2 < medianIdx:
    if idx1 < len(arr1) and idx2 < len(arr2):
      if arr1[idx1] < arr2[idx2]:
        lesserThanIdx = idx1
        idx1 += 1
      else:
        lesserThanIdx = idx2
        idx2 += 1
    
    if idx1 < len(arr1):
      lesserThanIdx = idx1
      idx1 += 1
    else:
      lesserThanIdx = idx2
      idx2 += 1
  
  
    

    
  
  
  
  



print(median([1,3,4,5], []))





