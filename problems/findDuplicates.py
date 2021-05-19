'''
Prompt:
Given an array of integers where each value 1 <= x <= len(array), write a
function that finds all the duplicates in the array.

findDuplicates([ 1 , 2 , 3 ]) = []
findDuplicates([ 1 , 2 , 2 ]) = [ 2 ]
findDuplicates([ 3 , 3 , 3 ]) = [ 3 ]
findDuplicates([ 2 , 1 , 2 , 1 ]) = [ 1 , 2 ]
'''

# Trivial solution using hash sets
# Time: O(n), Space: O(n)
def findDuplicatesHashSets(array):
  duplicates = set([])
  seenItems = set([])
  for n in array:
    if n in seenItems:
      duplicates.add(n)
      continue
    seenItems.add(n)

  return list(duplicates)

# Solution without extra space
def findDuplicates(array):
  duplicates = set([])
  for idx in range(len(array)):
    if array[abs(array[idx]) - 1] < 0:
      duplicates.add(abs(array[idx]))
      continue

    array[abs(array[idx]) - 1] *= -1

  return list(duplicates)




print(findDuplicates([ 1 , 2 , 3 ]))
print(findDuplicates([ 1 , 2 , 2 ]))
print(findDuplicates([ 3 , 3 , 3 ]))
print(findDuplicates([ 2 , 1 , 2 , 1 ]))