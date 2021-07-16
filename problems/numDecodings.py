'''
Prompt:
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

'''

def numDecodings(s, i=0, cache=None):
  if cache is None:
      cache = {}
      
  if i in cache:
      return cache[i]
  
  if i == len(s):
      return 1
  
  if s[i] == '0':
      return 0

  solutions = numDecodings(s, i+1, cache)

  if i+1 < len(s) and (s[i] == '1' or (s[i] == 2 and int(s[i+1]) <= 6)):
    solutions += numDecodings(s, i+2, cache)
  
  cache[i] = solutions
  return solutions
  
print(numDecodings("2611055971756562"))

# 2 6 11 0
# 2 6 1 1
# 2 6 1 10 5 59
    
        
        