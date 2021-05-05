'''
Prompt:
Write a function `countConstruct(target, wordBank)` that accepts a target
string and an array of strings.

The function should return the number of ways that the `target` can be
constructed by concatenating elemements of the `wordBank`.

You may reuse elements of `wordBank` as many times as needed.
'''

def countConstruct(target, wordBank, current='', cache=None):
  if cache is None:
    cache = {}

  if current in cache:
    return cache[current]

  if current == target:
    return 1

  if len(current) > len(target) or current != target[:len(current)]:
    return 0

  counter = 0
  for word in wordBank:
    counter += countConstruct(target, wordBank, current + word, cache)

  cache[current] = counter
  return counter

print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', 
                ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))