'''
Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
'''

def transpose(matrix):
  for diag in range(len(matrix)):
    for idx in range(diag, len(matrix)):
      matrix[diag][idx], matrix[idx][diag] = matrix[idx][diag], matrix[diag][idx]
  
  return matrix

def reverseRow(row):
  left = 0
  right = len(row) - 1
  while left < right:
    row[left], row[right] = row[right], row[left]
    left += 1
    right -= 1 

def reverse(matrix):
  for row in matrix:
    reverseRow(row)

  return matrix

def rotateMatrix(matrix):
  return reverse(transpose(matrix))

m1 = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
]
m2 = [
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12],
  [13,14,15,16],
]


def rotateMatrixSwapping(matrix):
  pass


print(rotateMatrix(m1))
print(rotateMatrix(m2))
