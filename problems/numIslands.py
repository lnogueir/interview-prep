'''
Prompt:
Given an m x n grid. Each element will be either a "1" or "0".
"1" represents land, "0" represents water

Goal: is to find how many islands exist on the map

Example 1:
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

Output: 3
'''

def exploreIsland(grid, coord, visited):
	i, j = coord
	if coord in visited or grid[i][j] == "0":
  	return
  
	visited.add(coord)
  
  if i < len(grid)-1: # Up
  	exploreIsland(grid, (i+1, j), visited)
  
  if i > 0: # Down
  	exploreIsland(grid, (i-1, j), visited)
  
  if j < len(grid[i])-1: # Right
  	exploreIsland(grid, (i, j+1), visited)
    
  if j > 0:  # Left
  	exploreIsland(grid, (i, j-1), visited)

# Time: O(n*m), Space: O(n*m)
def numIslands(grid):
	visited = set([])
  islandsCount = 0
	for i in range(len(grid)):
  	for j in range(len(grid[i])):
    	coord = (i, j)
      isWater = grid[i][j] == "0"
    	if not isWater and coord not in visited:
      	exploreIsland(grid, coord, visited)
        islandsCount += 1
        
  return islandsCount
