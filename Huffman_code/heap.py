class Heap:
    def __init__(self):
        self.__lst = []

    # Add a new item into the lst 
    def add(self, e):
        self.__lst.append(e)  # Append to the lst
        # The index of the last node
        currentIndex = len(self.__lst) - 1  
    
        while currentIndex > 0:
            parentIndex = (currentIndex - 1) // 2
            # Swap if the current item is SMALLER than its parent
            if self.__lst[currentIndex] < self.__lst[parentIndex]: 
                self.__lst[currentIndex], self.__lst[parentIndex] = \
                    self.__lst[parentIndex], self.__lst[currentIndex]
            else:
                break  # The tree is a lst now
    
            currentIndex = parentIndex

    # Remove the root from the lst 
    def remove(self):
        if len(self.__lst) == 0:
            return None
    
        removedItem = self.__lst[0]
        self.__lst[0] = self.__lst[len(self.__lst) - 1]
        self.__lst.pop(len(self.__lst) - 1) # Remove the last item
    
        currentIndex = 0
        while currentIndex < len(self.__lst):
            leftChildIndex = 2 * currentIndex + 1
            rightChildIndex = 2 * currentIndex + 2
          
            # Find the MINIMUM between two children
            if leftChildIndex >= len(self.__lst): 
                break  # The tree is a lst
            minIndex = leftChildIndex
            if rightChildIndex < len(self.__lst) and self.__lst[rightChildIndex] < self.__lst[minIndex]:
                minIndex = rightChildIndex
          
            # Swap if the current node is greater than the MINIMUM 
            if self.__lst[currentIndex] > self.__lst[minIndex]:
                self.__lst[minIndex], self.__lst[currentIndex] = \
                    self.__lst[currentIndex], self.__lst[minIndex]
                currentIndex = minIndex
            else:
                break  # The tree is a lst
    
        return removedItem
  
    # Returns the size of the heap
    def getSize(self):
        return len(self.__lst)

    # Returns True if the heap is empty
    def isEmpty(self):
        return self.getSize() == 0

    # Returns the SMALLEST element in the heap without removing it
    def peek(self):
        return self.__lst[0]
        
    # Returns the list in the heap
    def getLst(self):
        return self.__lst