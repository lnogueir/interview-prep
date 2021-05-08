'''
Given a string return true if it's a palindrome, false otherwise.
'''

def isPalindrome(string):
  left = 0
  right = len(string)-1
  while left < right:
    if string[left] != string[right]:
      return False
    left += 1
    right -= 1

  return True


if __name__ == '__main__':
  print(isPalindrome('abcba'))
  print(isPalindrome('abc'))
  print(isPalindrome('abccba'))

