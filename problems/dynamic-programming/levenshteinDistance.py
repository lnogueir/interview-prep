'''
Prompt:
Write a function that takes in two strings and returns the minimum number of
edit operations that need to be performed on the first string to obtain the
second string.

There are three edit operations: insertion of a character, deletion of a 
character, and substitution of a character for another.
'''

def minEditDistance(src, dst, a, b, cache=None):
  if cache is None:
    cache = {}
  
  if (a,b) in cache:
    return cache[(a,b)]

  if a == -1 and b == -1:
    return 0
  
  if a == -1:
    return b + 1
  
  if b == -1:
    return a + 1

  if src[a] == dst[b]:
    cache[(a,b)] = minEditDistance(src, dst, a-1, b-1)
  else:
    replace = minEditDistance(src, dst, a-1, b-1)
    insert = minEditDistance(src, dst, a-1, b)
    delete = minEditDistance(src, dst, a, b-1)
    cache[(a,b)] = min(replace, insert, delete) + 1

  return cache[(a,b)]

def levenshteinDistance(src, dst):
  return minEditDistance(src, dst, len(src)-1, len(dst)-1)



print(levenshteinDistance('abc', 'yabd')) # 2
print(levenshteinDistance('lucas', 'ucxs')) # 2
print(levenshteinDistance('cool', 'cxx')) # 3
