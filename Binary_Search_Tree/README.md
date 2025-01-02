# Binary Search Tree (BST) Implementation

This repository contains a Python implementation of a binary search tree (BST) that supports insertion, deletion, search, and traversal operations. The tree maintains elements in sorted order, and an iterator is provided for in-order traversal.

## Features

- **Insertion**: Add elements to the tree while maintaining the BST property.
- **Deletion**: Remove elements from the tree.
- **Search**: Check whether an element exists in the tree.
- **Traversals**: Perform in-order, pre-order, and post-order traversals.
- **Path Retrieval**: Retrieve the path from the root to a specified element.
- **Iterator Support**: Use Python's iterator protocol for in-order traversal.

## Usage Example

```python
# Create a binary search tree
tree = BST()

# Insert elements
tree.insert(10)
tree.insert(5)
tree.insert(15)

# Search for elements
print(tree.search(10))  # Output: True
print(tree.search(20))  # Output: False

# Traversal
tree.inorder()  # Output: 5 10 15
tree.preorder()  # Output: 10 5 15
tree.postorder()  # Output: 5 15 10

# Delete an element
tree.delete(10)
print(list(tree))  # Output: [5, 15] (in-order traversal)
Class Details

class BST
Core Methods

insert(e): Inserts an element e into the tree.
delete(e): Deletes an element e from the tree.
search(e): Searches for an element e in the tree.
getRoot(): Returns the root node of the tree.
Traversals

inorder(): Performs an in-order traversal.
preorder(): Performs a pre-order traversal.
postorder(): Performs a post-order traversal.
Utilities

path(e): Returns the path from the root to the specified element.
clear(): Removes all elements from the tree.
__iter__(): Returns an iterator for in-order traversal.
Testing

Run the script and input integers separated by spaces to test the BST implementation. For example:

python BST_iterator.py
Example input:

Enter integers in one line for tree separated by space: 10 5 15 3 7
Example output:

10 5 15 3 7 are inserted into the tree
Traverse the elements in this order: 3 5 7 10 15 All traversed
