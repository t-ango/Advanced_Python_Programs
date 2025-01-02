"""
Binary Search Tree (BST) Implementation

This script implements a binary search tree (BST) in Python with support for common operations such as insertion, deletion, and traversal. The BST maintains elements in sorted order and supports an iterator for in-order traversal.

Classes:
    - BST: Represents the binary search tree.
    - TreeNode: Represents a single node in the BST.

Key Methods in BST:
    - insert(e): Inserts an element into the tree.
    - delete(e): Deletes an element from the tree.
    - search(e): Searches for an element in the tree.
    - inorder(): Performs an in-order traversal of the tree.
    - preorder(): Performs a pre-order traversal of the tree.
    - postorder(): Performs a post-order traversal of the tree.
    - path(e): Returns the path from the root to a specified element.
    - getRoot(): Returns the root of the tree.
    - clear(): Clears the tree, removing all elements.
    - __iter__(): Returns an iterator for in-order traversal.

Usage Example:
    >>> tree = BST()
    >>> tree.insert(10)
    >>> tree.insert(5)
    >>> tree.insert(15)
    >>> print(tree.search(10))  # Output: True
    >>> print(tree.search(20))  # Output: False
    >>> tree.delete(10)
    >>> print(list(tree))  # Output: [5, 15] (in-order traversal)
"""

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    # Return True if the element is in the tree 
    def search(self, e):
        current = self.root # Start from the root

        while current != None:
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else: # element matches current.element
                return True # Element is found

        return False
    
    # Insert element e into the binary search tree
    # Return True if the element is inserted successfully 
    def insert(self, e):
        if self.root == None:
            self.root = self.createNewNode(e) # Create a new root
        else:
            # Locate the parent node
            parent = None
            current = self.root
            while current != None:
                if e < current.element:
                    parent = current
                    current = current.left
                elif e > current.element:
                    parent = current
                    current = current.right
                else:
                    return False # Duplicate node not inserted

            # Create the new node and attach it to the parent node
            if e < parent.element:
                parent.left = self.createNewNode(e)
            else:
                parent.right = self.createNewNode(e)

        self.size += 1 # Increase tree size
        return True # Element inserted

    # Create a new TreeNode for element e
    def createNewNode(self, e):
        return TreeNode(e)

    # Return the size of the tree
    def getSize(self):
        return self.size
    
    # Inorder traversal from the root
    def inorder(self):
        self.inorderHelper(self.root)

    # Inorder traversal from a subtree 
    def inorderHelper(self, r):
        if r != None:
            self.inorderHelper(r.left)
            print(r.element, end = " ")
            self.inorderHelper(r.right)

    # Postorder traversal from the root 
    def postorder(self):
        self.postorderHelper(self.root)

    # Postorder traversal from a subtree 
    def postorderHelper(self, root):
        if root != None:
            self.postorderHelper(root.left)
            self.postorderHelper(root.right)
            print(root.element, end = " ")

    # Preorder traversal from the root 
    def preorder(self):
        self.preorderHelper(self.root)

    # Preorder traversal from a subtree 
    def preorderHelper(self, root):
        if root != None:
            print(root.element, end = " ")
            self.preorderHelper(root.left)
            self.preorderHelper(root.right)

    # Returns a path from the root leading to the specified element 
    def path(self, e):
        list = []
        current = self.root # Start from the root

        while current != None:
            list.append(current) # Add the node to the list
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else:
                break

        return list # Return an array of nodes

    # Delete an element from the binary search tree.
    # Return True if the element is deleted successfully
    # Return False if the element is not in the tree 
    def delete(self, e):
        # Locate the node to be deleted and its parent node
        parent = None
        current = self.root
        while current != None:
            if e < current.element:
                parent = current
                current = current.left
            elif e > current.element: 
                parent = current
                current = current.right
            else:
                break # Element is in the tree pointed by current

        if current == None:
            return False # Element is not in the tree

        # Case 1: current has no left children
        if current.left == None:
            # Connect the parent with the right child of the current node
            if parent == None:
                self.root = current.right
            else:
                if e < parent.element:
                    parent.left = current.right
                else:
                    parent.right = current.right
        else:
            # Case 2: The current node has a left child
            # Locate the rightmost node in the left subtree of
            # the current node and also its parent
            parentOfRightMost = current
            rightMost = current.left

            while rightMost.right != None:
                parentOfRightMost = rightMost
                rightMost = rightMost.right # Keep going to the right

            # Replace the element in current by the element in rightMost
            current.element = rightMost.element

            # Eliminate rightmost node
            if parentOfRightMost.right == rightMost:
                parentOfRightMost.right = rightMost.left
            else:
                # Special case: parentOfRightMost == current
                parentOfRightMost.left = rightMost.left     

        self.size -= 1
        return True # Element deleted

    # Return true if the tree is empty
    def isEmpty(self):
        return self.size == 0
        
    # Remove all elements from the tree
    def clear(self):
        self.root = None
        self.size = 0

    # Return the root of the tree
    def getRoot(self):
        return self.root
    

    def __iter__(self):
        stack = []
        current = self.root
        
        #go down to the smallest element which is leftmost node:
        while current:
            stack.append(current)
            current = current.left

        #Remove elements from the stack starting with the smallest one
        #When popping the element keep its value and go to its right subtree
        #go to the left first to retrieve elements of the right subtree in accending order
        while stack:
            node = stack.pop()
            yield node.element 
            
            current = node.right
            while current:
                stack.append(current)
                current = current.left


class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None  # Point to the left node, default None
        self.right = None # Point to the right node, default None


def main():
    tree = BST()

    s = input("Enter integers in one line for tree separated by space: ");
    list1 = [int(x) for x in s.split()]
    for e in list1:
        tree.insert(e)
        
    print(s, "are inserted into the tree")
    print("Traverse the elements in this order: ", end = '')
    
    iterator = iter(tree) # Create an iterator
    try:
        while True:
            print(next(iterator), end = ' ')
    except StopIteration:
        print("All traversed")
    
main()
