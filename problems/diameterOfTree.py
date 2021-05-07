'''
Prompt:
Write a function that takes in a Binary Tree and returns its diameter. The
diameter of a binary tree is defined as the length of its longest path, even
if that path doesn't pass through the root of the tree.

A path is a collection of connected nodes in a tree, where no node is
connected to more than two other nodes. The length of a path is the number of
edges between the path's first node and its last node.

Each BinaryTree node has an integer value, a left child and a right child.
Sample input:
 tree =       1
            /   \
           3     2
         /   \ 
        7     4
       /       \
      8         5
     /           \
    9             6

Sample Output:
6 // 9 -> 8 -> 7 -> 3 -> 4 -> 5 -> 6
'''

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def getHeightAndDiameter(tree):
    if tree is None:
        return 0, 0
    
    leftHeight, leftDiameter = getHeightAndDiameter(tree.left)
    rightHeight, rightDiameter = getHeightAndDiameter(tree.right)

    rootHeight = 1 + max(leftHeight, rightHeight)
    rootDiameter = max(
        1 + leftHeight + rightHeight,
        leftDiameter,
        rightDiameter
    )
    return rootHeight, rootDiameter

def diameterOfTree(tree):
    _, diameter = getHeightAndDiameter(tree)
    return diameter

tree = Node(1)
tree.left = Node(3)
tree.right = Node(2)
tree.left.left = Node(7)
tree.left.left.left = Node(8)
tree.left.left.left.left = Node(9)
tree.left.right = Node(4)
tree.left.right.right = Node(5)
tree.left.right.right.right = Node(6)
print(diameterOfTree(tree))
