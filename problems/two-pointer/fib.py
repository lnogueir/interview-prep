'''
Prompt:
Compute Nth fibonnaci number.

Goal: time: O(n), space: O(1)
'''

def fib(n):
  if n == 0:
    return 0

  if n == 1:
    return 1

  prevOfPrev = 0 # fib(n-2)
  prev = 1 # fib(n-1)
  sol = prevOfPrev + prev
  i = 2
  for _ in range(2, n):
    prevOfPrev = prev
    prev = sol
    sol = prevOfPrev + prev
    
  return sol

print(fib(3))
print(fib(5))
print(fib(6))
print(fib(8))
print(fib(13))