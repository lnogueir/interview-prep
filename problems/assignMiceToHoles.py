'''
Prompt:
There are N Mice and N holes are placed in a straight line. 
Each hole can accommodate only 1 mouse. A mouse can stay at his position, 
move one step right from x to x + 1, or move one step left from x to x -1. 
Any of these moves consumes 1 minute. 

Assign mice to holes so that the time when the last mouse gets inside a hole is minimized.
'''

def minTimeToAssignMiceToHoles(mice, holes):
  mice.sort()
  holes.sort()
  
  maxTime = -float('inf')
  for m, h in zip(mice, holes):
    maxTime = max(maxTime, abs(m-h))

  return maxTime
