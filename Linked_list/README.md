# Linked List Implementation in Python

This project implements a singly linked list in Python, supporting common list operations like insertion, deletion, and searching.

## Features

- Add elements at the beginning, end, or a specific index.
- Remove elements by index or value.
- Access elements by index or retrieve the first/last element.
- Check if an element exists in the list.
- Replace elements at a specific index.
- Iterate through the list using a custom iterator.
- String representation for easy debugging.

## Usage Example

```python
from LinkedList import LinkedList

# Create a linked list
lst = LinkedList()
lst.add(1)
lst.add(2)
lst.add(3)

# Access and modify the list
print(lst)  # [1, 2, 3]
lst.set(1, 9)
print(lst)  # [1, 9, 3]
lst.remove(9)
print(lst)  # [1, 3]
Testing

Run the script to test the linked list:

python 18.3LinkedList.py
