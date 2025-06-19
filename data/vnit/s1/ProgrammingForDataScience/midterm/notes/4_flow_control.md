## Flow Control

**Main Themes:** Implementing conditional logic using `if`, `elif`, `else` statements, and iterating over sequences using `for` and `while` loops.

**Important Ideas and Facts:**

* **Conditional Statements (`if`, `elif`, `else`):**
    * **`if` statement:** Executes a block of code if a condition evaluates to `True`.
        ```python
        age = 20
        if age >= 18:
            print("You are eligible to vote.")
        ```
    * **`elif` statement:** (Else if) Checks an additional condition only if the preceding `if` or `elif` conditions were `False`. You can have multiple `elif` statements.
        ```python
        grade = 'B'
        if grade == 'A':
            print("Excellent!")
        elif grade == 'B':
            print("Good job.")
        elif grade == 'C':
            print("Keep trying.")
        else:
            print("Needs improvement.")
        ```
    * **`else` statement:** Provides a block of code to execute if none of the preceding `if` or `elif` conditions were `True`.
        ```python
        number = -5
        if number > 0:
            print("Positive number")
        elif number == 0:
            print("Zero")
        else:
            print("Negative number")
        ```
    * **Indentation:** Python uses indentation (typically 4 spaces) to define code blocks within conditional statements. Consistent indentation is crucial for the correct execution of your code.

* **`for` Loops:**
    * Iterate over each item in a sequence (like lists, strings, tuples, dictionaries, sets).
        ```python
        fruits = ["apple", "banana", "cherry"]
        for fruit in fruits:
            print(fruit)
        ```
    * **Dictionary Iteration:**
        * **`.keys()`:** Iterates over the keys of the dictionary.
            ```python
            my_dict = {'a': 1, 'b': 2, 'c': 3}
            for key in my_dict.keys():
                print(key)
            ```
        * **`.values()`:** Iterates over the values of the dictionary.
            ```python
            for value in my_dict.values():
                print(value)
            ```
        * **`.items()`:** Iterates over key-value pairs as tuples.
            ```python
            for key, value in my_dict.items():
                print(f"Key: {key}, Value: {value}")
            ```

* **`while` Loops:**
    * Execute a block of code as long as a specified condition is `True`.
        ```python
        count = 0
        while count < 5:
            print(f"Count is: {count}")
            count += 1
        ```
    * **`else` block with `while`:** Executes if the loop finishes normally (condition becomes `False`), but not if the loop is exited by a `break` statement.
        ```python
        number = 1
        while number <= 5:
            print(number)
            number += 1
        else:
            print("Loop finished normally.")

        number = 1
        while number <= 5:
            print(number)
            if number == 3:
                break
            number += 1
        else:
            print("This else block will not execute.")
        ```

* **Loop Control Statements:**
    * **`break`:** Immediately terminates the current loop and transfers control to the statement following the loop.
        ```python
        numbers = [1, 2, 3, 4, 5]
        for num in numbers:
            if num == 3:
                break
            print(num) # Output: 1, 2
        ```
    * **`continue`:** Skips the rest of the current iteration and proceeds to the next iteration of the loop.
        ```python
        numbers = [1, 2, 3, 4, 5]
        for num in numbers:
            if num == 3:
                continue
            print(num) # Output: 1, 2, 4, 5
        ```
    * **`pass`:** Does nothing. It's used as a placeholder where a statement is syntactically required but you don't want any action to be performed.
        ```python
        def my_function():
            pass # To be implemented later

        if True:
            pass
        else:
            print("This won't execute")
        ```

* **`range()` Function:**
    * Generates a sequence of numbers. `range(start, stop, step)`. `stop` is exclusive.
        ```python
        for i in range(5):       # Generates 0, 1, 2, 3, 4
            print(i)

        for i in range(2, 7):    # Generates 2, 3, 4, 5, 6
            print(i)

        for i in range(1, 10, 2): # Generates 1, 3, 5, 7, 9
            print(i)
        ```

* **`enumerate()` Function:**
    * Adds a counter to an iterable, returning an enumerate object which yields pairs of (index, element).
        ```python
        fruits = ["apple", "banana", "cherry"]
        for index, fruit in enumerate(fruits):
            print(f"Index: {index}, Fruit: {fruit}")
        ```

* **`zip()` Function:**
    * Iterates over multiple iterables in parallel, combining corresponding elements into tuples. Stops when the shortest iterable is exhausted.
        ```python
        names = ["Alice", "Bob", "Charlie"]
        ages = [25, 30, 28]
        for name, age in zip(names, ages):
            print(f"{name} is {age} years old.")

        list1 = [1, 2, 3]
        list2 = ['a', 'b']
        for item1, item2 in zip(list1, list2):
            print(item1, item2) # Output: 1 a, 2 b
        ```

* **Membership Operators (`in`, `not in`):**
    * Check if a value exists in a sequence.
        ```python
        fruits = ["apple", "banana", "cherry"]
        print("banana" in fruits)    # True
        print("grape" not in fruits) # True
        ```

* **`min()` and `max()` Functions:**
    * Return the smallest and largest elements in an iterable.
        ```python
        numbers = [3, 1, 4, 1, 5, 9, 2, 6]
        print(min(numbers)) # 1
        print(max(numbers)) # 9
        ```