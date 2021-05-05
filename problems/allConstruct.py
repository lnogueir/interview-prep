'''
Prompt:
Write a function `allConstruct(target, wordBank)` that accepts a
target string and an array of string.

The function should return a 2D array containing all of the ways that
the `target` can be constructed by concatenating elements of the `wordBank`
array. Each element of the 2D array should represent one combination that
constructs the `target`.

You may reuse elements of `wordBank` as many times as needed.
'''

allConstructs = []
def allConstruct(target, wordBank, construct=[], cache=None):
  if cache is None:
    cache = set([])

  current = ''.join(construct)
  if current in cache:
    return False

  if current == target:
    allConstructs.append(construct)
    return True

  if len(current) > len(target) or current != target[:len(current)]:
    return False 

  wasItPossible = False
  for word in wordBank:
    wasItPossible |= allConstruct(target, wordBank, [*construct, word], cache)

  if not wasItPossible:
    cache.add(current)

  return wasItPossible

allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])
print(allConstructs)
allConstructs = []
allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl'])
print(allConstructs)
allConstructs = []
allConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', 
                ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])
print(allConstructs)
allConstructs = []
allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'])
print(allConstructs)