'''
Prompt:
	Given a collection of closed intervals, merge all overlapping intervals.
	Ex: mergeIntervals(([[1,4],[7,8], [2,5], ]) == [[1,5], [7,8]]
'''

# Time: O(nlogn), Space: O(n), though one could argue O(1) space
def mergeIntervals(intervals):
  mergedIntervals = []
  intervals.sort(key=lambda item: item[0])
  currentInterval = []
  upperBound = -1
  for interval in intervals:
    left, right = interval
    if len(currentInterval) == 0:
      currentInterval.append(left)
      upperBound = right
      continue
    
    if left <= upperBound:
      upperBound = right
    else:
      currentInterval.append(upperBound)
      mergedIntervals.append(currentInterval)
      currentInterval = [left]

  if len(currentInterval) != 0:
      currentInterval.append(intervals[-1][1])
      mergedIntervals.append(currentInterval)

  return mergedIntervals
  
t1 = [[2,5], [5, 6], [1,4], [7,8]]
print(mergeIntervals(t1))

t2 = [[1,4], [2,5], [7,8]]
print(mergeIntervals(t2))

