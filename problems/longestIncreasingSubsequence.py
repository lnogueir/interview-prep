'''
Prompt:

Find the maximum-length sequence of array elements from left to right
where each element in the sequence is larger than the previous element.

ex:
input: [6, 2, 5, 1, 7, 4, 8, 3]
output: [2, 5, 7, 8]
'''

def longestIncreasingSubsequence(array):
  pass


# With dynamic programming
# Time: O(n^2), space: O(n)
def bruteForce(array):
  lengths = [1 for _ in array]
  n = len(array)
  for k in range(n):
    for i in range(0, k):
      if array[k] > array[i]:
        lengths[k] = max(lengths[k], lengths[i] + 1)

  return max(lengths)


t1 = [6, 2, 5, 1, 7, 4, 8, 3]
t2 = [3, 1, 2, 4]
t3 = [1]
t4 = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]
soln1 = bruteForce(t4)
soln2 = longestIncreasingSubsequence(t4)
print(soln1, soln2)
# print(longestIncreasingSubsequence(t2))

