#include "data-structures/heaps.hpp"

/**
 * Playground to test data structures
 */
int main () {
  MaxHeap mh = MaxHeap();
  std::array<Heap::Item, 4> items{{{4, "Lucas"}, {5, "Joao"}, {10, "Pedro"}, {3, "Antonio"}}};
  for (Heap::Item item: items) {
    mh.insert(item);
  }

  while (!mh.empty()) {
    std::optional<Heap::Item> maxItem = mh.extractMax();
    std::cout << *maxItem << std::endl;
  }
  
  return 0;
}