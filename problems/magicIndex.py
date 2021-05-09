'''
Prompt:
A magic index in an array A [ 0 ••• n -1] is defined to be an index such that A[ i] =
i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
array A.
FOLLOW UP
What if the values are not distinct?
'''

# Idea is do some sort of binary search
# For the follow up, if we have repetitive values,
# We the magic index might be in either direction
# However, we can limit the search based on A[mid]
def binarySearch(A, left, right):
  if left > right:
    return -1

  mid = (left + right) // 2
  if A[mid] == mid:
    return mid
  
  leftResult = binarySearch(A, left, min(mid-1, A[mid]))
  if leftResult != -1:
    return leftResult
  
  return binarySearch(A, max(A[mid], mid+1), right)


def magicIndex(A):
  return binarySearch(A, 0, len(A)-1)

t1 = [0, 3, 4, 7]
print(magicIndex(t1))
t2 = [1, 3, 4, 7]
print(magicIndex(t2))
t3 = [1, 1, 1, 2, 2, 7, 10]
print(magicIndex(t3))
t3 = [1, 2, 4, 5, 6, 6, 6]
print(magicIndex(t3))