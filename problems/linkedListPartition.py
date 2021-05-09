'''
Prompt:
Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions
'''

from nodes import SinglyLinkedListNode as Node

# Partition in place following standard partition algorithm from QuickSort
# Time: O(n), Space: O(1)
def linkedListPartition(head, pivot):
  lessThanPtr = None
  greaterThanPtr = head
  while greaterThanPtr is not None:
    if greaterThanPtr.value < pivot:
      lessThanPtr = lessThanPtr.next if lessThanPtr is not None else head
      lessThanPtr.value, greaterThanPtr.value = greaterThanPtr.value, lessThanPtr.value
    
    greaterThanPtr = greaterThanPtr.next

t1 = Node(3)
t1.next = Node(5)
t1.next.next = Node(8)
t1.next.next.next = Node(5)
t1.next.next.next.next = Node(4)
t1.next.next.next.next.next = Node(10)
t1.next.next.next.next.next.next = Node(2)
t1.next.next.next.next.next.next.next = Node(1)
  
linkedListPartition(t1, 5)

while t1 is not None:
  print(t1.value)
  t1 = t1.next