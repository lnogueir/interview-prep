'''
Prompt:
Implement a MyQueue class which implements a queue using two stacks
'''

class MyQueue:
  def __init__(self):
    self.enqueueStack = []
    self.dequeueStack = []
  
  def enqueue(self, value):
    self.enqueueStack.append(value)

  def dequeue(self):
    if len(self.dequeueStack) == 0:    
      while len(self.enqueueStack) > 0:
        self.dequeueStack.append(self.enqueueStack.pop())
    
    return self.dequeueStack.pop()

  def empty(self):
    return len(self.enqueueStack) == 0 and len(self.dequeueStack) == 0


q = MyQueue()
q.enqueue(3)
q.enqueue(5)
q.enqueue(2)
q.enqueue(8)
print(q.dequeue())
print(q.dequeue())
q.enqueue(7)
print(q.dequeue())
while not q.empty():
  print(q.dequeue())