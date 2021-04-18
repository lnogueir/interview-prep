'''
Prompt:
Given a list of weights [w1, w2, w3, ..., wn] 
determine all sums that can be constructed using the weights
'''

# A brute force solution would be to generate the
# powerset and then compute the sum for each subset

## Optimal solution:
# Time: O(W)
# Space: O(W)
# where W is the max sum of the weights 
##

class Solver():
  def __init__(self):
    self.possibleSums = set([])
  
  def solve(self, weights, currentSum = 0, currentIdx = 0):
    self.possibleSums.add(currentSum)

    if currentIdx >= len(weights):
      return

    for idx in range(currentIdx, len(weights)):
      self.solve(weights, currentSum + weights[idx], idx + 1)

def knapsackProblem(weights):
  solver = Solver()
  solver.solve(weights)
  return list(solver.possibleSums)
  
print(sorted(knapsackProblem([1,3,3,5])))
# print(sorted(knapsackProblem([1,3,6])))