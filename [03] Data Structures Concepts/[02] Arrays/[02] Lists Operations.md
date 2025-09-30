
# 📌 Python Lists Operations

View it in Detail here: [Python Tutorial](https://www.w3schools.com/python/default.asp)

## Overview
- Loop Lists
- List Comprehension
- Sort Lists
- Copy Lists
- Join Lists

### Loop Through a List:
You can loop through the list items by using a `for` loop:
```python
# Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
```
#### 1. Loop Through the Index Numbers:
You can also loop through the list items by referring to their index number.

Use the `range()` and `len()` functions to create a suitable iterable.
```python
# Print all items by referring to their index number:

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
```
`The iterable created in the example above is [0, 1, 2].`

#### 2. Using a While Loop
You can loop through the list items by using a `while` loop.

Use the `len()` function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.

Remember to increase the index by 1 after each iteration.
```python
# Print all items, using a while loop to go through all the index numbers

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
```

#### 3. Looping Using List Comprehension
List Comprehension offers the shortest syntax for looping through lists:
```python
# A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
```

### List Comprehension:
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example: 
Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

#### 1. Comparing Normal Looping with List Comprehension
Without list comprehension you will have to write a `for` statement with a conditional test inside:
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) # ['apple', 'banana', 'mango']
```
With list comprehension you can do all that with only one line of code:
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) # ['apple', 'banana', 'mango']
```

#### 2. The Syntax:
`newlist = [expression for item in iterable if condition == True]`

The return value is a new list, leaving the old list unchanged.
#### 2.1) Condition
The `condition` is like a filter that only accepts the items that valuate to `True`.
```python
# Only accept items that are not "apple":
newlist = [x for x in fruits if x != "apple"] 

# ['banana', 'cherry', 'kiwi', 'mango']
```
The condition `if x != "apple"`  will return `True` for all elements other than "apple", making the new list contain all fruits except "apple".

The `condition` is optional and can be omitted:
```python
# With no if statement: 
newlist = [x for x in fruits] 

# ['apple', 'banana', 'cherry', 'kiwi', 'mango']
```
#### 2.2) Iterable
The `iterable` can be any iterable object, like a list, tuple, set etc.
```python
# You can use the range() function to create an iterable:
newlist = [x for x in range(10)] 

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
Same example, but with a condition:
```python
# Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5] # [0, 1, 2, 3, 4]
```
#### 2.3) Expression
The `expression` is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
```python
# Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits] 

# ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']
```
You can set the outcome to whatever you like:
```python
# Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits] 

# ['hello', 'hello', 'hello', 'hello', 'hello']
```
The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
```python
# Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits] 

# ['apple', 'orange', 'cherry', 'kiwi', 'mango']
```
The expression in the example above says:

`"Return the item if it is not banana, if it is banana return orange".`

### Sort Lists
#### 1. Sort List Alphanumerically
List objects have a `sort()` method that will sort the list alphanumerically, ascending, by default:
```python
# Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']
```
```python
# Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) # [23, 50, 65, 82, 100]
```
#### 2. Sort Descending
To sort descending, use the keyword argument `reverse = True`:
```python
# Sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist) # ['pineapple', 'orange', 'mango', 'kiwi', 'banana']
```
```python
# Sort the list descending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist) # [100, 82, 65, 50, 23]
```
#### 3. Customize Sort Function
You can also customize your own function by using the keyword argument `key = function`.

The function will return a number that will be used to sort the list (the lowest number first):
```python
# Sort the list based on how close the number is to 50:

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist) # [50, 65, 23, 82, 100]
```

#### 4. Case Insensitive Sort
By default the `sort()` method is case sensitive, resulting in all capital letters being sorted before lower case letters:
```python
# Case sensitive sorting can give an unexpected result:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) # ['Kiwi', 'Orange', 'banana', 'cherry']
```
Luckily we can use built-in functions as key functions when sorting a list.

So if you want a case-insensitive sort function, use str.lower as a key function:

```python
# Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) # ['banana', 'cherry', 'Kiwi', 'Orange']
```

#### 5. Reverse Order
What if you want to reverse the order of a list, regardless of the alphabet?

The `reverse()` method reverses the current sorting order of the elements.
```python
# Reverse the order of the list items:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) # ['cherry', 'Kiwi', 'Orange', 'banana']
```

### Copy a List
You cannot copy a list simply by typing `list2 = list1`, because: `list2` will only be a reference to `list1`, and changes made in `list1` will automatically also be made in `list2`.
#### Use the copy() method
You can use the built-in List method `copy()` to copy a list.
```python
# Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) # ["apple", "banana", "cherry"]
```
#### Use the list() method
Another way to make a copy is to use the built-in method `list()`.
```python
# Make a copy of a list with the list() method:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist) # ["apple", "banana", "cherry"]
```
#### Use the slice Operator
You can also make a copy of a list by using the `:` (slice) operator.
```python
# Make a copy of a list with the : operator:

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist) # ["apple", "banana", "cherry"]
```

### Join Lists
There are several ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the `+` operator.
```python
# Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) # ['a', 'b', 'c', 1, 2, 3]
```
Another way to join two lists is by appending all the items from list2 into list1, one by one:
```python
# Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1) # ['a', 'b', 'c', 1, 2, 3]
```
Or you can use the `extend()` method, where the purpose is to add elements from one list to another list:
```python
# Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1) # ['a', 'b', 'c', 1, 2, 3]
```