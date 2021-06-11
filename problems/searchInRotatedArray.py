'''
Prompt
/*
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.




										 i	
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1 
*/


Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

 l     m       r 
[4,5,6,7,0,1,2,3] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
'''

# Time: O(logn), Space: O(logn)
def binarySearch(array, left, right):
  if array[left] < array[right]:
    return array[left]
    
  if right == left:
    return array[right]

  mid = (left + right) // 2
  if array[mid] > array[right]:
    return binarySearch(array, mid+1, right)

  return binarySearch(array, left, mid)
    
def searchSortedRotatedArray(array):
	return binarySearch(array, 0, len(array)-1)
  
def searchSortedRotatedArray(array):
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
  
  

  


