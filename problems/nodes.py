class SinglyLinkedListNode:
  def __init__(self, value):
    self.value = value
    self.next = None

class DoublyLinkedListNode:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None

class BinaryTreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class TreeNode:
  def __init__(self, value):
    self.value = value
    self.children = []