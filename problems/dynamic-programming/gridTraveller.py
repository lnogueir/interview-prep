'''
Prompt:
  Say that you are a traveler on a 2D grid. You begin in the 
  top-left corner and your goal is to travel to the bottom-right
  corner. You may only move down or right.

  In how many ways can you travel to the goal on a grid with dimensions MxN?
'''

import time

# This approach has exponential time complexity
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

# dynamic programing soln
def numWaysToTravel_DP(m, n, cache = {}):
  if m == 1 and n == 1:
    return 1

  if (m, n) in cache:
    return cache[(m, n)]
  
  wayDown = numWaysToTravel_DP(m-1, n, cache) if m > 0 else 0
  wayRight = numWaysToTravel_DP(m, n-1, cache) if n > 0 else 0
  cache[(m, n)] = wayDown + wayRight
  return cache[(m, n)]


def numWaysToTravel_tabulation(m, n):
  table = [[0]*(n+1) for _ in range(m+1)] 
  table[1][1] = 1

  for i in range(len(table)):
    for j in range(len(table[i])):
      if i < len(table)-1:
        table[i+1][j] += table[i][j]
      
      if j < len(table[i])-1:
        table[i][j+1] += table[i][j]
  return table[-1][-1]


start = time.time()
sol1 = numWaysToTravel(12, 10)
end = time.time()
print(f'Sol1 without DP: result: {sol1}, time: {end - start} secs')

start = time.time()
sol2 = numWaysToTravel_DP(180, 180)
end = time.time()
print(f'Soln2 with DP - result: {sol2}, time: {end - start} secs')

start = time.time()
soln3 = numWaysToTravel_tabulation(180, 180)
end = time.time()
print(f'Soln3 with DP tabulation - result: {sol2}, time: {end - start} secs')
