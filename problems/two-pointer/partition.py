'''
Prompt:
Write a function partition(array, pivot) that takes a non-empty array of numbers
and a pivot point index and that will modify the array in-place and ensure
that all elements in the left of pivot point are less than pivot point
and all elements to the right are greater than the pivot point.
Return the index of the pivot point after the condition is applied
'''


def swap(array, i, j):
  tmp = array[i]
  array[i] = array[j]
  array[j] = tmp

def partition(array, pivotIdx):
  pivotValue = array[pivotIdx]
  swap(array, pivotIdx, len(array)-1)

  partitionIdx = -1

  i = partitionIdx
  while i < len(array) - 1:
    if array[i] < pivotValue:
      partitionIdx += 1
      swap(array, partitionIdx, i)
    i += 1
  
  partitionIdx += 1
  swap(array, partitionIdx, len(array) - 1)
  return partitionIdx

array = [5,2,3,8,6]
partition(array, 0)
print(array)