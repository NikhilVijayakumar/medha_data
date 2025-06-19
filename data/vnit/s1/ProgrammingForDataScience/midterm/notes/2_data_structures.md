## Data Structures

**Main Themes:** Introduction to fundamental data structures in Python: lists, dictionaries, tuples, and sets. Emphasis on understanding how to manipulate these structures.

**Important Ideas and Facts:**

* **Lists:**
    * **Ordered Sequences:** Elements maintain their order of insertion.
    * **Mutable:** Elements can be added, removed, or modified after creation.
    * **Heterogeneous Elements:** Can contain items of different data types.
    * **Enclosed in Square Brackets `[]`:**
        ```python
        my_list = [1, "hello", 3.14, True]
        print(my_list)
        print(type(my_list))
        ```
    * **Indexing and Slicing:** Similar to strings.
        ```python
        my_list = [10, 20, 30, 40, 50]
        first_element = my_list[0]   # 10
        slice_of_list = my_list[1:4] # [20, 30, 40]
        last_element = my_list[-1]  # 50
        print(first_element)
        print(slice_of_list)
        print(last_element)
        ```
    * **Concatenation (`+`) and Repetition (`*`):**
        ```python
        list1 = [1, 2]
        list2 = [3, 4]
        combined_list = list1 + list2 # [1, 2, 3, 4]
        repeated_list = list1 * 3     # [1, 2, 1, 2, 1, 2]
        print(combined_list)
        print(repeated_list)
        ```
    * **Nested Lists:** Lists can contain other lists.
        ```python
        nested_list = [[1, 2], [3, 4, 5]]
        print(nested_list[0][1]) # Accesses the second element of the first inner list (2)
        ```
    * **List Methods (Examples):**
        ```python
        my_list = [1, 3, 2]
        my_list.append(4)      # [1, 3, 2, 4] - Adds to the end
        my_list.insert(1, 1.5)  # [1, 1.5, 3, 2, 4] - Inserts at a specific index
        my_list.sort()          # [1, 1.5, 2, 3, 4] - Sorts in place
        my_list.reverse()       # [4, 3, 2, 1.5, 1] - Reverses in place
        removed_element = my_list.pop() # [4, 3, 2, 1.5] - Removes and returns the last element
        my_list.remove(2)       # [4, 3, 1.5] - Removes the first occurrence of a value
        count_of_3 = my_list.count(3) # 1 - Counts occurrences
        index_of_3 = my_list.index(3) # 1 - Returns the index of the first occurrence
        my_list.extend([5, 6])  # [4, 3, 1.5, 5, 6] - Appends elements from another iterable
        my_list.clear()         # [] - Removes all elements
        print(my_list) # After clear()
        ```
    * **List Comprehensions (Revisited):** Concise way to create lists.
        ```python
        numbers = [1, 2, 3, 4, 5]
        squares = [x**2 for x in numbers]      # [1, 4, 9, 16, 25]
        even_squares = [x**2 for x in numbers if x % 2 == 0] # [4, 16]
        ```

* **Dictionaries:**
    * **Unordered Collections (Python 3.7+):** Insertion order is preserved. In earlier versions, they were unordered.
    * **Key-Value Pairs:** Store data as `key: value`. Keys must be unique and immutable (strings, numbers, tuples). Values can be of any type.
    * **Enclosed in Curly Braces `{}`:**
        ```python
        my_dict = {'name': 'Rohan', 'Marks': [23, 34, 49], 'age': 20}
        print(my_dict)
        print(type(my_dict))
        ```
    * **Accessing Values:** Use keys to retrieve values.
        ```python
        name = my_dict['name'] # 'Rohan'
        marks = my_dict['Marks'] # [23, 34, 49]
        print(name)
        print(marks[1]) # Accessing an element in the list value (34)
        ```
    * **Dictionary Methods (Examples):**
        ```python
        my_dict = {'a': 1, 'b': 2, 'c': 3}
        keys = my_dict.keys()     # dict_keys(['a', 'b', 'c'])
        values = my_dict.values() # dict_values([1, 2, 3])
        items = my_dict.items()   # dict_items([('a', 1), ('b', 2), ('c', 3)])
        value_of_b = my_dict.get('b')       # 2 - Returns value for key, or None if not found
        value_or_default = my_dict.get('d', 0) # 0 - Returns default if key not found
        my_dict['d'] = 4          # Adds a new key-value pair
        my_dict.update({'e': 5, 'f': 6}) # Updates with multiple key-value pairs
        removed_value = my_dict.pop('a')    # Removes and returns the value for the key 'a'
        removed_item = my_dict.popitem()  # Removes and returns the last inserted key-value pair (in 3.7+)
        my_dict.clear()           # Removes all items
        print(keys)
        print(values)
        print(items)
        print(value_of_b)
        print(value_or_default)
        print(my_dict) # After clear()
        ```
    * **Dictionary Comprehensions:** Concise way to create dictionaries.
        ```python
        numbers = [1, 2, 3, 4]
        square_dict = {x: x**2 for x in numbers} # {1: 1, 2: 4, 3: 9, 4: 16}
        even_square_dict = {x: x**2 for x in numbers if x % 2 == 0} # {2: 4, 4: 16}
        ```

* **Tuples:**
    * **Ordered Sequences:** Elements maintain their order.
    * **Immutable:** Cannot be modified after creation.
    * **Heterogeneous Elements:** Can contain different data types.
    * **Enclosed in Parentheses `()`:** Although parentheses are optional for single-element tuples, it's good practice to include them for clarity, especially for empty tuples `()` and multi-element tuples.
        ```python
        my_tuple = (1, 'one', 3.0, False)
        another_tuple = 10, 20, 30 # Parentheses are optional
        single_element_tuple = (5,) # Trailing comma is crucial
        empty_tuple = ()
        print(my_tuple)
        print(type(my_tuple))
        print(single_element_tuple)
        print(type(single_element_tuple))
        ```
    * **Indexing and Slicing:** Similar to lists and strings.
        ```python
        my_tuple = (10, 20, 30, 40)
        first = my_tuple[0]   # 10
        slice_ = my_tuple[1:3] # (20, 30)
        print(first)
        print(slice_)
        ```
    * **Tuple Packing and Unpacking:**
        ```python
        point = 10, 20, 30 # Packing
        x, y, z = point    # Unpacking
        print(x, y, z)
        ```
    * **Immutability Benefits:** Tuples are often used for data that should not be changed, and they can be used as keys in dictionaries (unlike lists).

* **Sets:**
    * **Unordered Collections:** Elements have no specific order.
    * **Unique Elements:** Duplicate elements are automatically removed.
    * **Mutable:** Elements can be added and removed.
    * **Enclosed in Curly Braces `{}`:** Note the distinction from dictionaries (which have key-value pairs). An empty set is created using `set()`, not `{}`.
        ```python
        my_set = {1, 2, 2, 3, 4, 4, 4} # Duplicates are removed
        print(my_set) # Output: {1, 2, 3, 4}
        print(type(my_set))
        empty_set = set()
        print(type(empty_set))
        ```
    * **Set Operations:**
        ```python
        set1 = {1, 2, 3}
        set2 = {3, 4, 5}
        union_set = set1 | set2       # {1, 2, 3, 4, 5}
        intersection_set = set1 & set2 # {3}
        difference_set = set1 - set2   # {1, 2} (elements in set1 but not in set2)
        symmetric_difference = set1 ^ set2 # {1, 2, 4, 5} (elements in either set but not both)
        ```
    * **Set Methods (Examples):**
        ```python
        my_set = {1, 2, 3}
        my_set.add(4)       # {1, 2, 3, 4} - Adds an element
        my_set.update([5, 6]) # {1, 2, 3, 4, 5, 6} - Adds multiple elements
        my_set.remove(3)    # {1, 2, 4, 5, 6} - Removes a specific element (raises KeyError if not found)
        my_set.discard(2)   # {1, 4, 5, 6} - Removes if present, no error if not found
        popped_element = my_set.pop() # Removes and returns an arbitrary element
        my_set.clear()      # Removes all elements
        print(my_set) # After clear()
        ```
    * **Set Comprehensions:** Concise way to create sets.
        ```python
        numbers = [1, 2, 2, 3, 3, 3]
        unique_squares = {x**2 for x in numbers} # {1, 4, 9}
        ```