'''
Prompt:
Given an m x n binary matrix filled with 0's and 1's, 
find the largest square containing only 1's and return its area.

Ex:
matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]
Output: 4
'''

# Time: O(m*n), Space: O(m*n)
def maximalSquare(matrix):
    m = len(matrix)
    if m == 0:
        return 0
    n = len(matrix[0])
    
    dp = [([0] * n) for _ in range(m)]
    maxLen = 0 
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "1":
                dp[i][j] = 1
                if i > 0 and j > 0:
                    dp[i][j] += min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                
                maxLen = max(maxLen, dp[i][j])

    return maxLen * maxLen

t1 =  [["1","1","1","1","0"],
       ["1","1","1","1","0"],
       ["1","1","1","1","1"],
       ["1","1","1","1","1"],
       ["0","0","1","1","1"]]

print(maximalSquare(t1))
