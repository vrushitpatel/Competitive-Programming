
# 📌 Python Lists

View it in Detail here: [Python Tutorial](https://www.w3schools.com/python/default.asp)

## Overview
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

### List Basics:
#### Create a List -
Lists are created using square brackets:
```python
thislist = ["apple", "banana", "cherry"] 
print(thislist) # ["apple", "banana", "cherry"]
```
#### List Items -
List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.

#### Ordered -
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.

**Note:** There are some [list methods](https://www.w3schools.com/python/python_lists_methods.asp) that will change the order, but in general: the order of the items will not change.

#### Allow Duplicates -
Since lists are indexed, lists can have items with the same value. Example:
```python
thislist = ["apple", "banana", "cherry", "apple", "cherry"] # ['apple', 'banana', 'cherry', 'apple', 'cherry']
print(thislist)
```

#### List Length -
To determine how many items a list has, use the len() function:
```python
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) # 3
```
#### List Items - Data Types
List items can be of any data type:

Example: `String`, `int` and `boolean` data types:
```python
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
```
A list can contain `different data types`. Example
A list with strings, integers and boolean values:
```python
list1 = ["abc", 34, True, 40, "male"]
```

#### type() - 
From Python's perspective, lists are defined as objects with the data type 'list': `print(type(mylist)) ----> <class 'list'>`

#### The list() Constructor -
It is also possible to use the list() constructor when creating a new list.
```python
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist) # ['apple', 'banana', 'cherry']
```

### Access List Items:
#### Access Items -
List items are indexed and you can access them by referring to the index number:
```python
# Print the second item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # banana
``` 
`Note: The first item has index 0.`

#### Negative Indexing -
Negative indexing means start from the end. `-1` refers to the last item, `-2` refers to the second last item etc.
```python
#Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) # cherry
```
#### Range of Indexes -
You can specify a range of indexes by specifying where to start and where to end the range. When specifying a range, the return value will be a new list with the specified items.
```python
# Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # ['cherry', 'orange', 'kiwi']
```

`Note: The search will start at index 2 (included) and end at index 5 (not included).`

By leaving out the start value, the range will start at the first item:
```python
# This example returns the items from the beginning to, but NOT including, "kiwi":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) # ['apple', 'banana', 'cherry', 'orange']
```
By leaving out the end value, the range will go on to the end of the list:
```python
# This example returns the items from "cherry" to the end:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) # ["cherry", "orange", "kiwi", "melon", "mango"]
```

#### Range of Negative Indexes -
Specify negative indexes if you want to start the search from the end of the list:
```python
# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) # ['orange', 'kiwi', 'melon']
```

#### Check if Item Exists -
To determine if a specified item is present in a list use the `in` keyword:
```python
# Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") # Yes, 'apple' is in the fruits list
```

### Change List Items:
#### Change Item Value - 
To change the value of a specific item, refer to the index number:
```python
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) # ['apple', 'blackcurrant', 'cherry']
```
#### Change a Range of Item Values
To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) # ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
```
If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

```python
# Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"] # ['apple', 'blackcurrant', 'watermelon', 'cherry']
print(thislist)
```

`Note: The length of the list will change when the number of items inserted does not match the number of items replaced.`
If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

```python
# Change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"] # ['apple', 'watermelon']
print(thislist)
```

### Add List Items:
#### Insert Items -
To insert a new list item, without replacing any of the existing values, we can use the `insert()` method.

The `insert()` method inserts an item at the specified index:

```python
#Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") # ['apple', 'banana', 'watermelon', 'cherry']
print(thislist)
```
`Note: As a result of the examples above, the lists will now contain 4 items.`

#### Append Items -
To add an item to the end of the list, use the `append()` method:
```python
thislist = ["apple", "banana", "cherry"]
thislist.append("orange") # ['apple', 'banana', 'cherry', 'orange']
print(thislist)
```

#### Extend List -
To append elements from another list to the current list, use the `extend()` method.
```python
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
```

#### Add Any Iterable -
The `extend()` method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

```python
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) # ['apple', 'banana', 'cherry', 'kiwi', 'orange']
```

### Remove List Items:
#### Remove Specified Item -
The `remove()` method removes the specified item.
```python
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) # ['apple', 'cherry']
```
If there are more than one item with the specified value, the `remove()` method removes the first occurrence:
```python
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) # ['apple', 'cherry', 'banana', 'kiwi']
```

#### Remove Specified Index
The `pop()` method removes the specified index.
```python
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) # ['apple', 'cherry']
```

If you do not specify the index, the `pop()` method removes the last item.
```python
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) # ['apple', 'banana']
```
#### Delete the List -
The `del` keyword also removes the specified index:
```python
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #this will cause an error because you have succsesfully deleted "thislist".
```
#### Clear the List -
The `clear()` method empties the list.

The list still remains, but it has no content.
```python
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # []
```
