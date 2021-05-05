'''
Prompt:
Given a string representation of the first n digits of Pi and a list of
positive integers (all in string format), write a function that returns the
smallest number of spaces that can be added to the n digits of Pi such that
all resulting numbers (after adding the spaces) are found in the list of integers.

For example:

input: pi: "3141592", numbers: ["3141", "5", "31", "2", "4159", "9", "42"]
output: 2 # because: 31 | 4159 | 2

Also, note that a single number can appear multiple times in the resulting numbers.
For example, if Pi is "3141", and the numbers are ["1", "3", "4"], the number "1"

is allowed to appear twice in the list of resulting numbers after three spaces are added:
"3 | 1 | 4 | 1"
  
If no number of spaces to be added exists such that all resulting numbers are
found in the list of integers, the function should return -1
'''

from trieConstruction import TrieNode, buildTrie

class Solver:
  def __init__(self, numbers):
    self.trie = buildTrie(numbers)
  
  def minNumSpacesToAdd(self, digits, i=0):
    currentNode = self.trie
    failed = False
    sol = float('inf')
    for idx in range(i, len(digits)):
      digit = digits[idx]
      if TrieNode.TERMINATING_CHAR in currentNode.children:
        sol = min(1 + self.minNumSpacesToAdd(digits, idx), sol)

      if digit in currentNode.children:
        currentNode = currentNode.children[digit]
        continue

      failed = True
      break

    lastPartFound = TrieNode.TERMINATING_CHAR in currentNode.children
    return sol if failed or not lastPartFound else 0
    



def numbersInPi(pi, numbers):
  solver = Solver(numbers)
  result = solver.minNumSpacesToAdd(pi)
  return result if result != float('inf') else -1
  

    
  
print(numbersInPi("3141592", ["3141", "5", "31", "2", "4159", "9", "42"]))
print(numbersInPi("3141592653589793238462643383279", ["314159265358979323846", "26433", "8", "3279", "314159265", "35897932384626433832", "79"]))
