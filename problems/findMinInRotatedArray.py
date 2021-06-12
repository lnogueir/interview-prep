'''
Prompt:
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2,3] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
'''

def binarySearch(array, left, right):
  if array[left] < array[right]:
    return array[left]
    
  if right == left:
    return array[left]

  mid = (left + right) // 2
  if array[mid] > array[right]:
    return binarySearch(array, mid+1, right)

  return binarySearch(array, left, mid)

# Time: O(logn), Space: O(logn)    
def findMinInRotatedArray(array):
	return binarySearch(array, 0, len(array)-1)
  
# Time: O(logn), Space: O(1)
def findMinInRotatedArray2(array):
  left = 0
  right = len(array)-1
  while left != right:
    if array[left] < array[right]:
      break
      
    mid = (left + right) // 2
    if array[mid] > array[right]:
      left = mid+1
    else:
      right = mid
    
  return array[left]
  
  

  


