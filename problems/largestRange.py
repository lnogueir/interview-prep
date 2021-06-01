'''
Prompt:

Given an array of integers, return an array of length 2 representing the 
largest range of integers contained in that array.

Input: [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]

Output: [0, 7]
'''

def rangeLength(rng):
  lowerBound, upperBound = rng
  return upperBound - lowerBound

# Solution 1: Sort array and look if next element is consecutive
# Time: O(nlogn), Space: O(1)
def largestRange(array):
  array.sort()
  bestRange = None
  currUpperBound = None
  currLowerBound = None
  for n in array:
    if bestRange is None:
      currLowerBound = n
      currUpperBound = n
      bestRange = [n, n]
      continue
    
    if n == currUpperBound + 1 or n == currUpperBound:
      currUpperBound = n
    else:
      currLowerBound = n
      currUpperBound = n
    
    currentRange = [currLowerBound, currUpperBound]
    if rangeLength(currentRange) > rangeLength(bestRange):
      bestRange = currentRange
    
  return bestRange

# Solution 2: Note that an element cannot ever belong to more than one range, 
# then explore elements to left and to the right, while marking them as visited
# Time: O(n), Space: O(n)
def largestRange2(array):
  hashMap = {}
  bestRange = None
  
  for n in array:
    hashMap[n] = True
  
  for n in array:
    if not hashMap[n]:
      continue
      
    hashMap[n] = False
    left = n
    right = n
    while left - 1 in hashMap:
      left -= 1
      hashMap[left] = False
    
    while right + 1 in hashMap:
      right += 1
      hashMap[right] = False
      
    if bestRange is None or rangeLength([left, right]) > rangeLength(bestRange):
      bestRange = [left, right]
  
  return bestRange

print(largestRange([19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]))
print(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))
print(largestRange2([19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]))
print(largestRange2([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))