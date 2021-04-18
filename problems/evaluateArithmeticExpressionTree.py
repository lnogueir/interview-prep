'''
Prompt:
is an integer and each internal node is one of '+', '−', '∗', or '/'.
Given the root to such a tree, write a function to evaluate it.
For example, given the following tree:
    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).

You can assume the values of the nodes are strings
in the set: [numbers, *, /, +, -]
'''

class Node:
  def __init__(self, value):
    self.value = value
    self.right = None
    self.left = None

operators = {
  '*': lambda a,b: a * b,
  '/': lambda a,b: a / b,
  '+': lambda a,b: a + b,
  '-': lambda a,b: a - b,
}
def evaluateArithmeticExpression(expression: Node) -> int:
  if expression is None:
    return 0

  if expression.value not in operators:
    return int(expression.value)
  
  leftExpressionResult = evaluateArithmeticExpression(expression.left)
  rightExpressionResult = evaluateArithmeticExpression(expression.right)
  return operators[expression.value](leftExpressionResult, rightExpressionResult)

exp1 = Node('*')
exp1.left = Node('+')
exp1.right = Node('+')
exp1.left.left = Node('3')
exp1.left.right = Node('2')
exp1.right.left = Node('4')
exp1.right.right = Node('5')

print(evaluateArithmeticExpression(exp1))

