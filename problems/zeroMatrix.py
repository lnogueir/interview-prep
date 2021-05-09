'''
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
'''
def fillRowWithZeros(matrix, rowIdx):
  for idx in range(len(matrix[rowIdx])):
    matrix[rowIdx][idx] = 0

def fillColumnWithZeros(matrix, columnIdx):
  for idx in range(len(matrix)):
    matrix[idx][columnIdx] = 0 

# Time: O(M*N), Space: O(M + N)
def zeroMatrix(matrix):
  columns = [False for _ in range(len(matrix))]
  rows = [False for _ in range(len(matrix[0]))]

  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if matrix[i][j] == 0:
        rows[i] = True
        columns[j] = True
  
  for idx in range(len(rows)):
    if rows[idx]:
      fillRowWithZeros(matrix, idx)
  
  for idx in range(len(columns)):
    if columns[idx]:
      fillColumnWithZeros(matrix, idx)

m1 = [
  [1,2,3],
  [1,0,2],
  [4,5,6],
]
zeroMatrix(m1)
print(m1)