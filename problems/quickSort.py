'''
Prompt:
Implement the quick algorithm.
'''
from partition import partition

def qsRecurse(array, left, right):
  if left >= right:
    return

  p = partition(array, left, right)
  qsRecurse(array, left, p-1)
  qsRecurse(array, p+1, right)

def quickSort(array):
  qsRecurse(array, 0, len(array)-1)
  return array

if __name__ == '__main__':
  t1 = [6, 3, 7, 9, 1]
  t2 = [-2, 5, 2, 1, 4]
  print(quickSort(t1))
  print(quickSort(t2))