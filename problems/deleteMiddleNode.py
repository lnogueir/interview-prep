'''
Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
lnput:the node c from the linked lista->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f
'''

from nodes import SinglyLinkedListNode as Node

def deleteMiddleNode(node):
  if node is None or node.next is None:
    return

  node.value = node.next.value
  node.next = node.next.next if node.next is not None else None
  return

t1 = Node('a')
t1.next = Node('b')
cNode = t1.next.next = Node('c')
t1.next.next.next = Node('d')
t1.next.next.next.next = Node('e')
t1.next.next.next.next.next = Node('f')

deleteMiddleNode(cNode)

while t1 is not None:
  print(t1.value)
  t1 = t1.next


