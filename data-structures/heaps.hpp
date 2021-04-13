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

  bool empty() const {
    return heap.empty();
  }

 protected:
  /**
   * Corrects a single heap violation starting from leaf going upwards.
   * @returns true if corrected a violation, false if no violation was found.
   */
  virtual bool bubbleUp(int nodeIdx) = 0;

  /**
   * Corrects a single heap violation starting from parent going downwards.
   * @returns idx of the node which swap fixed violation, -1 if no violation was found.
   */
  virtual int bubbleDown(int parentIdx) = 0;

  std::vector<Item> heap;
};

class MaxHeap final: public Heap {
 public:
  void insert(Item item) override{
    heap.push_back(item);
    int nodeIdx = heap.size();
    while (bubbleUp(nodeIdx)) {
      nodeIdx = nodeIdx / 2;
    }
  }

  std::optional<Item> max() const {
    return heap.size() > 0 ? std::optional<Item>{heap[0]} : std::nullopt;
  }

  std::optional<Item> extractMax() {
    std::optional<Item> maxItem = max();
    if (maxItem) {
      Item last = heap.back();
      heap[0] = last;
      heap.pop_back();
      int parentIdx = 1;
      while ((parentIdx = bubbleDown(parentIdx)) != -1) {}
    }

    return maxItem;
  }
 private:
  int bubbleDown(int parentIdx) override {
    int leftNodeIdx = 2*parentIdx;
    int rightNodeIdx = 2*parentIdx + 1;
    int actualParentIdx = parentIdx - 1;
    int actualLeftNodeIdx = leftNodeIdx - 1;
    int actualRightNodeIdx = rightNodeIdx - 1;

    if (actualLeftNodeIdx >= heap.size()) {
      return -1;
    }

    bool isLeftMoreImportantThanRight = actualRightNodeIdx >= heap.size() || 
                               heap[actualLeftNodeIdx].priority > heap[actualRightNodeIdx].priority;

    Item parentItem = heap[actualParentIdx];
    if (isLeftMoreImportantThanRight) {
      if (heap[actualParentIdx].priority < heap[actualLeftNodeIdx].priority) {
        heap[actualParentIdx] = heap[actualLeftNodeIdx];
        heap[actualLeftNodeIdx] = parentItem;
        return leftNodeIdx;
      }
    } else {
      if (heap[actualParentIdx].priority < heap[actualRightNodeIdx].priority) {
        heap[actualParentIdx] = heap[actualRightNodeIdx];
        heap[actualRightNodeIdx] = parentItem;
        return rightNodeIdx;
      }
    }

    return -1;
  }

  bool bubbleUp(int nodeIdx) override {
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