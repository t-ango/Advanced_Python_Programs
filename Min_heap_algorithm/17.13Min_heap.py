"""
Heap Sort Using Min-Heap

This program demonstrates the heap sort algorithm by utilizing a custom min-heap implementation. The heap sort algorithm sorts a list of integers in ascending order.

Functions:
    - heapSort(lst): Sorts the input list using the heap sort algorithm.
    - main(): Accepts user input, sorts the list using `heapSort`, and prints the result.

Usage:
    Run the program and input a list of integers separated by spaces. The sorted list will be displayed.

Example:
    Input: [5, 3, 8, 1]
    Output: [1, 3, 5, 8]
"""

from Min_heap_class import Heap

def heapSort(lst):
    heap = Heap() # Create a Heap 

    # Add elements to the heap
    for v in lst:
        heap.add(v)

    # Remove elements from the heap
    sorted_list = []    
    for i in range(len(lst)): 
        #lst[i] = heap.remove()
        sorted_list.append(heap.remove())
    lst[:] = sorted_list

  
def main():
    lst_input = input("Enter a list of integers separated by spaces: ")
    lst = [int(x) for x in lst_input.split()]
    print ("Your input: ")
    print (lst)
    heapSort(lst)
    print("Sorted: ")
    for v in lst:
        print(v, end = " ")

main()