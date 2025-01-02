# Map Implementation using Open Addressing

This repository contains a Python implementation of a hash map using open addressing for collision resolution. The implementation includes various methods for common hash map operations such as insertion, deletion, and lookup.

## Features

- **Customizable Capacity and Load Factor**: Adjust initial capacity and load factor threshold.
- **Collision Handling**: Implements open addressing to resolve hash collisions.
- **Dynamic Resizing**: Automatically rehashes when the load factor threshold is exceeded.
- **Key and Value Retrieval**: Retrieve all keys, values, or key-value pairs as needed.
- **Contains Checks**: Verify if a key or value exists in the map.
- **Clear Method**: Reset the map to an empty state.

## Usage Example

```python
# Create a map
map = Map()
map.put("Smith", 30)
map.put("Anderson", 31)

# Access items
print(map.items())  # Output: [['Smith', 30], ['Anderson', 31]]
print(map.get("Smith"))  # Output: 30

# Check presence
print(map.containsKey("Smith"))  # Output: True
print(map.containsValue(30))  # Output: True

# Remove an entry
map.remove("Smith")
print(map.get("Smith"))  # Output: None

# Clear the map
map.clear()
print(map.items())  # Output: []
Class Details

class Map
Initialization

__init__(capacity=DEFAULT_INITIAL_CAPACITY, loadFactorThreshold=DEFAULT_MAX_LOAD_FACTOR): Initializes the map with specified capacity and load factor.
Core Methods

put(key, value): Adds a key-value pair.
remove(key): Deletes a key-value pair by key.
get(key): Retrieves the value for a given key.
containsKey(key): Checks for key existence.
containsValue(value): Checks for value existence.
Utility Methods

keys(): Returns all keys in the map.
values(): Returns all values in the map.
clear(): Clears the map.
rehash(): Resizes and rehashes the map.
Testing

Run the program using the main() function for a demonstration of the map's capabilities.

python map.py
