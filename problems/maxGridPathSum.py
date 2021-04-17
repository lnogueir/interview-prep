'''
Prompt:
You are given an MxN grid where each square contains a positive integer.

Write a function maxGridPathSum(grid) which maximizes the path sum going from 
the most upper-left square to the most bottom-right square.

You can only move down and right.

M > 0, N > 0 
'''

def maxGridPathSum(grid, i=0, j=0, cache={}):
  if (i,j) in cache:
    return cache[(i,j)]

  if i >= len(grid) or j >= len(grid[0]):
    return 0

  if i == len(grid)-1 and j == len(grid[i])-1:
    return grid[i][j]

  downValue = 0
  if i < len(grid):
    downValue = maxGridPathSum(grid, i+1, j)
  
  rightValue = 0
  if j < len(grid[0]):
    rightValue = maxGridPathSum(grid, i, j+1)

  cache[(i,j)] = max(downValue, rightValue) + grid[i][j]
  return cache[(i,j)]



t1 = [
  [3, 7, 9, 2, 7],
  [9, 8, 3, 5, 5],
  [1, 7, 9, 8, 5],
  [3, 8, 6, 4, 10],
  [6, 3, 9, 7, 8]
]

print(maxGridPathSum(t1)) # 67