'''
Prompt:

Developers and Testers Integration

n: # of people in the meeting
d: max # of developers that can sit consecutively
t: max # of testers that can sit consecutively

Goal is to find how many ways you can rearrange the meeting.

Example:
n=5
d=2
t=2

DTDTD
DTTDT
TTDTD
TDTDT
'''

# Time: O(2^n), Space: O(n)
def helperTeam(d, t, n, initialD, initialT):
  if n == 0:
    return 1

  resultCount = 0

  if d > 0:
    resultCount += helperTeam(d - 1, initialT, n - 1, initialD, initialT)

  if t > 0:
    resultCount += helperTeam(initialD, t - 1, n - 1, initialD, initialT)

  return resultCount
    
def formTeam(d, t, n): 
	return helperTeam(d, t, n, d, t)
