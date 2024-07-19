
# 📌 Python Basic Syntax

View it in Detail here: [Python Tutorial](https://www.w3schools.com/python/default.asp)

## Overview
File just to mention some basic `Python` Commands

## Syntax
### 1. Comments
Single Line Comment:
```python
#This is a comment
print("Hello, World!")
```

Multi-Line Comment:
```python
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")
```
### 2. Variables
Variables are containers for storing data values. Python has no command for declaring a variable. 
#### About Variables
- A variable is created the moment you first assign a value to it.
- Variables do not need to be declared with any particular type, and can even change type after they have been set.
```python
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
```
- **Casting:** If you want to specify the data type of a variable, this can be done with casting.
```python
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
```
- Get the type
```python
x = 5
y = "John"
print(type(x))  # prints: <class 'int'>
print(type(y))  # prints: <class 'str'>
```
- String variables can be declared either by using single or double quotes:
```python
x = "John"
# both are same
x = 'John'
```
- Variable names are case-sensitive.

#### Variable names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)
- A variable name cannot be any of the Python keywords.

#### Naming Variables:
-- 1. Camel Case: Each word, except the first, starts with a capital letter:
    `myVariableName = "John"`

-- 2. Pascal Case: Each word starts with a capital letter::
    `MyVariableName = "John"`

-- 3. Snake Case: Each word is separated by an underscore character:
    `my_variable_name = "John"`

#### Assign Multiple Values to Variables
- Python allows you to assign values to multiple variables in one line:
```python
x, y, z = "Orange", "Banana", "Cherry"
print(x) # Orange
print(y) # Banana
print(z) # Cherry
```
- And you can assign the same value to multiple variables in one line:
```python
x = y = z = "Orange"
print(x) # Orange
print(y) # Orange
print(z) # Orange
```
- If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
```python
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x) # Apple
print(y) # Banana
print(z) # Cherry
```

#### Output Variables
- The Python print() function is often used to output variables.
```python
x = "Python is awesome"
print(x)  # Python is awesome
```
- In the print() function, you output multiple variables, separated by a comma:
```python
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)  # Python is awesome
```
- You can also use the + operator to output multiple variables:
```python
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)  # Python is awesome
```
```
Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".
```
- For numbers, the + character works as a mathematical operator:
```python
x = 5
y = 10
print(x + y)  # 15
```
- In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
```python
x = 5
y = "John"
print(x + y)  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
- The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
```python
x = 5
y = "John"
print(x, y)  # 5 John
```

#### Global Variables
Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

- Create a variable outside of a function, and use it inside the function:
```python
x = "awesome"

def myfunc(): 
  print("Python is " + x)  # Python is awesome

myfunc()

```
- Create a variable inside a function, with the same name as the global variable:
```python
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)  # Python is fantastic

myfunc()

print("Python is " + x)  # Python is awesome
```
- If you use the `global` keyword, the variable belongs to the global scope:
```python
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)  # Python is fantastic
```
- Also, use the `global` keyword if you want to change a global variable inside a function:
```python
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)  # Python is fantastic
```
```python
```