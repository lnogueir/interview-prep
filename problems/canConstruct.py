'''
Prompt:
Write a function `canConstruct(target, wordBank)` that accepts
a target sring and an array of strings.

The function should return a boolean indicating whether or not the
`target` can be constructed by concatenating elements of the `wordBank`
array.
'''

def canConstruct(target, wordBank, current='', cache=None):
  if cache is None:
    cache = set([])

  if current in cache:
    return False

  if current == target:
    return True

  if len(current) > len(target) or current != target[:len(current)]:
    return False

  for word in wordBank:
    if canConstruct(target, wordBank, current + word, cache):
      return True
  
  cache.add(current)
  return False

print(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) # False
print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) # True

print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', 
                ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])) # False