# Heap Implementation and Heap Sort

This project includes:
1. **Min-Heap Implementation**: A custom min-heap data structure.
2. **Heap Sort Algorithm**: A sorting algorithm built using the min-heap.

## Features

### Min-Heap
- Add elements while maintaining the heap property.
- Remove and retrieve the smallest element efficiently.
- Retrieve the heap size and check if it's empty.
- Peek at the smallest element without removal.

### Heap Sort
- Sorts a list of integers in ascending order.
- Utilizes the min-heap for sorting.

## Usage

### Min-Heap
```python
from Min_heap_class import Heap

heap = Heap()
heap.add(10)
heap.add(5)
heap.add(15)
print(heap.peek())  # Output: 5
print(heap.remove())  # Output: 5
Heap Sort
Run the heap sort program:

python 17.3Min_heap.py
Input a list of integers separated by spaces. The program sorts the list and displays the result.

Example:

Enter a list of integers separated by spaces: 5 3 8 1
Your input:
[5, 3, 8, 1]
Sorted:
1 3 5 8
Requirements

Python 3.x
