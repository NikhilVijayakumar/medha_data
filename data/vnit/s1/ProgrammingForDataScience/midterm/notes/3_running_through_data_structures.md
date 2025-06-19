## Running Through Elements of Data Structures

This section demonstrates how to iterate over the elements of Python's fundamental data structures (lists, dictionaries, tuples, sets) for operations and validations, along with related built-in functions and constructs.

**1. Lists:**

* **Basic Iteration (for loop):**
    ```python
    my_list = [10, 20, 30, 40, 50]
    for item in my_list:
        print(item * 2) # Example operation: multiply each element by 2
    ```

* **Iteration with Index (enumerate):**
    ```python
    my_list = ['a', 'b', 'c']
    for index, value in enumerate(my_list):
        print(f"Index: {index}, Value: {value}")
        if value == 'b':
            print("Found 'b' at index", index) # Example validation
    ```

* **List Comprehension (for creating new lists based on existing ones):**
    ```python
    my_list = [1, 2, 3, 4, 5]
    squared_list = [x**2 for x in my_list] # Operation: square each element
    even_numbers = [x for x in my_list if x % 2 == 0] # Validation: filter for even numbers
    print(squared_list)
    print(even_numbers)
    ```

* **`map()` (applying a function to each item):**
    ```python
    my_list = [1, 2, 3]
    doubled_list = list(map(lambda x: x * 2, my_list)) # Operation: double each element
    print(doubled_list)
    ```

* **`filter()` (selecting items based on a condition):**
    ```python
    my_list = [1, 5, 2, 8, 3]
    greater_than_4 = list(filter(lambda x: x > 4, my_list)) # Validation: keep elements greater than 4
    print(greater_than_4)
    ```

**2. Dictionaries:**

* **Iterating through Keys:**
    ```python
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    for key in my_dict: # Equivalent to: for key in my_dict.keys():
        print(key)
        if key == 'b':
            print("Found key 'b'") # Example validation
    ```

* **Iterating through Values:**
    ```python
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    for value in my_dict.values():
        print(value * 3) # Example operation: multiply each value by 3
        if value > 1:
            print("Value is greater than 1") # Example validation
    ```

* **Iterating through Items (key-value pairs):**
    ```python
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    for key, value in my_dict.items():
        print(f"Key: {key}, Value: {value}")
        if value % 2 != 0:
            print(f"Value {value} for key '{key}' is odd") # Example validation
    ```

* **Dictionary Comprehension (for creating new dictionaries):**
    ```python
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    squared_values = {key: value**2 for key, value in my_dict.items()} # Operation: square each value
    filtered_dict = {key: value for key, value in my_dict.items() if value > 1} # Validation: keep pairs where value > 1
    print(squared_values)
    print(filtered_dict)
    ```

* **`map()` and `filter()` with Dictionaries (less common directly on dictionaries):** You would typically iterate through `.items()`, `.keys()`, or `.values()` first and then apply `map()` or `filter()`.

**3. Tuples:**

* **Basic Iteration (for loop):**
    ```python
    my_tuple = (1, 2, 'hello', 4.5)
    for item in my_tuple:
        print(item)
        if isinstance(item, str):
            print("Found a string:", item) # Example validation
    ```

* **Iteration with Index (enumerate):**
    ```python
    my_tuple = ('x', 'y', 'z')
    for index, value in enumerate(my_tuple):
        print(f"Index: {index}, Value: {value}")
    ```

* **Tuple Comprehension (actually creates a generator expression, not a tuple directly):**
    ```python
    my_tuple = (5, 10, 15)
    multiplied = (x * 3 for x in my_tuple)
    print(tuple(multiplied)) # To see the results as a tuple
    ```

* **`map()` and `filter()` (similar to lists):**
    ```python
    my_tuple = (10, 20, 30)
    divided_by_5 = tuple(map(lambda x: x / 5, my_tuple)) # Operation
    greater_than_15 = tuple(filter(lambda x: x > 15, my_tuple)) # Validation
    print(divided_by_5)
    print(greater_than_15)
    ```

**4. Sets:**

* **Basic Iteration (for loop):** Note that sets are unordered, so the order of elements during iteration is not guaranteed.
    ```python
    my_set = {1, 2, 3, 4, 5}
    for item in my_set:
        print(item + 10) # Example operation
        if item % 2 == 0:
            print(f"{item} is even") # Example validation
    ```

* **Set Comprehension (for creating new sets):**
    ```python
    my_set = {1, 2, 3}
    squared_set = {x**2 for x in my_set} # Operation
    even_multiplied_set = {x * 2 for x in my_set if x % 2 == 0} # Operation and validation
    print(squared_set)
    print(even_multiplied_set)
    ```

* **`map()` and `filter()` (similar to lists and tuples):**
    ```python
    my_set = {2, 4, 6}
    halved_set = set(map(lambda x: x / 2, my_set)) # Operation
    greater_than_3_set = set(filter(lambda x: x > 3, my_set)) # Validation
    print(halved_set)
    print(greater_than_3_set)
    ```

**5. `zip()` (Iterating over multiple iterables in parallel):**

`zip()` can be used with any of these data structures to iterate over them simultaneously.

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 28]
cities = ["New York", "London", "Paris"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}.")