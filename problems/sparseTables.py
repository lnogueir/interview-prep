'''
Prompt:
You have an static array (values dont change between queries) 
and you want to make queries to find the minimum value of a 
given range from array.

Build a sparse table to perform queries in O(1).

Complexity of sparse table: O(nlogn) time & space
'''

def findMaxPowerOf2Exp(n):
  exp = 0
  while True: # O(logn)
    n = n >> 1
    if n > 0:
      exp += 1
      continue
    break
  return exp

def buildSparseTables(array):
  exp = findMaxPowerOf2Exp(len(array))
  sparseTable = [[float('inf')]*len(array) for _ in range(exp+1)]
  for log in (1 << i for i in range(exp+1)):
    i = log // 2
    if i == 0:
      sparseTable[i] = [n for n in array]
      continue

    for j in range(len(array)-(log-1)):
      sparseTable[i][j] = min(sparseTable[i-1][j], sparseTable[i-1][j + (log >> 1)])

  return sparseTable

class MinQuerier:
  def __init__(self, array):
    self.array = array
    self.sparseTable = buildSparseTables(array)

  # finds the min value of range [a,b] from the array
  def query(self, a, b):
    rangeLength = b-a
    logIdx = findMaxPowerOf2Exp(rangeLength)
    return min(self.sparseTable[logIdx][a], self.sparseTable[logIdx][b - (1 << logIdx) + 1])

# print(buildSparseTables([3,4,7,5,1,8]))
mq = MinQuerier([3,4,7,5,1,8])
print(mq.query(0,5)) # 1
print(mq.query(2,4)) # 1
print(mq.query(0,3)) # 3
print(mq.query(2,3)) # 5
print(mq.query(2,5)) # 1
print(mq.query(1,3)) # 4
