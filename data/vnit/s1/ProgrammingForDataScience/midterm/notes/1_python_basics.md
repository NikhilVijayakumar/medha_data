## Python Basics

**Main Themes:** Introduction to Python syntax and basic data types (numbers, strings, booleans). Emphasis on understanding the core concepts of variable assignment and dynamic typing.

**Important Ideas and Facts:**

* **Basic Data Types:**
    * **Integers (`int`):** Whole numbers without a decimal point. Python 3 supports arbitrarily large integers.
        ```python
        age = 30
        count = 123456789012345678901234567890
        print(type(age))
        print(type(count))
        ```
    * **Floating-Point Numbers (`float`):** Numbers with a decimal point. Represented using double-precision (64-bit) floating-point. Be aware of potential floating-point representation issues.
        ```python
        pi = 3.14159
        temperature = 25.5
        print(type(pi))
        print(type(temperature))
        ```
    * **Strings (`str`):** Immutable sequences of Unicode characters. Enclosed in single quotes (`'...'`), double quotes (`"..."`), or triple quotes (`'''...'''` or `"""..."""`) for multiline strings.
        ```python
        name = "Alice"
        message = 'Hello, world!'
        long_text = """This is a
        multiline string."""
        print(type(name))
        print(type(message))
        print(type(long_text))
        ```
    * **Booleans (`bool`):** Represent truth values: `True` or `False`. Result from logical operations.
        ```python
        is_valid = True
        has_permission = False
        print(type(is_valid))
        print(type(has_permission))
        ```

* **Variable Assignment:**
    * Variables are names that refer to objects in memory. Assignment uses the `=` operator.
        ```python
        x = 10
        y = "Hello"
        z = True
        ```
    * **Dynamic Typing:** Python infers the data type of a variable at runtime. A variable can be reassigned to a value of a different type.
        ```python
        my_var = 10      # my_var is an integer
        print(type(my_var))
        my_var = "Hello" # Now my_var is a string
        print(type(my_var))
        ```
    * **Naming Conventions (PEP 8):**
        * Variable names should be lowercase, with words separated by underscores (snake\_case).
        * Avoid single-character names (except for counters in loops).
        * Be descriptive and meaningful.
        ```python
        user_name = "John Doe"
        item_count = 5
        is_active = True
        ```

* **Strings (Further Details):**
    * **Indexing:** Access individual characters using zero-based indexing. Negative indexing accesses from the end.
        ```python
        text = "Python"
        first_char = text[0]  # 'P'
        last_char = text[-1] # 'n'
        print(first_char)
        print(last_char)
        ```
    * **Slicing:** Extract substrings using `[start:stop:step]`. `stop` index is exclusive.
        ```python
        substring = text[1:4]   # 'yth'
        every_other = text[::2] # 'Pto'
        reversed_text = text[::-1] # 'nohtyP'
        print(substring)
        print(every_other)
        print(reversed_text)
        ```
    * **Immutability:** Strings cannot be modified after creation. Operations create new strings.
        ```python
        text = "Hello"
        new_text = 'J' + text[1:] # Creates a new string "Jello"
        print(text)
        print(new_text)
        ```
    * **String Methods (Examples):**
        ```python
        text = "  python is fun  "
        upper_case = text.upper()   # "  PYTHON IS FUN  "
        lower_case = text.lower()   # "  python is fun  "
        stripped_text = text.strip() # "python is fun"
        split_text = text.split()   # ['python', 'is', 'fun']
        joined_text = "-".join(['python', 'is', 'fun']) # "python-is-fun"
        index_of_is = text.find("is") # 9
        replaced_text = text.replace("fun", "awesome") # "  python is awesome  "
        print(upper_case)
        print(lower_case)
        print(stripped_text)
        print(split_text)
        print(joined_text)
        print(index_of_is)
        print(replaced_text)
        ```

* **String Formatting:**
    * **f-strings (Formatted String Literals):** Embed expressions directly within string literals using curly braces `{}`.
        ```python
        name = "Bob"
        age = 25
        print(f"My name is {name} and I am {age} years old.")
        print(f"{2 + 2 = }") # Available in Python 3.8+ for debugging
        ```
    * **.format() method:** Uses placeholders `{}` that can be filled with values.
        ```python
        print("Coordinates: ({:.2f}, {:.3f})".format(3.14159, 2.71828))
        print("I got {x} marks in {a}".format(x=45.5475, a='Python'))
        print("I got {} marks in {}".format(45.5475, 'Python')) # Implicit order
        ```
    * **% formatting (Older style):** Uses `%` operator with format specifiers. Less readable and prone to errors. Generally avoid in new code.
        ```python
        name = "Charlie"
        score = 88.5
        print("Hello %s, your score is %.1f" % (name, score))
        ```

* **Booleans (Further Details):**
    * Boolean values are the result of comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`) and logical operators (`and`, `or`, `not`).
        ```python
        x = 5
        y = 10
        print(x == y)   # False
        print(x < y)    # True
        print(not (x > y)) # True
        print(x < y and y < 15) # True
        print(x > 0 or y < 5)  # True
        ```
    * **Truthiness and Falsiness:** Certain values are inherently considered "truthy" or "falsy" in boolean contexts (e.g., in `if` conditions).
        * **Falsy:** `False`, `None`, `0`, `0.0`, empty sequences (`""`, `[]`, `()`, `{}`), empty sets (`set()`).
        * **Truthy:** All other values.
        ```python
        if "":
            print("This won't print")
        if [1, 2, 3]:
            print("This will print")
        ```