'''
Prompt:
Given an array of distinct positive integers representing coin denominations
and a single non-negative integer n, write a function that returns the number
of ways to make change using the given coin denominations.

Note you can use an unlimited amount of each coin denomination, but your
solution may not contain duplicates.

i.e: input: n = 6, denoms = [1, 5] -> output: 2
Should not count 1+5, 5+1.
'''

# Time: O(n*d), Space: O(n*d)
def numWaysToMakeChange(n, coins):
  dpTable = [[0]*(n+1) for _ in range(len(coins)+1)]
  dpTable[0][0] = 1

  for i in range(1, len(dpTable)):
    for j in range(n+1):
      dpTable[i][j] += dpTable[i-1][j]

      remainder = j - coins[i-1]
      if remainder >= 0:
        dpTable[i][j] += dpTable[i][remainder]

  return dpTable[-1][-1]

print(numWaysToMakeChange(6, [1, 5]))

        
