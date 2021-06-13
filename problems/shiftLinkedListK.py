'''
Prompt:

Write a function that takes in the head of a Singly Linked List and an integer k,
shifts the list in place by k positions and returns its new head.

Ex:
input:
  head: 0 -> 1 -> 2 -> 3 -> 4 -> 5
  k = 2
output:
  4 -> 5 -> 0 -> 1 -> 2 -> 3
'''

from nodes import SinglyLinkedListNode as Node

def getLinkedListLength(head):
	size = 0
	while head != None:
		head = head.next
		size += 1
	return size

def shiftLinkedList(head, k):
	size = getLinkedListLength(head)
	nodeAhead = head
	if k % size == 0:
		return head
	
	for _ in range(k % size):
		nodeAhead = nodeAhead.next
	
	nodeBehind = head
	nodeBeforeBehind = None
	while nodeAhead != None:
		nodeAhead = nodeAhead.next
		nodeBeforeBehind = nodeBehind
		nodeBehind = nodeBehind.next
	
	nodeBeforeBehind.next = None
	
	nodeAhead = nodeBehind
	while nodeAhead.next != None:
		nodeAhead = nodeAhead.next
		
	nodeAhead.next, head = head, nodeBehind
	return head

LL = Node(0)
LL.next = Node(1)
LL.next.next = Node(2)
LL.next.next.next = Node(3)
LL.next.next.next.next = Node(4)
LL.next.next.next.next.next = Node(5)
r = shiftLinkedList(LL, 2)