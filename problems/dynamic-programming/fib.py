'''
Prompt:
Write a function `fib(n)` that takes in a number as an argument.

The function should return the n-th number of the Fibonacci sequence.
'''

def sillyFib(n):
  if n == 0:
    return 0
  
  if n == 1:
    return 1
  
  return sillyFib(n-1) + sillyFib(n-2)

# dynamic programming with memoization
def fib(n, cache=None):
  if cache is None:
    cache = {}

  if n in cache:
    return cache[n]

  if n == 0:
    return 0

  if n == 1:
    return 1

  cache[n] = fib(n-1, cache) + fib(n-2, cache)
  return cache[n]

# dynamic programming with tabulation
def fib_tabulation(n):
  table = [0] * (n+1)
  table[1] = 1

  for i in range(2, n+1):
    table[i] = table[i-1] + table[i-2]
  
  return table[-1]

print(fib(50))
print(fib_tabulation(50))