## Functions

**Main Themes:** Defining reusable blocks of code through functions. Understanding the concepts of scope, arguments, and return values.

**Important Ideas and Facts:**

* **Function Definition (`def`):**
    * Functions are defined using the `def` keyword, followed by the function name, parentheses for parameters, and a colon.
    * The code block within the function is indented.
    * **Docstrings:** It's good practice to include a docstring (a triple-quoted string) immediately after the function definition to describe what the function does, its parameters, and what it returns.
        ```python
        def greet(name):
            """Greets the person passed as a parameter."""
            print(f"Hello, {name}!")

        greet("Alice")
        help(greet) # Displays the docstring
        ```

* **Arguments (Parameters):**
    * Values passed to the function when it is called.
    * **Positional Arguments:** Passed in the order they are defined in the function signature.
        ```python
        def describe_pet(animal_type, pet_name):
            """Describes a pet."""
            print(f"I have a {animal_type} named {pet_name}.")

        describe_pet("dog", "Buddy")
        ```
    * **Keyword Arguments:** Passed with the parameter name, allowing you to specify arguments out of order and provide default values.
        ```python
        def power(base, exponent=2):
            """Returns the base raised to the power of the exponent (default is 2)."""
            return base ** exponent

        print(power(5))          # Output: 25 (exponent uses default value)
        print(power(base=3, exponent=3)) # Output: 27
        print(power(exponent=4, base=2)) # Output: 16 (order doesn't matter with keywords)
        ```

* **Return Values (`return`):**
    * The `return` statement exits the function and can optionally send a value back to the caller.
    * If no `return` statement is used, the function implicitly returns `None`.
        ```python
        def add(x, y):
            """Returns the sum of x and y."""
            return x + y

        result = add(5, 3)
        print(result) # Output: 8

        def no_return():
            print("This function doesn't explicitly return anything.")

        value = no_return()
        print(value) # Output: None
        ```
    * **Difference between `print` and `return`:** `print` displays output to the console, while `return` sends a value back from the function that can be used in further calculations or assignments.

* **Scope:**
    * The region of the code where a variable is accessible.
    * **Local Scope:** Variables defined inside a function are local to that function and are only accessible within it.
    * **Global Scope:** Variables defined outside any function have global scope and can be accessed from anywhere in the program.
    * **`global` keyword:** Used inside a function to modify a global variable.
    * **`nonlocal` keyword:** Used in nested functions to refer to a variable in the nearest enclosing function's scope.
        ```python
        global_var = 10

        def my_func():
            local_var = 5
            print(f"Local variable: {local_var}")
            print(f"Global variable (inside): {global_var}")

        my_func()
        print(f"Global variable (outside): {global_var}")
        # print(local_var) # This would cause a NameError

        def modify_global():
            global global_var
            global_var = 20

        modify_global()
        print(f"Modified global variable: {global_var}")

        def outer_func():
            outer_var = "outer"
            def inner_func():
                nonlocal outer_var
                outer_var = "inner"
                print(f"Inner variable: {outer_var}")
            inner_func()
            print(f"Outer variable (after inner): {outer_var}")

        outer_func()
        ```

* **`*args` (Arbitrary Positional Arguments):**
    * Allows a function to accept a variable number of positional arguments. These are collected into a tuple.
        ```python
        def sum_all(*numbers):
            """Sums all the numbers passed as arguments."""
            total = 0
            for num in numbers:
                total += num
            return total

        print(sum_all(1, 2, 3))       # Output: 6
        print(sum_all(10, 20, 30, 40)) # Output: 100
        ```

* **`**kwargs` (Arbitrary Keyword Arguments):**
    * Allows a function to accept a variable number of keyword arguments. These are collected into a dictionary.
        ```python
        def describe_person(**info):
            """Prints information about a person."""
            for key, value in info.items():
                print(f"{key}: {value}")

        describe_person(name="Charlie", age=30, city="London")
        ```

* **Lambda Expressions (Anonymous Functions):**
    * Small, single-expression anonymous functions defined using the `lambda` keyword.
    * Often used for short, simple operations where a full function definition is not necessary.
        ```python
        square = lambda num: num ** 2
        print(square(5)) # Output: 25

        add = lambda x, y: x + y
        print(add(3, 7)) # Output: 10
        ```

* **`map()` Function:**
    * Applies a given function to all items in an iterable and returns a map object (an iterator). You often need to convert it to a list or other sequence to see the results.
        ```python
        numbers = [1, 2, 3, 4]
        squares = map(lambda x: x**2, numbers)
        print(list(squares)) # Output: [1, 4, 9, 16]
        ```

* **`filter()` Function:**
    * Creates a new iterable with elements from the original iterable for which a given function returns `True`. Returns a filter object (an iterator).
        ```python
        numbers = [1, 2, 3, 4, 5, 6]
        even_numbers = filter(lambda x: x % 2 == 0, numbers)
        print(list(even_numbers)) # Output: [2, 4, 6]
        ```