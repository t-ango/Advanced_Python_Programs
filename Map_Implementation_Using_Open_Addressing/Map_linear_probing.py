"""
Map Implementation using Open Addressing

This script defines a `Map` class implementing a hash map with open addressing for collision handling. The map supports basic operations such as insertion, deletion, lookup, and resizing through rehashing. It also provides additional utility functions for retrieving keys, values, and checking for the presence of elements.

Classes:
    - Map: Implements the hash map with operations like `put`, `remove`, `get`, and utilities like `keys` and `values`.

Constants:
    - DEFAULT_INITIAL_CAPACITY: Default initial capacity of the hash table (default = 4).
    - DEFAULT_MAX_LOAD_FACTOR: Default load factor threshold (default = 0.75).
    - MAXIMUM_CAPACITY: Maximum allowed capacity for the hash table (2^30).

Key Methods:
    - put(key, value): Inserts a key-value pair into the map.
    - remove(key): Removes a key-value pair by its key.
    - containsKey(key): Checks if a key is present in the map.
    - containsValue(value): Checks if a value exists in the map.
    - items(): Returns all key-value pairs as tuples.
    - get(key): Retrieves the value associated with a key.
    - keys(): Returns all keys in the map.
    - values(): Returns all values in the map.
    - clear(): Clears all entries in the map.
    - rehash(): Resizes the hash table and redistributes entries.

Usage Example:
    >>> map = Map()
    >>> map.put("Smith", 30)
    >>> map.put("Anderson", 31)
    >>> print(map.items())
    (['Smith', 30], ['Anderson', 31])
    >>> map.remove("Smith")
    >>> print(map.get("Smith"))
    None
"""

# Define the default hash-table size
DEFAULT_INITIAL_CAPACITY = 4
  
# Define default load factor
DEFAULT_MAX_LOAD_FACTOR = 0.75 
     
# Define the maximum hash-table size to be 2 ** 30
MAXIMUM_CAPACITY = 2 ** 30 
  
class Map:
    def __init__(self, capacity = DEFAULT_INITIAL_CAPACITY, 
                 loadFactorThreshold = DEFAULT_MAX_LOAD_FACTOR):
        # Current hash-table capacity. Capacity is a power of 2
        self.capacity = capacity

        # Specify a load factor used in the hash table
        self.loadFactorThreshold = loadFactorThreshold
   
        # Create a list of empty buckets
        self.table = []
        for i in range(self.capacity):
            self.table.append(None) # Use open addressing
        
        self.size = 0 # Initialize map size

    # Add an entry (key, value) into the map 
    def put(self, key, value):

        if self.size >= self.capacity * self.loadFactorThreshold:          
            if self.capacity == MAXIMUM_CAPACITY:
                raise RuntimeError("Exceeding maximum capacity")
      
            self.rehash()

        # Use open addressing
        i = self.getHash(hash(key))
        while self.table[i] != None and self.table[i][0] != None:
            i = (i + 1) % self.capacity

        # Add an entry (key, value) to hashTable[index]
        self.table[i] = ([key, value])

        self.size += 1 # Increase size
 
    # Remove the entry for the specified key 
    def remove(self, key):
        i = self.getHash(hash(key))

        # Use open addressing
        while self.table[i] != None and (self.table[i][0] == None or self.table[i][0] != key):
            i = (i + 1) % self.capacity
      
        # Remove the first entry that matches the key from a bucket
        if self.table[i] != None and self.table[i][0] == key:
            # A special marker entry (None, None) is placed for the deleted entry
            self.table[i] = (None, None)
            self.size -= 1

    # Return true if the specified key is in the map
    def containsKey(self, key):
        if self.get(key) != None:
            return True
        else:
            return False

  
    # Return true if this map contains the specified value 
    def containsValue(self, value):
        for i in range(self.capacity):
            if self.table[i] is not None and value in self.table[i]:
                return True
        return False
    
    #alternativ containsValue funksjon:
    def containsValue1(self, value):
        for element in self.values():
            if element == value:
                return True
        return False


    # Return a set of entries in the map 
    def items(self):
        entries = []
        for i in range(self.capacity):
            if self.table[i] != None:
                entries.append(self.table[i]) # For open addressing
                
        return tuple(entries)
    
    # Return the first value that matches the specified key 
    def get(self, key):
        i = self.getHash(hash(key))
        while self.table[i] != None:
            if self.table[i][0] != None and self.table[i][0] == key:
                return self.table[i][1]
            i = (i + 1) % self.capacity
                
        return None
  
    # Return all values for the specified key in this map
    def getAll(self, key):
        values = []
        i = self.getHash(hash(key))

        while self.table[i] != None:
            if self.table[i][0] != None and self.table[i][0] == key:
                values.append(self.table[i][1])
            i = (i + 1) % self.capacity
            
        return tuple(values)
  
    # Return a set consisting of the keys in this map
    def keys(self):
        keys = []
    
        for i in range(0, self.capacity):
            if self.table[i] != None:
                keys.append(self.table[i][0])
    
        return keys
  
    # Return a set consisting of the values in this map 
    def values(self):
        values = []
    
        for entry in self.table:
            if entry is not None: 
                values.append(entry[1])
        
        return values
                  
    # Remove all of the entries from this map 
    def clear(self):
        self.size = 0 # Reset map size
        
        self.table = [] # Reset map
        for i in range(self.capacity):
            self.table.append(None)

    # Return the number of mappings in this map 
    def getSize(self):
        return self.size
        
    # Return true if this map contains no entries 
    def isEmpty(self):
        return self.size == 0
    
    # Rehash the map 
    def rehash(self):
        temp = self.items() # Get entries
        self.capacity *= 2 # Double capacity    
        self.table = [] # Create a new hash table
        self.size = 0 # Clear size
        for i in range(self.capacity):
            self.table.append(None)
            
        for entry in temp:
            self.put(entry[0], entry[1]) # Store to new table

    # Return the entries as a string 
    def toString(self):
        return str(self.items())
    
    # Return a string representation for this map 
    def setLoadFactorThreshold(self, threshold):
        self.loadFactorThreshold = threshold

    # Return the hash table as a string 
    def getTable(self):
        table_string = ""
        for entry in self.table:
            if entry is not None and entry [0] is not None:
                table_string += str(entry) + ", "
        return "[" + table_string.rstrip(", ") + "]"
    
    def supplementalHash(self, h):
        h ^= (h >> 20) ^ (h >> 12)
        return h ^ (h >> 7) ^ (h >> 4)

    def getHash(self, hashCode):
        return self.supplementalHash(hashCode) & (self.capacity - 1)



def main():
    # Create a map
    map = Map()
    map.put("Smith", 30) # Add (Smith, 30 ) to map
    map.put("Anderson", 31)
    map.put("Lewis", 29)
    map.put("Cook", 29)
    map.put("Cook", 129)
    
    print("Entry set in map: " + str(map.items()))
    print("The age for Lewis is " + str(map.get("Lewis")))
    print("Is Smith in the map? " + str(map.containsKey("Smith")))
    print("Is Johnson in the map? " + str(map.containsKey("Johnson")))
    print("Is value 30 in the map? " + str(map.containsValue(30)))
    print("Is value 33 in the map? " + str(map.containsValue(33)))
    print("Is age 33 in the map? " + str(map.containsValue(33)))
    print("All values for Cook? " + str(map.getAll("Cook")))
    print("keys are " + str(map.keys()))
    print("values are " + str(map.values()))

    print("Is value 30 in the map? " + str(map.containsValue1(30)))
    print("Is value 33 in the map? " + str(map.containsValue1(33)))
    print("Is age 33 in the map? " + str(map.containsValue1(33)))

    map.remove("Smith") # Remove Smith from map
    print("The map is " + map.getTable())

    map.clear()
    print("The map is " + map.getTable())

    
main()
