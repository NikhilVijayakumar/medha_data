## Error Handling

**Main Themes:** Managing runtime errors using `try`, `except`, `else`, and `finally` blocks.

**Important Ideas and Facts:**

* **`try-except` Block:**
    * The `try` block contains the code that might raise an exception (a runtime error).
    * If an exception occurs within the `try` block, the normal flow of execution is interrupted, and Python looks for a matching `except` block to handle the exception.
    * The `except` block specifies the code to be executed if a particular type of exception occurs.
    * You can have multiple `except` blocks to handle different types of exceptions.
    * If no matching `except` block is found, the exception propagates up the call stack, and if not handled elsewhere, it will terminate the program and print an error message.
        ```python
        try:
            result = 10 / 0
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")

        try:
            number = int("abc")
        except ValueError:
            print("Error: Invalid literal for integer.")

        try:
            my_list = [1, 2, 3]
            print(my_list[5])
        except IndexError as e:
            print(f"Error: Index out of bounds. Details: {e}")
        ```
    * **General `except` Block:** A bare `except` block will catch any type of exception. While it can be used as a last resort, it's generally better to catch specific exceptions for more targeted error handling and to avoid masking unexpected errors.
        ```python
        try:
            # Some code that might raise an exception
            x = undefined_variable
        except:
            print("An error occurred.")
        ```

* **`else` Block:**
    * The `else` block is optional and is executed only if no exceptions were raised in the `try` block.
    * It's useful for code that depends on the successful execution of the `try` block.
        ```python
        try:
            num = int(input("Enter a positive integer: "))
            if num <= 0:
                raise ValueError("Input must be a positive integer.")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            print(f"You entered: {num}")
        ```

* **`finally` Block:**
    * The `finally` block is also optional and is always executed, regardless of whether an exception was raised in the `try` block or not, and regardless of whether the exception was handled by an `except` block.
    * It's often used for cleanup operations, such as closing files or releasing resources.
        ```python
        file = None
        try:
            file = open("my_file.txt", "r")
            content = file.read()
            print(content)
        except FileNotFoundError:
            print("Error: File not found.")
        finally:
            if file:
                file.close()
                print("File closed.")
        ```

* **Raising Exceptions (`raise`):**
    * You can explicitly raise exceptions in your code using the `raise` keyword.
    * This is useful for signaling specific error conditions that your code detects.
        ```python
        def check_age(age):
            if age < 0:
                raise ValueError("Age cannot be negative.")
            elif age < 18:
                raise Exception("You must be 18 or older.")
            else:
                print("Age is valid.")

        try:
            check_age(-5)
        except ValueError as e:
            print(f"Caught a ValueError: {e}")

        try:
            check_age(15)
        except Exception as e:
            print(f"Caught an Exception: {e}")

        check_age(25)
        ```

* **Evaluating Strings (`eval()`):**
    * The `eval()` function executes a string as a Python expression.
    * **Caution:** Using `eval()` with untrusted input can be very dangerous as it allows arbitrary code execution. Avoid using it with external or user-provided strings unless you have complete control over their content.
        ```python
        x = 5
        expression = "x + 2"
        result = eval(expression)
        print(result) # Output: 7

        # Danger! Avoid with untrusted input:
        # user_input = "import os; os.system('rm -rf /')"
        # eval(user_input) # This could have disastrous consequences!
        ```