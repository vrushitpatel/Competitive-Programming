
# 📌 Python Strings

View it in Detail here: [Python Tutorial](https://www.w3schools.com/python/default.asp)

## Overview
Strings in python are surrounded by either single quotation marks, or double quotation marks.

- 'hello' is the same as "hello".

You can display a string literal with the print() function:

```python
print("Hello")
print('Hello')
```

## Syntax and Declaration
### 1. Quotes Inside Quotes
You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
```python
print("It's alright") # It's alright
print("He is called 'Johnny'") # He is called 'Johnny'
print('He is called "Johnny"') # He is called "Johnny"
```

### 2. Assign String to a Variable
Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
```python
a = "Hello"
print(a) # Hello
```

### 3. Multiline Strings
You can assign a multiline string to a variable by using `three quotes`:
```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```
Or `three single quotes`:
```python
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
```
`Note: in the result, the line breaks are inserted at the same position as in the code.`

### 4. Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
```python
# Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1]) # e
```

### 5. Looping Through a String
Since strings are arrays, we can loop through the characters in a string, with a `for` loop.
```python
# Loop through the letters in the word "banana" & prints each letter on a new line
for x in "banana":
  print(x)
```

### 6. String Length
To get the length of a string, use the `len()` function.
```python
# The len() function returns the length of a string:
a = "Hello, World!"
print(len(a)) # 13
```

### 7. Check String
To check if a certain phrase or character is present in a string, we can use the keyword `in`.
```python
# Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.") # Yes, 'free' is present.
```
Or
```python
# print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.") # No, 'expensive' is NOT present.
```

## Slicing Strings
### 1. Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string. End Index after the colon is not included in the output.
```python
# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5]) # llo
```
`Note: The first character has index 0.`

### 2. Slice From the Start
By leaving out the start index, the range will start at the first character:
```python
# Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5]) # Hello
```

### 3. Slice To the End
By `leaving out the end index`, the range will go to the end:
```python
# Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:]) # llo, World!
```

### 4. Negative Indexing
Use `negative indexes` to start the slice from the end of the string:
```python
# Get the characters:
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):
b = "Hello, World!" #orl
print(b[-5:-2])
```
`Last Index is -1 and not 0.`

## Modify Strings
Python has a set of built-in methods that you can use on strings.

### 1. Upper Case
The `upper()` method returns the string in upper case:
```python
a = "Hello, World!"
print(a.upper()) # HELLO, WORLD!
```

### 2. Lower  Case
The `lower()` method returns the string in lower case:
```python
a = "Hello, World!"
print(a.lower()) # hello, world!
```

### 3. Remove Whitespace
Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

The `strip()` method removes any whitespace from the beginning or the end:
```python
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
```

### 4. Replace String
The `replace()` method replaces a string with another string:
```python
a = "Hello, World!"
print(a.replace("H", "J")) # Jello, World!
``` 
`Note: it is Case Sensitive.`

### 5. Split String
The `split()` method returns a list where the text between the specified separator becomes the list items.
The `split()` method splits the string into substrings if it finds instances of the separator:
```python
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
``` 

## String Concatenation

To concatenate, or combine, two strings you can use the + operator.
```python
# Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
d = a + " " + b # Add Space between 2 Variables
print(c) # HelloWorld
print(d) # Hello World
``` 

## ASCII Value
- ord() - Converts a Character into a ASCII Value
- chr() - Converts a ASCII Value into a Character

## Formatted Strings

As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
```python
age = 36
txt = "My name is John, I am " + age
print(txt) # My name is John, I am 36
``` 

But we can combine strings and numbers by using `f-strings` or the `format()` method!

### F-Strings
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
```python
# Create an f-string:
age = 36
txt = f"My name is John, I am {age}"
print(txt) # My name is John, I am 36
```
### Using Format Function
```python
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
```
### Placeholders and Modifiers
A placeholder can contain variables, operations, functions, and modifiers to format the value.
```python
# Add a placeholder for the price variable:
price = 59
txt = f"The price is {price} dollars"
print(txt) # The price is 59 dollars
``` 

A placeholder can include a modifier to format the value.

A `modifier` is included by adding a colon : followed by a legal formatting type, like `.2f` which means fixed point number with 2 decimals:
```python
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt) # The price is 59.00 dollars
``` 
`Note: it can also round up the value, if price is 56.237 it will round up to 56.24`

A placeholder can contain Python code, like math operations:
```python
txt = f"The price is {20 * 59} dollars"
print(txt) # The price is 1180 dollars
``` 

## Escape Characters
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash `\` followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
```python
# You will get an error if you use double quotes inside a string that is surrounded by double quotes:
txt = "We are the so-called "Vikings" from the north." # Gives an error.
``` 
To fix this problem, use the escape character \":
```python
txt = "We are the so-called \"Vikings\" from the north."
``` 

Other escape characters used in Python:
| Code | Result | Example |
| ---- | ------ | ------- |
| \\'	| Single Quote | txt = 'It\\'s alright.' |
| \\\	| Backslash | txt = "This will insert one \\\ (backslash)." |
| \n	| New Line | txt = "Hello\nWorld!" |
| \r	| Carriage Return |	txt = "Hello\rWorld!" |
| \t	| Tab |	txt = "Hello\tWorld!" - Hello   World! |
| \b	| Backspace, Erases one Character | txt = "Hello \bWorld!" - HelloWorld! |
| \f	| Form Feed |	|
| \ooo	| Octal value | txt = "\110\145\154\154\157" - 	prints Hello |
| \xhh	| Hex value | txt = "\x48\x65\x6c\x6c\x6f" - prints Hello |

```
Note: 
- A backslash followed by three integers will result in a octal value.
- A backslash followed by an 'x' and a hex number represents a hex value:
```
