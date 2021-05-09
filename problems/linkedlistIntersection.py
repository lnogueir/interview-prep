'''
Prompt:
Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting
node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.
'''

from nodes import SinglyLinkedListNode as Node

# Idea is to go from the same starting point
# So advance longer ll pointer to an offset equal to lengths diff
def intersection(l1, l2):
  l1Len = length(l1)
  l2Len = length(l2)

  shorter = l1 if l1Len < l2Len else l2
  longer = l1 if l1Len >= l2Len else l2

  # idea
  for _ in range(abs(l1Len - l2Len)):
    longer = longer.next
  
  while shorter is not None and longer is not None:
    if shorter == longer:
      return shorter
    
    shorter = shorter.next
    longer = longer.next

  return None

def length(l):
  counter = 0
  while l is not None:
    counter += 1
    l = l.next
  return counter

intersectingNode = Node(3)
l1 = Node(1)
l1.next = Node(2)
l1.next.next = intersectingNode
l1.next.next.next = Node(4)
l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(7)
l2.next.next.next = intersectingNode

print(intersectingNode == intersection(l1, l2))