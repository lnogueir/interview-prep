'''
Prompt:
You're given an array of arrays where each subarray holds two integer values
and represents an item; the first integer is the item's value, and the second
integer is the item's weight. You're also given an integer representing the
maximum capacity of a knapsack that you have.

Your goal is to fit items in your knapsack without having the sum of their weights 
exceed the knapsack's capacity, all that while maximizing their combined values. 
Note that you only have one of each item at your disposal.

Example:
input:
{
  "items": [
    [1, 2],
    [4, 3],
    [5, 6],
    [6, 7]
  ],
  "capacity": 10
}

output:
[10, [1, 3]] since items [4, 3] and [6, 7] will be maximum sum to 10.

'''


class Solver():
    def __init__(self):
      self.maxValue = 0
      self.indexes = []
		
    def solve(self, items, carryCapacity, carryValue=0, i=0, idxs = []):
      if carryCapacity < 0:
        return

      if carryValue > self.maxValue:
        self.maxValue = carryValue
        self.indexes = idxs

      for idx in range(i, len(items)):
        value, weight = items[idx]
        remainder = carryCapacity - weight
        self.solve(items, remainder, carryValue+value, idx+1, [*idxs, idx])
        continue
			

def knapsackProblem(items, capacity):
  solver = Solver()
  solver.solve(items, capacity)
  return [
    solver.maxValue,
    solver.indexes
  ]

print(knapsackProblem([
    [1, 2],
    [4, 3],
    [5, 6],
    [6, 7]
  ], 10))

print(knapsackProblem([
  [1, 3],
  [4, 5],
  [5, 2],
  [6, 4]
], 8))
