'''
Prompt:
Write a function partition(array, left, right) that takes a non-empty array of numbers
and boundaries and will modify the array in-place and ensure
that all elements in the left of some pivot point are less than pivot point
and all elements to the right are greater than the pivot point.
Return the index of the pivot point after the condition is applied.
'''

def partition(array, left, right):
	lessThanOffset = -1 + left
	pivotIdx = right
	for greaterThanOffset in range(left, pivotIdx):
		if array[greaterThanOffset] < array[pivotIdx]:
			lessThanOffset += 1
			array[lessThanOffset], array[greaterThanOffset] = array[greaterThanOffset], array[lessThanOffset]
			
	lessThanOffset += 1
	array[lessThanOffset], array[pivotIdx] = array[pivotIdx], array[lessThanOffset]
	
	pivotIdx = lessThanOffset 
	return pivotIdx


if __name__ == '__main__':
  array = [5,2,3,8,6]
  partition(array, 0, len(array)-1)
  print(array)