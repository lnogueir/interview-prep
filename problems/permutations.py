'''
Prompt:
Given a string return an array of all its permutations.
'''

def permutations(string):
  solutions = []
  def _permutations(string, i=0):
    if i == len(string):
      solutions.append(''.join(string))
      return
    
    for idx in range(i, len(string)):
      string[idx], string[i] = string[i], string[idx]
      _permutations(string, i+1)
      string[idx], string[i] = string[i], string[idx]

  _permutations([c for c in string])
  return solutions

if __name__ == '__main__':
  t1 = 'abc'
  print(permutations(t1))