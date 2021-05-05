'''
Prompt:
Given an array of words, construct a trie representing this array of words.

Consider '#' to be a terminating character.

Ex: ['cat', 'car', 'dog', 'd']
                                  ''
                              'c'     'd'
                            'a'     'o'  '#'
                          'r' 't'   'g'
                          '#' '#'   '#'

'''

class TrieNode:
	TERMINATING_CHAR = '#'
	def __init__(self, character=''):
		self.char = character
		self.children = {}
		
def buildTrie(listOfWords):
  trie = TrieNode()
  for word in listOfWords:
    curr = trie
    for c in word:
      if c not in curr.children:
        curr.children[c] = TrieNode(c)
      curr = curr.children[c]
    curr.children[TrieNode.TERMINATING_CHAR] = True
  return trie

def printWordsInTrie(trie, currentWord=None):
  if currentWord is None:
    currentWord = []

  for c in trie.children:
    if c == TrieNode.TERMINATING_CHAR:
      print(''.join(currentWord))
    else:
      currentWord.append(c)
      printWordsInTrie(trie.children[c], currentWord)
      currentWord.pop()

if __name__ == '__main__':
  t1 = buildTrie(["cat", "car", "dog", "d"])
  print('t1: ["cat", "car", "dog", "d"]')
  printWordsInTrie(t1)
  print('t2: ["3141", "5", "31", "2", "4159", "9", "42"]')
  t2 = buildTrie(["3141", "5", "31", "2", "4159", "9", "42"])
  printWordsInTrie(t2)
  t3 = buildTrie(["woooow"])
  print('t2: ["woooow"]')
  printWordsInTrie(t3)