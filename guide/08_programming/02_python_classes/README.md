Contents
==
- [Contents](#contents)
- [Python Classes](#python-classes)
- [Examples](#examples)
- [Basic building blocks](#basic-building-blocks)
  - [Defining a class](#defining-a-class)
  - [Object initializer](#object-initializer)
  - [Attributes](#attributes)
  - [Methods](#methods)
  - [Creating objects](#creating-objects)
  - [Accessing attributes](#accessing-attributes)
  - [Accessing methods](#accessing-methods)
  - [Public vs non-public members](#public-vs-non-public-members)
  - [Name mangling](#name-mangling)
  - [Class attributes](#class-attributes)
  - [Instance attributes](#instance-attributes)
  - [Inheritance](#inheritance)
  - [Class method](#class-method)
  - [Static method](#static-method)
  - [Representation method](#representation-method)
  - [Magic methods](#magic-methods)
  - [Decorators](#decorators)

<!--intro-start-->
# Python Classes
Classes are the building blocks of object-oriented programming in Python. They allow you to leverage the power of Python while writing and organizing your code. 
- Reuse code and avoid repetition
- Bundle together related attributes and methods in a single entity, the object
- Provide users with intuitive APIs

# Examples
Take a look at animal.py and dog.py to test out the building blocks of python classes.

# Basic building blocks

## Defining a class
Defines a blueprint for objects with methods and attributes.

```python
class MyClass: # this
    pass
```

## Object initializer
Initializes a new object's attributes when an instance is created.

```python
class MyClass:
    def __init__(self, value): # this
        self.value = value
```
## Attributes
Variables that hold data for an object.

```python
class MyClass:
    def __init__(self, value):
        self.value = value # this
```

## Methods
Functions defined within a class that operate on instances of the class.

```python
class MyClass:
    def greet(self): # this
        return "Hello"
```

## Creating objects
Instantiating a class to create an object.

```python
obj = MyClass("example_value")
```

## Accessing attributes
Getting or setting the value of an object's attribute.

```python
obj.value
```

## Accessing methods
Calling a method on an object.

```python
obj.greet() 
```

## Public vs non-public members
Public members are accessible from outside the class, while non-public members are intended for internal use.

```python
class MyClass:
    def __init__(self, value):
        self.public_attribute = value
        self._protected_attribute = value
        self.__private_attribute = value
```

## Name mangling
Name mangling is used to make non-public members harder to access from outside the class.

```python
class MyClass:
    def __init__(self, value):
        self.__private_attribute = value

    def __private_method(self):
        return "This method is private"
```

## Class attributes
Attributes shared across all instances of a class.

```python
class MyClass:
    class_attribute = "Class attribute"

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute
```

## Instance attributes
Attributes unique to each instance of a class.

```python
obj1 = MyClass("Instance attribute 1")
obj2 = MyClass("Instance attribute 2")
```

## Inheritance
Mechanism to create a new class that inherits attributes and methods from an existing class.

```python
class ParentClass:
    def __init__(self, parent_value):
        self.parent_value = parent_value

    def parent_method(self):
        return "This is a method from the parent class"

class ChildClass(ParentClass):
    def __init__(self, parent_value, child_value):
        super().__init__(parent_value)
        self.child_value = child_value

    def child_method(self):
        return "This is a method from the child class"

# Example usage:
child_obj = ChildClass("parent_value", "child_value")
child_obj.parent_method()  # Output: 'This is a method from the parent class'
child_obj.child_method()   # Output: 'This is a method from the child class'
```

## Class method
Method bound to the class rather than its instances, accessible via the class itself.

```python
class MyClass:
    class_value = 0

    def __init__(self, instance_value):
        self.instance_value = instance_value

    @classmethod
    def class_method(cls):
        cls.class_value += 1
        return cls.class_value

# Example usage:
obj1 = MyClass(1)
obj2 = MyClass(2)

MyClass.class_method()  # Output: 1
MyClass.class_method()  # Output: 2
```

## Static method
Method that does not receive an implicit first argument and does not depend on class or instance variables.

```python
class MyClass:
    @staticmethod
    def static_method():
        return "This is a static method"

# Example usage:
MyClass.static_method()  # Output: 'This is a static method'
```

## Representation method
Special method used to define how an object is represented as a string.

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'MyClass({self.value})'

# Example usage:
obj = MyClass(10)
print(obj)  # Output: MyClass(10)
```

## Magic methods
Special methods that allow instances of the class to interact with built-in functions and operators.

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'MyClass instance with value {self.value}'

    def __add__(self, other):
        return MyClass(self.value + other.value)

# Example usage:
obj1 = MyClass(5)
obj2 = MyClass(10)

print(obj1 + obj2)  # Output: MyClass instance with value 15
```

## Decorators
Functions that modify the behavior of other functions or methods.

```python
# Decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Function decorated with `my_decorator`
@my_decorator
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()

# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.

```