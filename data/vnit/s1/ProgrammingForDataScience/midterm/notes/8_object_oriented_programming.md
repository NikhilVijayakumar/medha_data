## Object-Oriented Programming (OOP)

**Main Themes:** Introduction to the fundamental concepts of Object-Oriented Programming (OOP), including classes, objects, attributes, methods, inheritance, and polymorphism. Understanding the syntax for defining classes and creating instances.

**Important Ideas and Facts:**

* **Classes and Objects:**
    * **Class:** A blueprint or template for creating objects. It defines the attributes (data) and methods (behavior) that objects of that class will have.
    * **Object (Instance):** A specific instance of a class. Multiple objects can be created from the same class, each with its own set of attribute values.
        ```python
        class Dog:
            pass # An empty class

        # Creating objects (instances) of the Dog class
        sam = Dog()
        buddy = Dog()

        print(type(sam))   # <class '__main__.Dog'>
        print(type(buddy)) # <class '__main__.Dog'>
        ```

* **Attributes:**
    * Variables associated with an object (instance attributes) or the class itself (class attributes).
    * **`__init__()` method (Constructor):** A special method that is automatically called when an object is created. It's used to initialize the object's attributes using the `self` parameter, which refers to the instance being created.
        ```python
        class Dog:
            # Class attribute (shared by all instances)
            species = 'mammal'

            # Constructor (instance attributes are defined here)
            def __init__(self, breed, name):
                self.breed = breed
                self.name = name

        my_dog = Dog("Labrador", "Lucy")
        your_dog = Dog("Pug", "Max")

        print(my_dog.breed)  # Labrador
        print(my_dog.name)   # Lucy
        print(my_dog.species) # mammal

        print(your_dog.breed)  # Pug
        print(your_dog.name)   # Max
        print(your_dog.species) # mammal
        ```

* **Methods:**
    * Functions defined within a class that operate on the object's data (attributes).
    * The first parameter of a method is always `self`, which refers to the instance of the object calling the method.
        ```python
        class Circle:
            def __init__(self, radius):
                self.radius = radius

            def area(self):
                return 3.14159 * self.radius * self.radius

            def circumference(self):
                return 2 * 3.14159 * self.radius

        my_circle = Circle(5)
        print(f"Area: {my_circle.area()}")         # Area: 78.53975
        print(f"Circumference: {my_circle.circumference()}") # Circumference: 31.4159
        ```

* **Inheritance:**
    * Allows a new class (subclass or derived class) to inherit attributes and methods from an existing class (superclass or base class).
    * Promotes code reusability and the creation of hierarchical relationships between classes.
    * **`super()` function:** Used in the subclass to call methods or the constructor of the superclass.
        ```python
        class Animal:
            def __init__(self, name):
                self.name = name

            def speak(self):
                print("Generic animal sound")

        class Dog(Animal):
            def speak(self): # Method overriding
                print("Woof!")

        class Cat(Animal):
            def speak(self): # Method overriding
                print("Meow!")

        animal = Animal("Generic")
        dog = Dog("Buddy")
        cat = Cat("Whiskers")

        animal.speak() # Generic animal sound
        dog.speak()    # Woof!
        cat.speak()    # Meow!

        print(dog.name) # Buddy (inherited from Animal)
        ```

* **Method Overriding:**
    * A subclass can provide its own implementation of a method that is already defined in its superclass. This allows subclasses to customize inherited behavior.

* **Special Methods (Dunder Methods - Double Underscore Methods):**
    * Methods with double underscores (`__`) at the beginning and end of their names. They provide special functionality and are often invoked implicitly by Python operators or built-in functions.
    * `__init__(self, ...)`: Constructor, called when an object is created.
    * `__str__(self)`: Returns a string representation of the object. Used by `print()` and `str()`.
    * `__len__(self)`: Returns the length of the object. Used by `len()`.
    * `__del__(self)`: Called when the object is about to be deleted (garbage collected). Rarely used explicitly.
        ```python
        class Book:
            def __init__(self, title, pages):
                self.title = title
                self.pages = pages

            def __str__(self):
                return f"Title: {self.title}, Pages: {self.pages}"

            def __len__(self):
                return self.pages

            def __del__(self):
                print(f"Book object '{self.title}' is being deleted.")

        book = Book("The Python Guide", 300)
        print(book)     # Output: Title: The Python Guide, Pages: 300 (using __str__)
        print(len(book)) # Output: 300 (using __len__)

        del book # Explicitly delete the object (invokes __del__)
        ```

* **Polymorphism:**
    * The ability of different objects to respond to the same method call in their own way. This allows for writing more flexible and generic code.
        ```python
        class Dog:
            def speak(self):
                return "Woof!"

        class Cat:
            def speak(self):
                return "Meow!"

        def animal_sound(animal):
            print(animal.speak())

        my_dog = Dog()
        my_cat = Cat()

        animal_sound(my_dog) # Woof!
        animal_sound(my_cat) # Meow!

        animals = [Dog(), Cat()]
        for animal in animals:
            print(animal.speak())
        ```

* **Lecture Slides on OOP:** Emphasize that OOP allows for creating reusable and organised code, especially for larger projects. The general structure of a class with `__init__` and methods is fundamental. The concept of calling methods using the `.method_name()` syntax is linked back to how you interact with built-in Python objects (e.g., `list.append()`, `string.upper()`).