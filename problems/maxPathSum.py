'''

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def maxDirectAndOverallPathSum(tree):
	if tree is None:
		return 0, float('-inf')

	leftDirect, leftOverall = maxDirectAndOverallPathSum(tree.left)
	rightDirect, rightOverall = maxDirectAndOverallPathSum(tree.right)

	rootDirect = tree.value + max(leftDirect, rightDirect)
	rootOverall = max(
		rootDirect,
		tree.value + leftDirect + rightDirect,
		leftOverall, 
		rightOverall
	)

	return rootDirect, rootOverall

def maxPathSum(tree):
	_, overallMaxPathSum = maxDirectAndOverallPathSum(tree)
	return overallMaxPathSum


t1 = Node(1)
t1.left = Node(2)
t1.left.left = Node(4)
t1.left.right = Node(5)
t1.right = Node(3)
t1.right.left = Node(6)
t1.right.right = Node(7)

print(maxPathSum(t1))

t2 = Node(1)
t2.left = Node(-1)
t2.right = Node(2)
print(maxPathSum(t2))

