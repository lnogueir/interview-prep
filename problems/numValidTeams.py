'''
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
Example 3:

Input: rating = [1,2,3,4]
Output: 4
'''

class Solution():
    def isValidTeam(self, ratings, i, j, k):
        N = len(ratings)
        if i >= N or j >= N or k >= N:
          return False
        
        return (ratings[i] < ratings[j] < ratings[k]) or (ratings[k] < ratings[j] < ratings[i])
    
    def numTeams(self, ratings, i=0, j=1, k=2, visited = None):
        if visited is None:
            visited = set([])
            
        if (i, j, k) in visited:
            return 0
        
        visited.add((i, j, k))
        
        solutions = 0
        if self.isValidTeam(ratings, i, j, k):
            solutions += 1
          
        # print('Is ', i, j, k, 'valid:', bool(solutions))
        
        if k + 1 < len(ratings):
          solutions += self.numTeams(ratings, i, j, k+1, visited)
        
        if j + 1 < k:
            solutions += self.numTeams(ratings, i, j+1, k, visited)
        
        if i + 1 < j:
            solutions += self.numTeams(ratings, i+1, j, k, visited)
            
        return solutions

print(Solution().numTeams([2,5,3,4,1]))