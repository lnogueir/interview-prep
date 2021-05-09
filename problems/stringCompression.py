'''
Prompt:
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
'''
def stringCompression(string):
  charCounter = 0
  currentChar = ''
  compressedString = []
  for c in string:
    if c == currentChar:
      charCounter += 1
    else:
      if charCounter > 0:
        compressedString.append(currentChar)
        compressedString.append(str(charCounter))
      currentChar = c
      charCounter = 1

  if charCounter > 0:
    compressedString.append(currentChar)
    compressedString.append(str(charCounter))

  return ''.join(compressedString) if len(compressedString) < len(string) else string

print(stringCompression('aabcccccaaa'))
print(stringCompression('aabcccccqqtaaaaaaa'))
print(stringCompression('abcdef'))


