'''
Given a Binary Tree find the length of the longest path which comprises of connected nodes with consecutive values in increasing order. 

Example 1:

Input :      
           1                               
         /   \                          
        2     3                      

Output: 2

Explanation : Longest sequence is 1, 2.
'''

from nodes import BinaryTreeNode as Node

class Solution:
    def longestConsecutiveHelper(self, root):
        if root is None:
            return 0
            
        longestConsecutiveFromLeft = self.longestConsecutiveHelper(root.left)
        longestConsecutiveFromRight = self.longestConsecutiveHelper(root.right)
        
        longest = 0
        if root.left is not None and root.left.value == root.value + 1:
            longest = max(longest, longestConsecutiveFromLeft + 1)
        
        if root.right is not None and root.right.value == root.value + 1:
            longest = max(longest, longestConsecutiveFromRight + 1)
        
        return longest

    def longestConsecutive(self, root):
        solution = self.longestConsecutiveHelper(root)
        return solution + 1 if solution != 0 else -1

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
print(Solution().longestConsecutive(tree))