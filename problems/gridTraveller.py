'''
Prompt:
  Say that you are a traveler on a 2D grid. You begin in the 
  top-left corner and your goal is to travel to the bottom-right
  corner. You may only move down or right.

  In how many ways can you travel to the goal on a grid with dimensions MxN?
'''

def numWaysToTravel(m, n):
  queue = [(0, 0)]
  totalNumWays = 0

  while len(queue) > 0:
    i, j = queue.pop()

    if i == m-1 and j == n-1:
      totalNumWays += 1

    if 0 <= i < m:
      queue.append((i+1, j))
    if 0 <= j < n:
      queue.append((i, j+1))

  return totalNumWays
    
print(numWaysToTravel(10, 10))