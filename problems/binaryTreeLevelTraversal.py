'''
Prompt:
Given the oot of a binary tree, return the level order traversal of its nodes' values (from left to right, level by level).
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# solution with BFS
def levelOrder(root):
  soln = []
  if root is None:
    return soln

  queue = [root]
  while len(queue) > 0:
    currentLevel = []
    levelLength = len(queue)
    for _ in range(levelLength):
      node = queue.pop(0)
      currentLevel.append(node.val)
      if node.left is not None:
        queue.append(node.left)

      if node.right is not None:
        queue.append(node.right)
    soln.append(currentLevel)

  return soln



# solution using a heap

import heapq

class Solution:
  def __init__(self):
    self.minHeap = []
    self.soln = []
    self.idx = 0
      
  def populateMinHeap(self, root, level = 0):
    if root is None:
      return
    heapq.heappush(self.minHeap, (level, self.idx, root))
    self.idx += 1
    self.populateMinHeap(root.left, level + 1)
    self.populateMinHeap(root.right, level + 1)
      
  def levelOrder(self, root):
    self.populateMinHeap(root)
    level = -1
    while len(self.minHeap) > 0:
      currentLevel, _, item = heapq.heappop(self.minHeap)
      if level != currentLevel:
        level = currentLevel
        self.soln.append([item.val])
      else:
        self.soln[-1].append(item.val)
            
    return self.soln

root = TreeNode(3)
root.left = TreeNode(9)
root.left.left = TreeNode(10)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# print(Solution().levelOrder(root))
print(levelOrder(root))


