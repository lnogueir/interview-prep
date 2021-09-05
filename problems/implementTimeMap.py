'''
Prompt:
Write a map implementation with a get function that lets you retrieve the value of a key at a particular time.
It should contain the following methods:
•	set(key, value, time): sets key to value for t = time.
•	get(key, time): gets the key at t = time.

The map should work like this. If we set a key at a particular time, 
it will maintain that value forever or until it gets set at a later time. 
In other words, when we get a key at a time, 
it should return the value that was set for that key set at the most recent time.

Consider the following examples:
d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 2) # set key 1 to value 2 at time 2
d.get(1, 1) # get key 1 at time 1 should be 1
d.get(1, 3) # get key 1 at time 3 should be 2
d.set(1, 1, 5) # set key 1 to value 1 at time 5
d.get(1, 0) # get key 1 at time 0 should be null
d.get(1, 10) # get key 1 at time 10 should be 1
d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 0) # set key 1 to value 2 at time 0
d.get(1, 0) # get key 1 at time 0 should be 2
'''

'''
My Solution:

If `set` is always called with a `time` greater than the previous time set, then:
Use a hash table to map keys to an array of pairs representing the values and their respective times.
Since the condition above is true, then this array is sorted based on time. Therefore, `set` is O(1)
and `get` would be O(logn), we could simply do a binary search to find the time lower bound to get the right value.

If the condition above isn't true, then we could use an AVL tree to keep the keys sorted by time. Each node
of the AVL tree contains a pair of the time and value. In this case, `set` is O(logn), since that's the cost of 
insertion on AVL tree. And `get` is still O(logn), because that's the time required to search the time lower bound in the
tree.
'''
  
