# 📌 Python Lists

View it in Detail here: [Python List Tutorial](https://www.w3schools.com/python/python_lists.asp)

## Overview

Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

### List Basics:

- Lists are created using square brackets
- List items are ordered, changeable, and allow duplicate values.
- List items are indexed, the first item has index [0], the second item has index [1] etc.
- When we say that lists are ordered, it means that the items have a defined order, and that order will not change. If you add new items to a list, the new items will be placed at the end of the list.

**Note:** There are some [list methods](https://www.w3schools.com/python/python_lists_methods.asp) that will change the order, but in general: the order of the items will not change.

- Since lists are indexed, lists can have items with the same value.

#### List Items - Data Types

- List items can be of any data type:
  - Example: `String`, `int` and `boolean` data types:
- A list can contain `different data types`. Example
  - A list with strings, integers and boolean values:

```python
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list4 = ["abc", 34, True, 40, "male"]
```

## A cheat sheet for the most fundamental operations for the Python `list` data structure.

<table>
  <thead>
    <tr>
      <th>Method</th>
      <th>Description</th>
      <th>Code Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td><strong>Creation</strong> <code>[]</code> or <code>list()</code></td>
        <td>Lists are created using square brackets Or Using the list() Constructor</td>
        <td>
<pre><code>
thislist = ["apple", "banana", "cherry"]
print(thislist) # ["apple", "banana", "cherry"]
<br/>
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist) # ['apple', 'banana', 'cherry']
</code></pre>
        </td>
    </tr>
<!---------------------------------------------------------------------------------------------->
    <tr>
        <td><strong>List Length</strong> - use the <code>len()</code> function:</td>
        <td>Length of the Array/List</td>
        <td>
<pre><code>
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) # 3
</code></pre>
        </td>
    </tr>
<!---------------------------------------------------------------------------------------------->
    <tr>
        <td><code>type()</code> function:</td>
        <td>From Python's perspective, lists are defined as objects with the data type 'list'</td>
        <td>
<pre><code>
print(type(mylist)) ----> class 'list'
</code></pre>
        </td>
    </tr>
<!---------------------------------------------------------------------------------------------->
    <tr>
        <td>Access Items </td>
        <td>List items are indexed and you can access them by referring to the index number. <br>Note: The first item has index 0.</td>
        <td>
<pre><code>
# Print the second item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # banana
</code></pre>

</td>
</tr>

<!---------------------------------------------------------------------------------------------->
<tr>
        <td><strong>Negative Indexing</strong> </td>
        <td>Negative indexing means start from the end. -1 refers to the last item, -2 refers to the second last item etc.</td>
        <td>

<pre><code>
#Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) # cherry
</code></pre>

</td>
</tr>

<!---------------------------------------------------------------------------------------------->
<tr>
        <td><strong>Range of Indexes</strong> </td>
        <td>You can specify a range of indexes by specifying where to start and where to end the range. When specifying a range, the return value will be a new list with the specified items. <br> Note: The search will start at index 2 (included) and end at index 5 (not included). </td>
        <td>

<pre><code>
# Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # ['cherry', 'orange', 'kiwi']
</code></pre>

</td>
</tr>

<!---------------------------------------------------------------------------------------------->
<tr>
        <td></td>
        <td>By leaving out the start value, the range will start at the first item:</td>
        <td>

<pre><code>
# This example returns the items from the beginning to, but NOT including, "kiwi":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) # ['apple', 'banana', 'cherry', 'orange']
</code></pre>

</td>
</tr>

<!---------------------------------------------------------------------------------------------->
<tr>
        <td></td>
        <td>By leaving out the end value, the range will go on to the end of the list:</td>
        <td>

<pre><code>
# This example returns the items from "cherry" to the end:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) # ["cherry", "orange", "kiwi", "melon", "mango"]
</code></pre>

</td>
</tr>

<!---------------------------------------------------------------------------------------------->
<tr>
        <td><strong>Range of Negative Indexes</strong></td>
        <td>Specify negative indexes if you want to start the search from the end of the list:</td>
        <td>

<pre><code>
# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) # ['orange', 'kiwi', 'melon']
</code></pre>

</td>
</tr>

<!---------------------------------------------------------------------------------------------->
<tr>
        <td><strong>Check if Item Exists</strong></td>
        <td>To determine if a specified item is present in a list use the <code>in</code> keyword:</td>
        <td>

<pre><code>
# Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") # Yes, 'apple' is in the fruits list
</code></pre>

</td>
</tr>

<!---------------------------------------------------------------------------------------------->
<tr>
        <td><strong>Change Single Item Value </strong></td>
        <td>To change the value of a specific item, refer to the index number:</td>
        <td>

<pre><code>
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) # ['apple', 'blackcurrant', 'cherry']
</code></pre>

</td>
</tr>

<!---------------------------------------------------------------------------------------------->
<tr>
        <td><strong>Change a Range of Item Values</strong></td>
        <td>To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:</td>
        <td>

<pre><code>
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) # ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
</code></pre>

</td>
</tr>

<!---------------------------------------------------------------------------------------------->
<tr>
        <td></td>
        <td>If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly: <br> Note: The length of the list will change when the number of items inserted does not match the number of items replaced.</td>
        <td>

<pre><code>
# Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"] # ['apple', 'blackcurrant', 'watermelon', 'cherry']
print(thislist)
</code></pre>

</td>
</tr>

<!---------------------------------------------------------------------------------------------->
<tr>
        <td></td>
        <td>If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly: <br> Note: The length of the list will change when the number of items inserted does not match the number of items replaced.</td>
        <td>

<pre><code>
# Change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"] # ['apple', 'watermelon']
print(thislist)
</code></pre>

</td>
</tr>

<!---------------------------------------------------------------------------------------------->
<tr>
        <td><strong>Add List Items: Insert Items</strong></td>
        <td>To insert a new list item, without replacing any of the existing values, we can use the <code>insert()</code> method. The <code>insert()</code> method inserts an item at the specified index:</td>
        <td>

<pre><code>
#Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") # ['apple', 'banana', 'watermelon', 'cherry']
print(thislist)
</code></pre>

</td>
</tr>

<!---------------------------------------------------------------------------------------------->
<tr>
        <td><strong>Add List Items: Append Items</strong></td>
        <td>To add an item to the end of the list, use the <code>append()</code> method: </td>
        <td>

<pre><code>
thislist = ["apple", "banana", "cherry"]
thislist.append("orange") # ['apple', 'banana', 'cherry', 'orange']
print(thislist)
</code></pre>

</td>
</tr>

<!---------------------------------------------------------------------------------------------->
<tr>
        <td><strong>Add List Items: Extend List</strong></td>
        <td>To append elements from another list to the current list, use the <code>extend()</code> method: </td>
        <td>

<pre><code>
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
</code></pre>

</td>
</tr>

<!---------------------------------------------------------------------------------------------->
<tr>
        <td><strong>Add List Items: Add Any Iterable</strong></td>
        <td>The <code>extend()</code> method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.). </td>
        <td>

<pre><code>
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) # ['apple', 'banana', 'cherry', 'kiwi', 'orange']
</code></pre>

</td>
</tr>

<!---------------------------------------------------------------------------------------------->
<!---------------------------------------------------------------------------------------------->
<tr>
        <td><strong>Remove List Items: Remove Specified Item </strong></td>
        <td>The <code>remove()</code> method removes the specified item. <br>If there are more than one item with the specified value, the `remove()` method removes the first occurrence:</td>
        <td>

<pre><code>
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) # ['apple', 'cherry']
<br>
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) # ['apple', 'cherry', 'banana', 'kiwi']
</code></pre>

</td>
</tr>

<!---------------------------------------------------------------------------------------------->
<tr>
        <td><strong>Remove List Items: Remove Specified Index </strong></td>
        <td>The <code>pop()</code> method removes the specified index.<br>If you do not specify the index, the `pop()` method removes the last item.</td>
        <td>

<pre><code>
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) # ['apple', 'cherry']
<br>
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) # ['apple', 'banana']
</code></pre>

</td>
</tr>

<!---------------------------------------------------------------------------------------------->
<tr>
        <td><strong>Delete the List </strong></td>
        <td>The <code>del</code> keyword also removes the specified index:</td>
        <td>

<pre><code>
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #this will cause an error because you have succsesfully deleted "thislist".
</code></pre>

</td>
</tr>

<!---------------------------------------------------------------------------------------------->
<tr>
        <td><strong>Clear the List </strong></td>
        <td>The <code>clear()</code> method empties the list. The list still remains, but it has no content.</td>
        <td>

<pre><code>
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # []
</code></pre>

</td>
</tr>

<!---------------------------------------------------------------------------------------------->

  </tbody>
</table>
