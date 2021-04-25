#include <vector>
#include <cmath>
#include <algorithm>
#include <iostream>

/**
 * @class SegmentTree
 * 
 * Useful to perform queries on a non-static array.
 * Sum Segment Tree for the array [5, 8, 6, 3]:
 *                             22|1   (value|index)
 *                           /      \
 *                         13|2      9|3
 *                         /   \    /   \
 *                       5|4   8|5 6|6  3|7
 * Notes:
 * - Tree is 1-indexed
 * - parent(i) = floor(i / 2)
 * - left(i) = 2*i
 * - right(i) = 2*i + 1
 */
class SegmentTree {
 public:
  /**
   * Updates value of array at idx with newValue based 
   * on specific segment tree operation.
   */
  virtual void update(int idx, int newValue) = 0;

  /**
   * Queries the range (a, b) inclusive based on the specific 
   * segment tree operation.
   */
  virtual int query(int a, int b) const = 0;
 protected:
  SegmentTree(std::vector<int> array): 
    // expression below just finds next power of 2 of the array size
    arrayOffset((int)pow(2, ceil(log(array.size())/log(2)))),
    // expression below just finds next power of 2 of the array size times 2
    tree(pow(2, 1 + ceil(log(array.size())/log(2))) - 1) {}
  
  /**
   * The structure holding the segment tree.
   */
  std::vector<int> tree;

  /**
   * Equivalent to tree.size() / 2.
   */
  const int arrayOffset;
};

class SumSegmentTree : public SegmentTree {
 public:
  SumSegmentTree(std::vector<int> array) : SegmentTree(array) {
    std::fill(tree.begin(), tree.end(), 0);
    for (int i = 0; i < array.size(); i++) {
      update(i, array[i]);
    }
  }

  void update(int arrayIdx, int newValue) override {
    int treeIdx = arrayOffset + arrayIdx;
    tree[treeIdx - 1] = newValue;
    treeIdx /= 2;
    while (treeIdx >= 1) {
      int leftChildIdx = 2*treeIdx;
      int rightChildIdx = 2*treeIdx + 1;
      tree[treeIdx - 1] = tree[leftChildIdx - 1] + tree[rightChildIdx - 1];
      treeIdx /= 2;
    }
  }

  int query(int a, int b) const override {
    a += arrayOffset;
    b += arrayOffset;
    int sum = 0;

    // The idea here is that odd indexes are terminating a segment
    // while even indexes are the start of a segment. Therefore, we
    // only sum from the `a` if index is odd, since it terminates
    // that segment, and we won't be able to get it from parent.
    // Similarly, we only sum from the `b` index if it's even, or else
    // we would potentially be summing things multiple times.
    while (a <= b) {
      if (a%2 == 1) sum += tree[a++ - 1];
      if (b%2 == 0) sum += tree[b-- - 1];
      a /= 2; b /= 2;
    }
    return sum;
  }
};