'''
Prompt:
Write a function to flatten a nested dictionary. Namespace the keys with a period.
For example, given the following dictionary:
{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

it should become:
{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
You can assume keys do not contain dots in them, i.e. no clobbering will occur.
'''

class Solver:
  def __init__(self):
    self.flattenedDictionary = {}
  
  def flattenDictionary(self, dictionary, prefix=''):
    for key in dictionary:
      if type(dictionary[key]) is dict:
        self.flattenDictionary(dictionary[key], prefix + key + '.')
      else:
        self.flattenedDictionary[prefix + key] = dictionary[key]

d1 = {
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

d2 = {
  't1': 0,
  't2': {
    'cool': {
      'wow': {
        'what': {
          'nice': 'cool'
        }
      }
    }
  },
  't3': None
}

s1 = Solver()
s1.flattenDictionary(d1)
print(s1.flattenedDictionary)
s2 = Solver()
s2.flattenDictionary(d2)
print(s2.flattenedDictionary)
    
