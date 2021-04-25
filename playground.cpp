#include "data-structures/Heaps.hpp"
#include "data-structures/SegmentTrees.hpp"

/**
 * Playground to test data structures
 */
int main () {
  std::cout << "=============Heap Tests=============" << std::endl;
  MaxHeap mh = MaxHeap();
  std::array<Heap::Item, 4> items{{{4, "Lucas"}, {5, "Joao"}, {10, "Pedro"}, {3, "Antonio"}}};
  for (Heap::Item item: items) {
    mh.insert(item);
  }
  
  while (!mh.empty()) {
    std::optional<Heap::Item> maxItem = mh.extractMax();
    std::cout << *maxItem << std::endl;
  }

  std::cout << "=============SegmentTree Tests=============" << std::endl;
  SumSegmentTree st = SumSegmentTree({5, 8, 6, 3, 2, 7, 2, 6});
  std::cout << "(2, 7): " << st.query(2, 7) << std::endl;
  std::cout << "(0, 3): " << st.query(0, 3) << std::endl;
  std::cout << "(1, 4): " << st.query(1, 4) << std::endl;
  std::cout << "(5, 8): " << st.query(5, 8) << std::endl;
  return 0;
}