'''
Prompt:
You have an static array (values dont change between queries) 
and you want to make queries to find the sum of a 
given range from array.

Build a prefix sum table to perform queries in O(1).
'''

def buildPrefixSum(array):
  table = [0] * (len(array) + 1)
  for idx in range(1, len(array) + 1):
    table[idx] = table[idx-1] + array[idx-1]

  return table

class SumQuerier:
  def __init__(self, array):
    self.array = array
    self.prefixSum = buildPrefixSum(array)

  def query(self, a, b):
    return self.prefixSum[b+1] - self.prefixSum[a]
  
sq = SumQuerier([7,8,3,1])
print(sq.query(2,3))
print(sq.query(0,3))
print(sq.query(1,2))
print(sq.query(0,1))
print(sq.query(0,0))
