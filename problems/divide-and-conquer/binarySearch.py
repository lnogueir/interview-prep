'''
Prompt:
Write a function `search(array, target)` that takes a sorted 
array and a target and returns the index of target or -1 if not found.
'''
import math

# recursive solution
def helper(array, target, left, right):
  if left > right:
    return -1

  mid = math.floor((left + right)/2)
  if array[mid] == target:
    return mid
  
  if array[mid] < target:
    return helper(array, target, mid+1, right)
  
  return helper(array, target, left, mid-1)

def search1(array, target):
  return helper(array, target, 0, len(array)-1)

print(search1([1, 3, 5, 8], 9))
print(search1([1, 3, 5, 8], 5))
