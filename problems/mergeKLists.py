'''
Prompt: 
Merge K Sorted Linked Lists in-place

     j
0 -> 2 -> 5

i
1 -> 2 -> 3

current = 0

0 -> 1 -> 2 -> 2 -> 3 -> 5
'''

from nodes import SinglyLinkedListNode as Node
import heapq

# O(n*k*log(k)) where k = # of lists, n = # of nodes in the longest list
def mergeKLists(lists):
  k = len(lists)
  dummyHead = Node(None)
  currentNode = dummyHead

  minHeap = [(head.value, i) for i, head in enumerate(lists)]
  heapq.heapify(minHeap)

  while len(minHeap) > 0:
    _, minNodeIdx = heapq.heappop(minHeap)
    
    currentNode.next = lists[minNodeIdx]
    currentNode = currentNode.next
    lists[minNodeIdx] = lists[minNodeIdx].next
    if lists[minNodeIdx] is not None:
      heapq.heappush(minHeap, (lists[minNodeIdx].value, minNodeIdx))

  return dummyHead.next

l1 = Node(5)
l1.next = Node(7)
l1.next.next = Node(9)
l2 = Node(2)
l2.next = Node(3)
l2.next.next = Node(10)

merged = mergeKLists([l1, l2])
while merged != None:
  print(merged.value)
  merged = merged.next
