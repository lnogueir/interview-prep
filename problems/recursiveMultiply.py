'''
Write a recursive function to multiply two positive integers without using the
*operator.You can use addition, subtraction, and bit shifting, but you should minimize the number
of those operations.
'''

def previousPowerOfTwoExponent(n):
  exp = 0
  while 1 << exp <= n:
    exp += 1

  return exp - 1

def recursiveMultiply(a, b):
  if b == 0:
    return 0
  
  exp = previousPowerOfTwoExponent(b)
  remainder = b - (1 << exp)
  return (a << exp) + recursiveMultiply(a, remainder)

def recursiveMultiplyBetter(a, b):
  if b > a:
    return recursiveMultiplyBetter(b, a)
  
  if b == 0:
    return 0

  if b == 1:
    return a

  halvedMultiplier = b >> 1
  halvedResult = recursiveMultiplyBetter(a, halvedMultiplier)
  if halvedMultiplier % 2 == 0:
    return halvedResult + halvedResult
  
  return halvedResult + halvedResult + a


print(recursiveMultiplyBetter(3,93))
print(recursiveMultiply(3,93))
