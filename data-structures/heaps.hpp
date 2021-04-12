#include <array>
#include <iostream>
#include <cmath>
#include <optional>
#include <vector>

/**
 * Recall nodes are indexed starting at 1.
 * Properties:
 * parent(idx) = floor(idx / 2)
 * left(idx) = 2*idx
 * right(idx) = 2*idx + 1
 */
class Heap {
 public:
  struct Item {
    int priority;
    std::string key;
    friend std::ostream& operator<<(std::ostream& os, const Item& item);
  };

  virtual void insert(Item item) = 0;

 protected:
  /**
   * Swaps node with parent if needed
   * @returns true if node was swapped, otherwise false.
   */
  virtual bool swapWithParent(int nodeIdx) = 0;

  /**
   * Updates parent node with children appropriately
   * @returns idx of the node it update to. -1 if not updated
   */
  virtual int updateParent(int parentIdx) = 0;

  std::vector<Item> heap;
};

class MaxHeap final: public Heap {
 public:
  void insert(Item item) override{
    heap.push_back(item);
    int nodeIdx = heap.size();
    while (swapWithParent(nodeIdx)) {
      nodeIdx = nodeIdx / 2;
    }
  }

  std::optional<Item> max() {
    return heap.size() > 0 ? std::optional<Item>{heap[0]} : std::nullopt;
  }

  std::optional<Item> extractMax() {
    std::optional<Item> maxItem = max();
    if (maxItem) {
      int parentIdx = 1;
      while (parentIdx != -1) {
        parentIdx = updateParent(parentIdx);
      }
      heap.pop_back();
    }

    return maxItem;
  }
 private:
  int updateParent(int parentIdx) override{
    int leftNodeIdx = 2*parentIdx;
    int rightNodeIdx = 2*parentIdx + 1;
    int actualParentIdx = parentIdx - 1;
    int actualLeftNodeIdx = leftNodeIdx - 1;
    int actualRightNodeIdx = rightNodeIdx - 1;

    if (actualLeftNodeIdx >= heap.size()) {
      return -1;
    }

    bool isLeftMoreImportant = actualRightNodeIdx >= heap.size() || 
                               heap[actualLeftNodeIdx].priority > heap[actualRightNodeIdx].priority;

    heap[actualParentIdx] =  isLeftMoreImportant ? heap[actualLeftNodeIdx] : heap[actualRightNodeIdx];
    return isLeftMoreImportant ? actualLeftNodeIdx : actualRightNodeIdx;
  }

  bool swapWithParent(int nodeIdx) override{
    int parentIdx = nodeIdx / 2;
    int actualNodeIdx = nodeIdx - 1;
    int actualParentIdx = parentIdx - 1;
    if (actualNodeIdx > 0 && heap[actualParentIdx].priority < heap[actualNodeIdx].priority) {
      Item tmp = heap[actualParentIdx];
      heap[actualParentIdx] = heap[actualNodeIdx];
      heap[actualNodeIdx] = tmp;
      return true;
    }
    return false;
  }
};

std::ostream& operator<<(std::ostream& os, const Heap::Item& item) {
  os << "Priority: " << item.priority << " - Key: " << item.key;
  return os;
}