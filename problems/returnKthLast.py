'''
Prompt:
Implement an algorithm to find the kth to last element of a singly linked list.
'''

from nodes import SinglyLinkedListNode as Node

# Time: O(n), Space: O(n), could have also done recursively
def returnKthLast(head, k):
  stack = []
  while head is not None:
    stack.append(head.value)
    head = head.next
  
  for _ in range(k-1):
    stack.pop()
  
  return stack.pop()

# Time: O(n), Space: O(1)
def returnKthLastOptimal(head, k):
  pback = head
  pahead = head
  # Assuming k is always less than size of head
  for _ in range(k):
    pahead = pahead.next
  
  while pahead is not None:
    pback = pback.next
    pahead = pahead.next
  
  return pback.value
  
  

t1 = Node(1)
t1.next = Node(2)
t1.next.next = Node(3)
t1.next.next.next = Node(4)
print(returnKthLastOptimal(t1, 2))
