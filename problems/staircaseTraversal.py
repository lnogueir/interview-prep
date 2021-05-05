'''
Prompt:
Write a function `staircaseTraversal(height, maxStep)` that takes a `height` and a `maxStep`.

The function should return the number of ways you can reach the height using steps from (1, maxStep).

Ex:
staircaseTraversal(3, 2) -> 2. Because you can do [1, 1], or [2, 1].
'''

def staircaseTraversal(height, maxStep, memo={}):
  if height in memo:
    return memo[height]

  if height == 0:
    return 1

  if height < 0:
    return 0
  
  waysToTraverse = 0
  for step in range(1, maxStep + 1):
    waysToTraverse += staircaseTraversal(height - step, maxStep, memo)
  
  memo[height] = waysToTraverse
  return waysToTraverse

print(staircaseTraversal(110, 12)) # [2,2], [1,1,1,1], [2, 1, 1], [1, 1, 2], [1, 2, 1]