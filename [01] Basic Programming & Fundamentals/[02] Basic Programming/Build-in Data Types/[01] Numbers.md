
# 📌 Python Numbers

View it in Detail here: [Python Tutorial](https://www.w3schools.com/python/default.asp)

## Overview
There are three numeric types in Python:

- int
- float
- complex
Variables of numeric types are created when you assign a value to them:
```python
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>
```

### Int
Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
Examples:
```python
x = 1
y = 35656222554887711
z = -3255522
```

### Float
Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
Examples:
```python
x = 1.10
y = 1.0
z = -35.59
```
Float can also be scientific numbers with an "e" to indicate the power of 10.
```python
x = 35e3
y = 12E4
z = -87.7e100
```
`Note: All are type - <class 'float'>`

### Complex
Complex numbers are written with a "j" as the imaginary part:
```python
x = 3+5j
y = 5j
z = -5j
```

## Type Conversion
You can convert from one type to another with the int(), float(), and complex() methods:
```python
#convert from int to float:
x = float(1)  # 1.0, <class 'float'>

#convert from float to int:
y = int(2.8)  # 2, <class 'int'>

#convert from int to complex:
z = complex(1) # (1+0j), <class 'complex'>
```

`Note: You cannot convert complex numbers into another number type.`

## Random Number
Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

Example
Import the random module, and display a random number between 1 and 9:
```python
import random

print(random.randrange(1, 10))
```