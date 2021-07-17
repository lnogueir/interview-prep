'''
Prompt:

Given a knight coordinate in a chess board and a target coordinate
return the minimum number of moves to get to the target location.
'''

# knight possible moves: 
# (x+2, y+1), (x-2, y-1), (x+2,y-1), (x-2,y+1), (x+1,y-2), (x+1, y+2), (x-1, y+2), (x-1,y+2)

def isInBoard(n, x, y):
	return 0 <= x < n and 0 <= y < n
  
def knightPossibleMoves(x, y):
	return ((x+2, y+1), (x-2, y-1), (x+2,y-1), (x-2,y+1), (x+1,y-2), (x+1, y+2), (x-1, y+2), (x-1,y+2))
              
def minKnightMovesHelper(n, x, y, target_x, target_y, visited):
  if (x, y) in visited:
    return visited[(x,y)]

  if not isInBoard(n, x, y):
    visited[(x,y)] = float('inf')
    return float('inf')

  if (x, y) == (target_x, target_y):
    visited[(x,y)] = 0
    return 0

  minimumMoves = float('inf')
  for i, j in knightPossibleMoves(x, y):
    minimumMoves = min(1 + minKnightMovesHelper(n, i, j, target_x, target_y, visited), minimumMoves)
    
  visited[(x,y)] = minimumMoves
  return minimumMoves
  
def minKnightMoves(n, x, y, target_x, target_y):
	result = minKnightMovesHelper(n, x, y, target_x, target_y, {}) 
	return result if result != float('inf') else -1